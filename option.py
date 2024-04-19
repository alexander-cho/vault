from security import Security


class Option(Security):
    def __init__(self, ticker_symbol, expiration_date, strike_price, **kwargs):
        super().__init__(ticker_symbol, **kwargs)
        self.expiration_date = expiration_date
        self.strike_price = strike_price

    def __str__(self):
        super().__str__()
