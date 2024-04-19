class Security:
    def __init__(self, ticker_symbol, **kwargs):
        self.ticker_symbol = ticker_symbol

    def __str__(self):
        return self.ticker_symbol
