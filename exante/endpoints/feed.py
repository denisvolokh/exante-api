from .apirequest import APIRequest


class Feed(APIRequest):
    """
        Stream of symbol(s) price updates.

        URI Parameters:
         - symbols: required (string)

        Example:
            /1.0/feed/MSFT.NASDAQ,AAPL.NASDAQ,GAZP.MICEX
    """

    ENDPOINT = "/2.0/feed/{symbols}"
    METHOD = "GET"
    SCOPE = "FEED"
    HEADER = {"Accept": "application/x-json-stream"}

    def __init__(self, symbols: str):
        endpoint = self.ENDPOINT.format(symbols=symbols)

        super(Feed, self).__init__(endpoint, method=self.METHOD, scope=self.SCOPE)
