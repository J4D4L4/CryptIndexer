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
    def reCalcPortfolio(self):
        self.calcInvestmentSlize()
        for cCoin in self.coins:
            cCoin.prozent=(100/self.investmentSize)*cCoin.worth
        return self

    def calcInvestmentSlize(self):
        self.investmentSize = 0
        for cCoin in self.coins:
            self.investmentSize+=cCoin.worth

    def getCoin(self, symbol):
        for iCoin in self.coins:
            if iCoin.symbol == symbol:
                return iCoin

    def reSortCoins(self,inPortfolio):
        newCoinList=list()
        for iCoin in inPortfolio.coins:
            newCoinList.append(self.getCoin(iCoin.symbol))
        return newCoinList

