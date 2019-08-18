class APIRequest(object):
    def __init__(self, endpoint: str, method: str = "GET", scope: str = "DATA"):
        self._endpoint = endpoint
        self._response = None

        self.method = method
        self.scope = scope

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        self._response = value

    def __str__(self):
        return self._endpoint
