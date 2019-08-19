import requests

from .endpoints.apirequest import APIRequest
from .exceptions import APIError, BadEnvironment

import time
import jwt
import json

ENVIRONMENTS = {
    "DEMO": {
        "DATA": "https://api-demo.exante.eu/md",
        "TRADE": "https://api-demo.exante.eu/trade",
        "FEED": "https://api-demo.exante.eu/md",
    },
    "LIVE": {"DATA": "", "TRADE": ""},
}


class ExanteAPI(object):
    def __init__(
        self,
        client_id: str,
        application_id: str,
        shared_key: str,
        api_scopes: list,
        environment: str = "DEMO",
    ):
        self.client_id = client_id
        self.application_id = application_id
        self.shared_key = shared_key
        self.api_scopes = api_scopes

        try:
            ENVIRONMENTS[environment]

        except Exception:
            raise BadEnvironment(f"Unknown environment: {environment}")

        else:
            self.environment = environment

        self.session = requests.Session()
        self.token = self.generate_token(
            client_id=self.client_id,
            application_id=self.application_id,
            api_scopes=self.api_scopes,
            shared_key=shared_key,
        )

    def create_payload(self, client_id: str, application_id: str, api_scopes: list):
        iat = int(time.time())

        # expire in 1 hour ToDo: make expiration as parameter

        return {
            "iss": client_id,
            "sub": application_id,
            "iat": int(iat),
            "exp": int(iat + 60 * 60),
            "aud": api_scopes,
        }

    def generate_token(
        self, client_id: str, application_id: str, api_scopes: list, shared_key: str
    ):
        """
            Generate JWT token

        :return:
         token

        """

        payload = self.create_payload(
            client_id=client_id, application_id=application_id, api_scopes=api_scopes
        )

        token = jwt.encode(payload, shared_key, "HS256").decode()

        return token

    def __make_request(
        self,
        method: str,
        url: str,
        query_params: dict,
        data_params: dict,
        headers: dict = None,
    ) -> requests.Response:
        """
            Makes HTTP request to endpoint
        """

        if headers is None:
            headers = {}

        headers.update({"authorization": "Bearer {}".format(self.token)})

        response = None

        if method == "GET":
            response = self.session.get(url=url, params=query_params, headers=headers)

        if method == "POST":
            response = self.session.post(url=url, json=data_params, headers=headers)

        if response.status_code >= 400:
            raise APIError(response.status_code, response.content.decode("utf-8"))

        return response

    def __make_feed_request(self, url: str, query_params: dict, headers: dict):
        """
            Makes HTTP request to feed endpoint
        """

        if headers is None:
            headers = {}

        response = self.session.get(
            url=url, params=query_params, headers=headers, stream=True
        )
        lines = response.iter_lines(60)
        for line in lines:
            if line:
                data = json.loads(line.decode("utf-8"))
                yield data

    def request(self, endpoint: APIRequest) -> :
        """
            Perform a request for the APIRequest instance 'endpoint'

            :param endpoint:
            :return:
        """

        method = endpoint.method.upper()
        url = f"{ENVIRONMENTS[self.environment][endpoint.scope]}{endpoint}"

        try:
            query_params = getattr(endpoint, "params")

        except AttributeError:
            query_params = {}

        try:
            data_params = getattr(endpoint, "data")

        except AttributeError:
            data_params = {}

        header = {}

        if hasattr(endpoint, "HEADER"):
            header = getattr(endpoint, "HEADER")

        header.update({"Authorization": "Bearer {}".format(self.token)})

        scope = getattr(endpoint, "SCOPE")

        if scope == "FEED":
            response = self.__make_feed_request(
                url=url, query_params=query_params, headers=header
            )

            return response

        else:
            response = self.__make_request(
                method=method,
                url=url,
                query_params=query_params,
                data_params=data_params,
                headers=header,
            )

            content = response.json()

            endpoint.response = content
            endpoint.status_code = response.status_code

            return response
