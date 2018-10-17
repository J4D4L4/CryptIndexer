from abc import ABC, abstractmethod
import configparser

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

    def createConfig(self):
        config = configparser.ConfigParser()
        with open('settings.ini','w') as config_file:
            config.write(config_file)

    def readConfig(self):
        f = open('settings.ini')
        config = f.read()
        f.close()
        return config

    def getConfig(self):
        config = configparser.ConfigParser()
        readConfig = config.read('settings.ini')
        return readConfig

    def creatSection(config, section):
        config.add_section(section)
        return config

    def addToSection(config, section, option, value):
        config.set(section,option,value)
        return config
