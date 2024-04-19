from stock import Stock


class Portfolio:

    def __init__(self, name, initial_balance=100000):
        self.name = name
        self.initial_balance = float(initial_balance)
        self.holdings = {}

    def display_holdings(self):
        pass

    def deposit_cash(self):
        pass

    def withdraw_cash(self):
        pass

    def get_share_price(self):
        pass

    def create_stock_buy_order(self) -> Stock:
        pass

    def create_stock_sell_order(self) -> Stock:
        pass

    def buy_stock(self, buy_order, price):
        pass

    def sell_stock(self, sell_order, price):
        pass

    def __str__(self):
        return f'This is the account of {self.name}'
