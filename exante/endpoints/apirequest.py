class APIRequest(object):
    def __init__(self, endpoint: str, method: str = "GET", scope: str = "DATA", expected_status: int = 200):
        self._endpoint = endpoint
        self._response = None
        self._status_code = None
        self._expected_status = 200

        self.method = method
        self.scope = scope

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        self._response = value

    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value

    @property
    def expected_status(self):
        return self._expected_status

    @expected_status.setter
    def expected_status(self, value):
        self._expected_status = value

    def __str__(self):
        return self._endpoint
