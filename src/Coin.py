from coinmarketcap import Market

class coin:
    def __init__(self, prozent, symbol):

        self.prozent = prozent
        self.symbol = symbol
        self.price = self.getMarketPrice()
        self.amt = 0.0
        self.worth =0.0

    def getMarketPrice(self):
        coinmarketcap = Market()
        listings = coinmarketcap.ticker()
        for symbolOn in listings['data'].items():
            if symbolOn[1]['symbol']==self.symbol:
                return symbolOn[1]['quotes']['USD']['price']
        return 0.0
