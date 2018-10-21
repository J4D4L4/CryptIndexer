class portfolio:
    #fuellungsGrad=0
    #coins = list()
    #market = dict()

    def __init__(self, marketSize, maxSlize, investmentSize):
        self.market=getMarket(marketSize)
        self.fuellungsGrad = 0
        self.coins = list()
        self.maxSlize = maxSlize
        self.investmentSize = investmentSize