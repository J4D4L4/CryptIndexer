from abc import ABC, abstractmethod
import configparser
import os

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

#config = Config()
#config.createConfig()
#inConfig = config.readConfig()
#iniConfig = config.createNewConfig()
