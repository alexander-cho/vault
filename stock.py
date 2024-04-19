from security import Security


class Stock(Security):
    def __init__(self, ticker_symbol, **kwargs):
        super().__init__(ticker_symbol, **kwargs)

    def __str__(self):
        super().__str__()
