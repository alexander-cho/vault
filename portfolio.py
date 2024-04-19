class Portfolio:

    def __init__(self, name):
        self.name = name
        self.holdings = {}

    def buy(self, ticker, num_shares):
        if ticker in self.holdings.keys():
            self.holdings[ticker] += num_shares
        else:
            self.holdings[ticker] = num_shares

        print(f'You bought {num_shares} shares of {ticker}')

    def sell(self, ticker, num_shares):
        if ticker in self.holdings.keys():
            if num_shares > self.holdings[ticker]:
                print("You cannot sell more than you already have.")
            else:
                self.holdings[ticker] -= num_shares
        else:
            print("You don't own that stock.")

        print(f'You sold {num_shares} shares of {ticker}')

    def display_holdings(self) -> dict:
        print(self.holdings)
        return self.holdings

    def __str__(self):
        return f'This is the account of {self.name}'


if __name__ == '__main__':
    a = Portfolio('alex')
    a.buy('SOFI', 100)
    a.buy('AFRM', 50)
    a.buy('UPST', 40)
    a.buy('TSLA', 10)
    a.buy('HOOD', 75)
    a.buy('LC', 100)
    a.display_holdings()
