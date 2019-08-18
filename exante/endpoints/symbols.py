from .apirequest import APIRequest


class Symbols(APIRequest):
    """
        The collection of the available trading symbols.
        Please note that the symbol list is subject to change, and it needs to be updated from time to time.
    """

    ENDPOINT = "/1.0/symbols"
    METHOD = "GET"
    SCOPE = "DATA"

    def __init__(self, params=None):
        super(Symbols, self).__init__(
            self.ENDPOINT, method=self.METHOD, scope=self.SCOPE, params=params
        )


class Symbol(APIRequest):
    """
        The collection of the available trading symbols.
        Please note that the symbol list is subject to change, and it needs to be updated from time to time.
    """

    ENDPOINT = "/1.0/symbols/{symbol_id}"
    METHOD = "GET"
    SCOPE = "DATA"

    def __init__(self, symbol_id: str):
        endpoint = self.ENDPOINT.format(symbol_id=symbol_id)

        super(Symbol, self).__init__(endpoint, method=self.METHOD, scope=self.SCOPE)


class SymbolSpecification(APIRequest):
    """
        The collection of the available trading symbols.
        Please note that the symbol list is subject to change, and it needs to be updated from time to time.
    """

    ENDPOINT = "/1.0/symbols/{symbol_id}/specification"
    METHOD = "GET"
    SCOPE = "DATA"

    def __init__(self, symbol_id: str):
        endpoint = self.ENDPOINT.format(symbol_id=symbol_id)

        super(SymbolSpecification, self).__init__(
            endpoint, method=self.METHOD, scope=self.SCOPE
        )
