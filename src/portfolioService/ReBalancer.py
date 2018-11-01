from src.portfolioService.Trade import trade
from src.portfolioService.Coin import coin
class Rebalancer:
    def __init__(self):

        super().__init__()

    def getReBalanceTrades(self,portfolioOld, portfolioNew, minDiffrence):
        trades=list()
        sellOrder=list()
        buyOrder=list()

        count =0

        copyNewPortfolio = portfolioNew.coins.copy()
        while (count<len(portfolioOld.coins)):
        #for coin in portfolioOld.coins:

            coinOld = portfolioOld.coins[count]
            testPortfolioCoins=portfolioOld.coins.copy()

            count2=0
            if self.checkIfSymbolInPortfolio(coinOld.symbol,portfolioNew):
                indexOfCoinInNew=self.getIndexOfSymbol(coinOld.symbol,portfolioNew)
                coinNew=portfolioNew.coins[indexOfCoinInNew]
                if abs(coinOld.prozent-coinNew.prozent)>=float(minDiffrence):
                    trades.append(self.calcReBalanceTrade(coinOld,coinNew))
                copyNewPortfolio.remove(coinNew)
                '''
                for coinNew in portfolioNew.coins:

                    if coinOld.symbol==coinNew.symbol:
                        coinOld=1
                        if abs(coinNew.prozent-coinOld.prozent)>=float(minDiffrence):
                            trades.append(self.calcReBalanceTrade(coinOld,coinNew))

                        copyNewPortfolio.remove(coinNew)
                '''
            else:
                textTade = "Sell: Sell " + str(coinOld.amt) + " " + coinOld.symbol + ". This is " + str(abs(coinOld.worth)) + "$ worth of the Coin."
                trades.append(trade('Sell',textTade, coinOld.amt,coinOld.worth,coinOld.symbol))

            count+=1
        if len(copyNewPortfolio) != 0:
            for coin in copyNewPortfolio:
                tradeText = textTade = "Buy: Buy " + str(coin.amt) + " " + coin.symbol + ". This is " + str(abs(coin.worth)) + "$ worth of the Coin."
                trades.append(trade('Buy', textTade, coin.amt, coin.worth,coin.symbol))

        return trades

    def calcReBalanceTrade(self,coinOld,coinNew):
        diffrence = coinOld.worth - coinNew.worth
        diffrenceCoins=diffrence/coinNew.price
        if diffrence>0:

            textTade="Sell: Sell "+str(abs(diffrenceCoins))+" "+coinNew.symbol+ ". This is "+ str(abs(diffrence))+"$ worth of the Coin."

            nTrade = trade("Sell",textTade,diffrenceCoins,abs(diffrence),coinNew.symbol )
        elif diffrence<0:
            textTade = "Buy: Buy " + str(diffrenceCoins) + " " + coinNew.symbol + ". This is " + str(diffrence) + "$ worth of the Coin."
            nTrade = trade("Buy", textTade, abs(diffrenceCoins), abs(diffrence),coinNew.symbol)
        return nTrade



    def removeEmptyCoins(self,portfolio):
        count=0
        cCoins=portfolio.coins.copy()
        while count<len(portfolio.coins):
            if float(portfolio.coins[count].amt)<=0.0:
                cCoins.remove(portfolio.coins[count])
            count+=1
        portfolio.coins=cCoins
        return portfolio

    def tradeOnPortfolio(self,oldPortfolio,trade):
        foundCoin = 0
        for tCoin in oldPortfolio.coins:
            if tCoin.symbol==trade.symbol:
                if trade.type=="Buy":
                    tCoin.worth+=trade.value
                    cAmt=float(tCoin.amt)+float(trade.amt)
                    tCoin.amt=str(cAmt)
                    foundCoin=1
                    break
                else:
                    tCoin.worth-=trade.value
                    cAmt=float(tCoin.amt)-float(trade.amt)
                    tCoin.amt=str(cAmt)
                    foundCoin=1
                    break

        #### todo check if needed can probally be deleted
        if foundCoin==0:
            nCoin=coin(0,trade.symbol)
            nCoin.amt=str(trade.amt)
            nCoin.worth=trade.value
            #oldPortfolio.coins.append(coin())
            oldPortfolio.coins.append(nCoin)

        return oldPortfolio
    def checkIfSymbolInPortfolio(self,symbol,portfolio):
        inPortfolio = bool(0)
        for inCoin in portfolio.coins:
            if inCoin.symbol == symbol:
                inPortfolio= bool(1)
        return inPortfolio
    def getIndexOfSymbol(self,symbol,portfolio):

        for  checkCoin in (portfolio.coins):
            if checkCoin.symbol==symbol:
                index = portfolio.coins.index(checkCoin)
        return index
