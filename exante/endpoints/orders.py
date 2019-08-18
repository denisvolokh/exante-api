from .apirequest import APIRequest


class Orders(APIRequest):
    """
        List orders

    """

    ENDPOINT = "/1.0/orders"
    METHOD = "GET"
    SCOPE = "TRADE"

    def __init__(self, params: dict = None):
        """
            Instantiate a Orders APIRequest instance.

                Parameters
                ----------

                params : dict (required)
                    parameters for the request, check https://developers.exante.eu/api/#1_0_orders for details.
        """

        super(Orders, self).__init__(
            self.ENDPOINT, method=self.METHOD, scope=self.SCOPE
        )

        self.params = params


class OrderCreate(Orders):
    """
        Create an Order
    """

    METHOD = "POST"

    def __init__(self, data):
        super(OrderCreate, self).__init__()
        self.data = data
