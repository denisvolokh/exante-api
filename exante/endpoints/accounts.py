from .apirequest import APIRequest


class Accounts(APIRequest):
    """
        Collection of user accounts.
    """

    ENDPOINT = "/1.0/accounts"
    METHOD = "GET"
    SCOPE = "DATA"
    EXPECTED_STATUS = 200

    def __init__(self):
        super(Accounts, self).__init__(
            self.ENDPOINT,
            method=self.METHOD,
            scope=self.SCOPE,
            expected_status=self.EXPECTED_STATUS,
        )


class AccountSummary(APIRequest):
    """
        Account summary
    """

    ENDPOINT = "/1.0/summary/{account_id}/{currency}"
    METHOD = "GET"
    SCOPE = "DATA"
    EXPECTED_STATUS = 200

    def __init__(self, account_id: str, currency: str = "EUR"):
        endpoint = self.ENDPOINT.format(account_id=account_id, currency=currency)

        super(AccountSummary, self).__init__(
            endpoint, method=self.METHOD, scope=self.SCOPE
        )
