class APIError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

        super(APIError, self).__init__(message)


class BadEnvironment(Exception):
    def __init__(self, message):
        self.message = message

        super(BadEnvironment, self).__init__(message)
