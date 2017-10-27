import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import constants

"""
This is a common utils class file which can be used across py packages
"""


def gettickerdata(tickername):
    """
    function calls bloomberg API and scraps the current price
    """

    r = requests.get(constants.bloomurl + getticker(tickername) + ':US')
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all('div', class_="price")
    return ("$" + results[0].text)


def getticker(ticker):
    """
    getticker: connect to mongoDB hosted in mLab
    """
    # getDBConnection
    db = getDBConnection()
    # getTable
    tickerCollection = db['tickerdata']
    tkrlist = tickerCollection.find({"Name": {"$regex": "^" + ticker, "$options": 'i'}})
    # print (tickerCollection.find({"Name":{"$regex":"^"+ticker,"$options":'i'}}).explain())
    # get possible combination of the ticker val
    tickrCombination = map((ticker + '{0}').format, [".", ",", " "])

    if tkrlist.count() > 1:
        for i in tkrlist:
            if (i['Name'][:len(tickrCombination[0])] in tickrCombination):
                return i['Symbol']
    else:
        return tkrlist[0]['Symbol']


def getDBConnection():
    """
    client = MongoClient('mongodb://localhost:27017/')
    return DB data
    :return:
    """
    # Connect to mLab DB
    client = MongoClient(constants.mongo_uri)
    # getDB
    db = client['stockitdb']
    return db


def ticker_wrapper(ticker):
    """
    This is a wrapper to get the ticker data
    """


pass
