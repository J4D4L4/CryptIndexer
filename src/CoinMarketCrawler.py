from coinmarketcap import Market
import matplotlib.pyplot as plt
import numpy as np
from src.BrokerCrawler import Config
from src.Coin import coin
from src.Portfolio import portfolio

import json
import copy

class CoinMarketCrawlerService:
    def getMarketWorth(ticker, symbol):
        marketCounter=0
        symbolReached = 0
        for tick in ticker['data'].items():
            if tick[1]['symbol'] == symbol:
                symbolReached=1
            if symbolReached == 1:
                marketCounter += tick[1]['quotes']['USD']['market_cap']
        return marketCounter



    def getCoin(coin, ticker):
        for tick in ticker['data'].items():
            if str(tick[1]['symbol']) == coin:
                return tick[1]

        return 0
    #def calcRestMarketWorth(portfolio, symbol)
     #   symbolReached = 0
      #  for symbol in portfolio.market.items

    def calcSlize(portfolio, symbol):
        prozentLeft = 100 - CoinMarketCrawlerService.calcProzentVergeben(portfolio.coins)
        marketWorthfromSymbol = CoinMarketCrawlerService.getMarketWorth(portfolio.market, symbol)
        infoCoin = CoinMarketCrawlerService.getCoin(symbol, portfolio.market)
        marketCap = infoCoin['quotes']['USD']['market_cap']
        price  = infoCoin['quotes']['USD']['price']
        prozent= (prozentLeft/marketWorthfromSymbol)*marketCap
        if prozent > portfolio.maxSlize:
            prozent = portfolio.maxSlize
        #print(prozent)
        nCoin = coin(prozent, symbol)
        nCoin = CoinMarketCrawlerService.calcCoinAmt(nCoin, portfolio.investmentSize)
        return nCoin

    def calcProzentVergeben(coinList):
        cProzent = 0
        for eCoin in coinList:
           cProzent += eCoin.prozent
        #print(eCoin.symbol)
        return cProzent

    def calcPortfolio(portfolio):

        for symbol in portfolio.market['data'].items():
            portfolio.coins.append(CoinMarketCrawlerService.calcSlize(portfolio,symbol[1]["symbol"]))
        return portfolio

    def listSymbols(portfolio):
        symbols =list()
        for symbol in portfolio.market['data'].items():
            symbols.append(symbol[1]["symbol"])

        return symbols
    def calcCoinAmt(coin, portfolioSize):
        coin.worth = ((portfolioSize/100)*coin.prozent)
        coin.amt = coin.worth/coin.price
        return coin

    def removeSymbol(market, symbols):
        nMarket= copy.deepcopy(market)
        for key, symbol in market['data'].items():
            if symbol['symbol']  in symbols:
                nMarket['data'].pop(key)
        return nMarket

    def getListofSymbols(coins):
        symbols = list()
        for coin in coins:
            symbols.append(coin.symbol)
        return symbols

    def getListofProzent(coins):
        prozent = list()
        for coin in coins:
            prozent.append(coin.prozent)
        return prozent

    def getListOfValues(coins):
        values = list()
        for coin in coins:
            values.append(coin.worth)
        return values

    def getListOfAmtCoins(coins):
        amtCoins = list()
        for coin in coins:
            amtCoins.append(coin.amt)
        return amtCoins





