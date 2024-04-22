class Portfolio:

    def __init__(self, name):
        self.name = name
        self.holdings = {}

    def buy(self, ticker, num_shares):
        # check for proper parameter types
        if isinstance(ticker, str) and isinstance(num_shares, int):
            # check if stock is already owned
            if ticker in self.holdings.keys():
                self.holdings[ticker] += num_shares
            else:
                self.holdings[ticker] = num_shares
        else:
            raise TypeError('Ticker must be a string, number of shares must be an integer')

        print(f'You bought {num_shares} shares of {ticker}')

    def sell(self, ticker, num_shares):
        # check for proper parameter types
        if isinstance(ticker, str) and isinstance(num_shares, int):
            # check is stock is already owned
            if ticker in self.holdings.keys():
                # check if investor is trying to sell more than they own
                if num_shares > self.holdings[ticker]:
                    print("You cannot sell more than you already have.")
                else:
                    self.holdings[ticker] -= num_shares
            else:
                print("You don't own that stock.")
        else:
            raise TypeError('Ticker must be a string, number of shares must be an integer')

        print(f'You sold {num_shares} shares of {ticker}')

    def display_holdings(self) -> dict:
        print(self.holdings)
        return self.holdings

    def __str__(self):
        return f'This is the account of {self.name}'


if __name__ == '__main__':
    a = Portfolio('alex')

    try:
        a.buy('SOFI', 100)
        a.buy('AFRM', 50)
        a.buy('UPST', 40)
        a.buy('TSLA', 10)
        a.buy('HOOD', 75)
        a.buy(3, 'LC')
    except Exception as e:
        print(e)

    a.display_holdings()
