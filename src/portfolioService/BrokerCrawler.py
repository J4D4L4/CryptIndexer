import hashlib
from abc import ABC, abstractmethod

import requests
import time
import hmac
from binance.client import Client
from src.portfolioService.Config import Config
from src.portfolioService.Coin import coin
from src.portfolioService.Portfolio import portfolio

#abstract broker
class Broker(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def getMyPortfolio(self):
        pass


class restCall():
    def __init__(self):

        super().__init__()

    kwargs=list()
    config=Config()
    burl='https://api.binance.com/'

    def getUserPorfolio(self):

        query='api/v3/account'
        timeQuery="/api/v1/time"
        url=self.burl+query
        timeUrl=self.burl+timeQuery

        parameter="?"
        serverTime = requests.get(timeUrl)

        keyPara='?X-MBX-APIKEY='+  self.config.readConfig().get("Binance","pubKey")
        timePara= '?timestamp='+ str(time.time())[:14].replace('.','')
        hearder={'X-MBX-APIKEY' : self.config.readConfig().get("Binance","pubKey")

        }
        self.kwargs['data']["timestamp"] = timePara
        secret=self._generate_signature(self.kwargs['data'])
        requestUrl= url+timePara
        r = requests.get(requestUrl,   auth=secret)
        print(r.json())
    def _generate_signature(self, data):

        ordered_data = self._order_params(data)
        query_string = '&'.join(["{}={}".format(d[0], d[1]) for d in ordered_data])
        m = hmac.new(self.API_SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256)
        return m.hexdigest()

class binanceAPI:
    def __init__(self):

        super().__init__()
    def getClient(self):
        config = Config()
        client = Client(config.readConfig().get("Binance","pubKey"), config.readConfig().get("Binance","prvkey"))
        return client
    def getUserPortfolio(self):


        binancePortfolio = portfolio(0, 0, 0)
        symbolList=list()
        client=self.getClient()
        info = client.get_account()
        balance = info['balances']

        for symbol in balance:
            if float(symbol['free']) != 0.0:
                nCoin = coin(0,symbol["asset"])
                #binanceSymbolInfo=self.getSymbolPrice(symbol["asset"])

                nCoin.amt=symbol['free']
                nCoin.worth=float(nCoin.amt)*float(nCoin.price)
                symbolList.append(nCoin)
                binancePortfolio.coins.append(nCoin)
                binancePortfolio.investmentSize+=nCoin.worth
        for itCoin in binancePortfolio.coins:
            itCoin.prozent=(100/binancePortfolio.investmentSize)*itCoin.worth

        return binancePortfolio






#config = Config()
#config.createConfig()
#inConfig = config.readConfig()
#iniConfig = config.createNewConfig()
#restCall().getUserPorfolio()
binanceAPI().getUserPortfolio()