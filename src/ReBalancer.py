from src.Trade import trade
class Rebalancer:
    def __init__(self):

        super().__init__()

    def getReBalanceTrades(self,portfolioOld, portfolioNew, minDiffrence):
        trades=list()
        sellOrder=list()
        buyOrder=list()

        count =0
        while (count<len(portfolioOld.coins)):
        #for coin in portfolioOld.coins:
            coinOld=0
            coin = portfolioOld.coins[count]
            for coinNew in portfolioNew.coins:

                if coin.symbol==coinNew.symbol:
                    coinOld=1
                    if abs(coinNew.prozent-coin.prozent)>=float(minDiffrence):
                        trades.append(self.calcReBalanceTrade(coin,coinNew))
                    portfolioNew.coins.remove(coinNew)
            if count==len(portfolioOld.coins)-1:
                tradeText=textTade = "Sell: Sell " + str(coin.amt) + " " + coin.symbol + ". This is " + str(abs(coin.worth)) + "$ worth of the Coin."
                trades.append(trade('Sell',textTade, coin.amt,coin.worth))
            count+=1
        if len(portfolioNew.coins) != 0:
            for coin in portfolioNew.coins:
                tradeText = textTade = "Buy: Buy " + str(coin.amt) + " " + coin.symbol + ". This is " + str(abs(coin.worth)) + "$ worth of the Coin."
                trades.append(trade('Buy', textTade, coin.amt, coin.worth))

        return trades

    def calcReBalanceTrade(self,coinOld,coinNew):
        diffrence = coinOld.worth - coinNew.worth
        diffrenceCoins=diffrence/coinNew.price
        if diffrenceCoins>0:

            textTade="Buy: Buy "+str(diffrenceCoins)+" "+coinNew.symbol+ ". This is "+ str(diffrence)+"$ worth of the Coin."

            nTrade = trade("Buy",textTade,diffrenceCoins,diffrence )
        elif diffrenceCoins<0:
            textTade = "Sell: Sell " + str(diffrenceCoins) + " " + coinNew.symbol + ". This is " + str(diffrence) + "$ worth of the Coin."
            nTrade = trade("Sell", textTade, abs(diffrenceCoins), abs(diffrence))
        return nTrade