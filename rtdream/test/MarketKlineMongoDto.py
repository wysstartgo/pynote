import urllib3
import pandas as pd

import ExceptionEnum as ee


class MarketKlineMongoDto(object):
    def __init__(self,symbol,name,date,open,low,close,high,volume,amount,time):
        self.symbol = symbol
        self.name = name
        self.date = date
        self.open = open
        self.low = low
        self.close = close
        self.high = high
        self.volume = volume
        self.amount = amount
        self.time = time

    #
    # 从json转成对象
    #
    def jsonToObj(self,mkmd):
        pass


    poolManager = urllib3.PoolManager()
    response = poolManager.request('GET','http://192.168.1.156:898/InfoOpSys/market/klineByTime?symbol=000001.SZ&startTime=1492412400000&endTime=1495522800000&resolution=9')
    print(type(response.data))
    #print(str(response.data.decode('utf-8')))
    jsonRes = pd.io.json.loads(response.data)
    print(str(ee.ExceptionEnum.Success))
    if(jsonRes['code'] == ee.ExceptionEnum.Success.value):
        print(type(jsonRes))
        #print(str(jsonRes['data']))
        pdData = pd.DataFrame(jsonRes['data'])
        print(pdData)

  #  pdData = pd.DataFrame(pd.json.loads(response.data).data)
  #  print(pdData)