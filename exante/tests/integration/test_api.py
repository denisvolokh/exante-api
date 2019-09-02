import logging
import os

import betamax
import pytest

from exante.endpoints.accounts import Accounts, AccountSummary
from exante.exceptions import APIError

logger = logging.getLogger("integration")
logger.setLevel(level=logging.DEBUG)


class TestSaxoOpenAPI(object):
    """
        Integration tests for the Exanty API object.
    """

    @pytest.fixture(autouse=True)
    def setup(self, exante_api_demo_client, exante_api_demo_client_no_scopes):
        """
            Create ExanteAPI and Betamax instances.
        """

        self.client = exante_api_demo_client
        self.recorder = betamax.Betamax(session=self.client.session)

        self.client_no_scopes = exante_api_demo_client_no_scopes
        self.recorder_no_scopes = betamax.Betamax(session=self.client_no_scopes.session)

    @staticmethod
    def generate_cassette_name(method_name):
        """Generate cassette names for tests."""
        return "exante_api__" + method_name

    def test__accounts_list(self):
        """
            Verify we can get a list of accounts
        """

        accounts_list_request = Accounts()

        cassette_name = self.generate_cassette_name("accounts_list")
        with self.recorder.use_cassette(cassette_name):
            accounts_list_response = self.client.request(accounts_list_request)

        assert isinstance(accounts_list_response, list)

    def test__account_details(self):
        account_id = os.getenv("EXANTE__ACCOUNT_ID", None)

        account_summary_request = AccountSummary(account_id=account_id, currency="USD")

        cassette_name = self.generate_cassette_name("account_details")
        with self.recorder.use_cassette(cassette_name):

            with pytest.raises(APIError):
                self.client_no_scopes.request(account_summary_request)
