from .apirequest import APIRequest


class Accounts(APIRequest):
    """
        Collection of user accounts.
    """

    ENDPOINT = "/1.0/accounts"
    METHOD = "GET"
    SCOPE = "DATA"

    def __init__(self):
        super(Accounts, self).__init__(
            self.ENDPOINT, method=self.METHOD, scope=self.SCOPE
        )


class AccountSummary(Accounts):
    """
        Account summary
    """

    ENDPOINT = "/1.0/summary/{account_id}/{currency}"

    def __init__(self, account_id: str, currency: str = "EUR"):
        endpoint = self.ENDPOINT.format(account_id=account_id, currency=currency)

        super(Accounts, self).__init__(endpoint, method=self.METHOD, scope=self.SCOPE)
