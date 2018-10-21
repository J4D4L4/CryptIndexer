import hashlib
from abc import ABC, abstractmethod
import configparser
import os

import binance as binance
import requests
import time
import hmac
from binance.client import Client
#from src.CoinMarketCrawler import portfolio
#from src.Coin import coin
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

class Config():

    def __init__(self):

        super().__init__()

    def createConfig(self, ):
        config = configparser.ConfigParser()
        with open('settings.ini','w') as config_file:
            config.write(config_file)
        return config

    def readConfig(self):
        settings = configparser.ConfigParser()
        settings._interpolation = configparser.ExtendedInterpolation()
        settings.read('settings.ini')
        return settings

    def getConfig(self):
        config = configparser.ConfigParser()
        readConfig = config.read('settings.ini')
        return readConfig

    def creatSection(self, section):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        if not config.has_section(section):
            config.add_section(section)
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)
        return config

    def addToSection(self, section, option, value):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        config.set(section,option,value)
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)
        return config
    def createNewConfig(self):

        print("Creating Config")
        if not os.path.exists('settings.ini'):
            config = self.createConfig()
        print("adding Binance broker")
        self.creatSection("Binance")
        pubKey=input("Enter public Key: ")
        privKey=input("Enter priv Key: ")
        self.addToSection("Binance","pubKey",pubKey)
        self.addToSection( "Binance", "prvKey", privKey)
        print ("config Created")
        print("PubKey is: "+ self.readConfig().get("Binance","pubKey"))
        return config

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

    def getUserPortfolio(self):

        config=Config()
        portfolio = list()
        client = Client(config.readConfig().get("Binance","pubKey"), config.readConfig().get("Binance","prvkey"))
        info = client.get_account()

        print(info)

#config = Config()
#config.createConfig()
#inConfig = config.readConfig()
#iniConfig = config.createNewConfig()
#restCall().getUserPorfolio()
binanceAPI().getUserPortfolio()