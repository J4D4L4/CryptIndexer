from coinmarketcap import Market

class portfolio:
    #fuellungsGrad=0
    #coins = list()
    #market = dict()

    def __init__(self, marketSize, maxSlize, investmentSize):
        self.market=self.getMarket(marketSize)
        self.fuellungsGrad = 0
        self.coins = list()
        self.maxSlize = maxSlize
        self.investmentSize = investmentSize

    def getMarket(self, nrOfPositions):
        coinmarketcap = Market()
        linstings = coinmarketcap.listings()
        ticker = coinmarketcap.ticker(start=0, limit=nrOfPositions, convert='USD')
        return ticker