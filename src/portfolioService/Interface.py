from src.portfolioService.CoinMarketCrawler import CoinMarketCrawlerService
import matplotlib.pyplot as plt
import numpy as np
from src.portfolioService.BrokerCrawler import Config
from src.portfolioService.BrokerCrawler import binanceAPI
from src.portfolioService.Portfolio import portfolio
from src.portfolioService.ReBalancer import Rebalancer


class Interface:
    def consoleIntefaceMainMenu(self):


        choice = input('Press 1 to create Your Config(do this the first time in the Programm. Press 2 to create Portfolio) Press 3 to Rebalance your Portfolio')
        if (choice =="1"):
            config = Config()
            iniConfig = config.createNewConfig()
        elif(choice=='2'):
            myPortfolio = self.consoleInterfaceCreatePortfolio()
            label = CoinMarketCrawlerService.getListofSymbols(myPortfolio.coins)
            prozent = CoinMarketCrawlerService.getListofProzent(myPortfolio.coins)
            values = CoinMarketCrawlerService.getListOfValues(myPortfolio.coins)
            amtCoins = CoinMarketCrawlerService.getListOfAmtCoins(myPortfolio.coins)
            self.printBarChart(myPortfolio.coins)

            for coin in myPortfolio.coins:
                print(str(coin.symbol) + ":" + str(coin.amt) + " Worth: " + str(coin.worth) + "$ Portfolio Slize: " + str(
                    coin.prozent))
        elif(choice=='3'):
            binance=binanceAPI()
            minChange=input('min % diffrence when rebalancing should be done')
            currentPortfolio=binance.getUserPortfolio()
            newPortfolio = self.consoleInterfaceReBalance(currentPortfolio)
            #newPortfolio.worth=currentPortfolio.worth
            trades=list()
            reBalance=Rebalancer()
            trades=reBalance.getReBalanceTrades(currentPortfolio,newPortfolio,minChange)
            for nTrade in trades:
                print(nTrade.text)
            self.printBarChart(newPortfolio.coins)
            newOldPortfolio=portfolio(0,0,0)
            for trde in trades:
                newOldPortfolio=reBalance.removeEmptyCoins(reBalance.tradeOnPortfolio(currentPortfolio,trde))
            newOldPortfolio=newOldPortfolio.reCalcPortfolio()
            self.printBarChartfor2(newOldPortfolio.coins,newPortfolio.coins)
            self.printBarChartfor3(currentPortfolio.coins,newPortfolio.coins, newPortfolio.coins)
            print(newOldPortfolio)

        else :
            print("wrong input")

    def consoleInterfaceCreatePortfolio(self):
        print('Create your Crypto Index')
        print('-------------------------')
        try:
            investSize = int(input('How much do you want to invest? (In $)'))
        except ValueError:
            print("thats not a number")
            return



        print('-------------------------')
        try:
            amtOfSymbols = int(input('The index can include the top x Symbols. What should x be? '))
        except ValueError:
            print("thats not a number")
            return

        print('-------------------------')
        try:
            highestPortfolioProzentage = int(input('What should be the highes prozentage allocation to a single Coin?(the lower the number the higher the focus on smaller alt coins'))
        except ValueError:
            print("thats not a number")
            return
        print('-------------------------')
        myPortfolio = portfolio(int(amtOfSymbols), int(highestPortfolioProzentage), int(investSize))
        print ("the current Symbols are:")

        repeat=1
        symbols = list()
        while True:
            print(CoinMarketCrawlerService.listSymbols(myPortfolio))
            try:
                exclude = input('enter the symbol you want to exclude. If you do not want to exclude anything enter: 0')
                if exclude=='0':
                    break
                else:
                    symbols.append(exclude)
                    myPortfolio.market = CoinMarketCrawlerService.removeSymbol(myPortfolio.market, symbols)
            except ValueError:
                print("thats not a number")
                return

        print('-------------------------')
        print('Creating Portfolio')
        myPortfolio = CoinMarketCrawlerService.calcPortfolio(myPortfolio)
        #for coin in myPortfolio.coins:
            #print(str(coin.symbol) + ": "+ str(coin.prozent)+"%")
        return myPortfolio

    def consoleInterfaceReBalance(self, oldPortfolio):
        print('Create your Crypto Index')
        print('-------------------------')
        try:
            investSize = oldPortfolio.investmentSize
        except ValueError:
            print("thats not a number")
            return

        print('-------------------------')
        try:
            amtOfSymbols = int(input('The index can include the top x Symbols. What should x be? '))
        except ValueError:
            print("thats not a number")
            return

        print('-------------------------')
        try:
            highestPortfolioProzentage = int(input(
                'What should be the highes prozentage allocation to a single Coin?(the lower the number the higher the focus on smaller alt coins'))
        except ValueError:
            print("thats not a number")
            return
        print('-------------------------')
        myPortfolio = portfolio(int(amtOfSymbols), int(highestPortfolioProzentage), int(investSize))
        print("the current Symbols are:")

        repeat = 1
        symbols = list()
        while True:
            print(CoinMarketCrawlerService.listSymbols(myPortfolio))
            try:
                exclude = input('enter the symbol you want to exclude. If you do not want to exclude anything enter: 0')
                if exclude == '0':
                    break
                else:
                    symbols.append(exclude)
                    myPortfolio.market = CoinMarketCrawlerService.removeSymbol(myPortfolio.market, symbols)
            except ValueError:
                print("thats not a number")
                return

        print('-------------------------')
        print('Creating Portfolio')
        myPortfolio = CoinMarketCrawlerService.calcPortfolio(myPortfolio)
        # for coin in myPortfolio.coins:
        # print(str(coin.symbol) + ": "+ str(coin.prozent)+"%")
        return myPortfolio

    def printBarChart(self,coins):
        n_groups = len(coins)
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.35


        rects1 = ax.bar(index,CoinMarketCrawlerService.getListofProzent(coins), bar_width, label='Symbol')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(CoinMarketCrawlerService.getListofSymbols(coins))

        fig.tight_layout()
        plt.show()

    def printBarChartfor2(self,coinsOld, coinsNew):
        n_groups = len(coinsOld)
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.35


        rects1 = ax.bar(index,CoinMarketCrawlerService.getListofProzent(coinsOld), bar_width, label='Symbol')
        rects2 = ax.bar(index + bar_width, CoinMarketCrawlerService.getListofProzent(coinsNew), bar_width,label='Symbol')
        ax.set_xticks(index + bar_width / 2)

        ax.set_xticklabels(CoinMarketCrawlerService.getListofSymbols(coinsOld))
        ax.legend((rects1[0], rects2[0]), ('RealPortfolio', 'Calculatetd Index'))
        fig.tight_layout()
        plt.show()

    def printBarChartfor3(self,coinsOld, coinsNew, coinsOldwithTrades):
        n_groups = len(coinsOld)
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.35


        rects1 = ax.bar(index,CoinMarketCrawlerService.getListofProzent(coinsOld), bar_width, label='Symbol')
        rects2 = ax.bar(index + bar_width, CoinMarketCrawlerService.getListofProzent(coinsNew), bar_width,label='Symbol')
        rects3 = ax.bar(index + bar_width, CoinMarketCrawlerService.getListofProzent(coinsOldwithTrades), bar_width,label='Symbol')
        ax.set_xticks(index + bar_width / 3)

        ax.set_xticklabels(CoinMarketCrawlerService.getListofSymbols(coinsOld))
        ax.legend((rects1[0], rects2[0]), rects3[0], ('Old Portfolio', 'New Portfolio','Calculatetd Index'))
        fig.tight_layout()
        plt.show()

Interface().consoleIntefaceMainMenu()