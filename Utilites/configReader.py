from configparser import ConfigParser


def readConfig(section, key):
    config = ConfigParser()
    config.read(".\\Configrationdata\\config.ini")
    return config.get(section, key)

