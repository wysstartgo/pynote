
import imp
import sys
import json
import urllib3
import ssl
import redis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class CQuantMainContent:
    def __init__(self):
        pass
class CQuantArrayNode:
    def __init__(self):
        pass

def getHtml(url):
    http = urllib3.PoolManager();
    r = http.request('GET',url)
    print (r.status)
    html = r.data
    return html

def getUrl(content):
    pass


def init(v1):
    content = CQuantMainContent()

    content.file = v1
    content.marketCode =  'WALL_XAUUSD'
    content.dataSort = 'dec'
    content.startTime = 222
    content.endTime = 111
    content.klineType = 11
    content.pageSize = 11
    myClassDict = content.__dict__
    myClassJson = json.dumps(myClassDict)
    print (myClassJson)
    B = imp.load_source('B', content.file)
    import B

    m = 10
    B.init(content)

    print (m)
    ssl._create_default_https_context = ssl._create_unverified_context

    url = "http://192.168.1.183:808/InfoOpSys/market/kline?symbol=WALL_XAUUSD&sort=dec&time=1520546399999&resolution=9&count=400"

    html = getHtml(url)
    print (html)
    print ('xxxxxxxxxxxxxxxxxxx')
    datas = json.loads(html).get("data")

    content.OPEN = []
    content.DATE = []
    content.CLOSE= []
    content.HIGH = []
    content.LOW = []
    content.VOL = []
    content.AMOUNT = []
    for data in datas:
        content.OPEN.insert(0,data.get('open'))
        content.DATE.insert(0,data.get('date'))
        content.HIGH.insert(0, data.get('high'))
        content.LOW.insert(0, data.get('low'))


        content.CLOSE.insert(0,data.get("close"))

        if (data.get('volume')==None):
            content.VOL.insert(0,0)
        else:
            content.VOL.insert(0, data.get('volume'))

        if (data.get('amount')==None):
            content.AMOUNT.insert(0,0)
        else:
            content.AMOUNT.insert(0, data.get('amount'))

    print (content.OPEN)
    print (content.DATE)
    print (content.VOL)
    print (content.AMOUNT)
    print (datas)

    B.handle_bar(content)
    r = redis.Redis(host='192.168.1.182',password='reRedis123',port=6379)
    r.set('strategy_key','hello')
    print (r.get('strategy_key'))
    print (content.a)
    print (content.b)
    return 1000