import math
import pymongo as pm
import datetime as date
import json
import time
import pandas as pd
from functools import reduce
import numpy as np

# 计算EMA
def ema(count, data=None):
    closeValue = data
    alpha = 2 / (count + 1)
    ema_last = 0
    isStart = True
    result = []
    for i in range(len(closeValue)):
        if (closeValue[i] == None):
            result.append(None)
            continue

        if (isStart):
            v = closeValue[i]
            result.append(v)
            ema_last = v
            isStart = False
            continue
        else:
            v = (ema_last + (closeValue[i] - ema_last) * alpha)
            result.append(v)
            ema_last = v
    return result
 #计算MA
 #计算MA
def ma(timeperiod, data=None):
    closeValue = data
    result = []
    for i in range(len(closeValue)):
        if (i >= timeperiod):
            total = 0
            count = 0
            subIndex = 0
            while subIndex < timeperiod:
                if (closeValue[i-subIndex] != None):
                    total = total + closeValue[i-subIndex]
                    count = count + 1
                subIndex = subIndex + 1
            if (total != None and count > 0):
                result.append(total/count)
            else:
                result.append(None)
        else:
            result.append(None)

    return result

  #计算SMA 权重MA
def sma(maperiod, weight, data=None):
    closeValue = data
    result = []
    for i in range(len(closeValue)):
        if (i >= maperiod):
            total = 0
            count = 0
            subIndex = 0

            if (i == maperiod or ( i> maperiod and result[-1] == None )):
                while subIndex < maperiod:
                    if (closeValue[i - subIndex] != None):
                        total = total + closeValue[i - subIndex]
                        count = count + 1
                    subIndex = subIndex + 1
                if (total != None and count > 0):
                    result.append(total / count)
                else:
                    result.append(None)
            else:
                if (result[-1] != None and closeValue[i] != None):
                    result.append( ((weight*closeValue[i]) + (maperiod-weight)*result[-1])/maperiod )
                else:
                    result.append(None)
        else:
            result.append(None)

    return result

#
#
#https://baike.baidu.com/item/EMA/12646151?fr=aladdin
#http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.ewma.html
#
def cal_ema(dataList,span):
    # print(str(closeList))
    # print('================================================')
    pdData = pd.DataFrame(dataList, columns=['date', 'symbol', 'high', 'low', 'close', 'open'])
    # print(pdData)
    seriesResult = pdData['close'].rolling(window=12, center=False, min_periods=1).mean()
    # print(seriesResult)
    # maList = [12,26,9]
    maList = [9]
    pClose = pdData['close']
    # print(pd.rolling_mean(pClose,window=2,min_periods=9))
    for ma in maList:
        result = pd.rolling_mean(pdData['close'], ma)
        # print('===============' + str(result))
    # EMAfast = pd.Series(pd.ewma(df[price], span=n_fast, min_periods=n_slow - 1))
    #    EMAslow = pd.Series(pd.ewma(df[price], span=n_slow, min_periods=n_slow - 1))
    #    MACD = pd.Series(EMAfast - EMAslow, name='MACD_%d_%d' % (n_fast, n_slow))
    #    MACDsign = pd.Series(pd.ewma(MACD, span=9, min_periods=8), name='MACDsign_%d_%d' % (n_fast, n_slow))
    #    MACDdiff = pd.Series(MACD - MACDsign, name='MACDdiff_%d_%d' % (n_fast, n_slow))
    #    result = pd.DataFrame([MACD, MACDsign, MACDdiff]).transpose()
    #    return out(SETTINGS, df, result)
    # s = pd.Series(pd.ewma(pdData['close'],span=9,min_periods=1))
    # print('===================' + str(s))
    #
    # s2 = pdData['close'].ewm(span=9,min_periods=1).mean()
    # print('*****' + str(s2))
    # 用pandas计算ema
    emaRes = pd.ewma(pdData['close'], span=span, adjust=True) #adjust=False表示不进行加权
    # print('=============' + str(emaRes))
    # emaList = ema(9, pClose)
    # print('******************' + str(emaList))
    # pdData['close'].plot(figsize=(9, 5), grid=True)
    # plt.show()
    # print('===================' + str(count))
    return emaRes

# 算法
#求X的N日移动平均，M为权重
# Y = (X*M + Y'*(N-M)) / N
#算法：若Y=SMA(X,N,M) 则 Y=(M*X+(N-M)*Y')/N，其中Y'表示上一周期Y值，N必须大于M。
# 2种实现，结果相同
# 注：使用SMA函数，历史数据越多越准确，EMA同
def SMA(vals, n, m) :
    # 算法1
    # L = [vals[0]]
    # reduce(lambda x,y:print('x' + str(x) + ',y:' + str(y)),vals)
    # print('***************************************************')
    # reduce(lambda x, y: ((n - m) * x + y * m) / n, vals)
    L = []
    ret = vals[0]
    for x in vals:
        L.append(ret)
        ret = (x * m + ret * (n - m)) / n
    return L


# def cal_sma(x,y,n,m,L):
#     print('x:' + str(type(x)))
#     print('=======================')
#     print('y:' + str(type(y)))
#     if(x):
#         print('****' + str(type(x)))
#         if(isinstance(L,list)):
#             L.append(((n - m) * x + y * m) / n)

#
#https://baike.baidu.com/item/SMA%E5%9D%87%E7%BA%BF/7238642
#https://www.joinquant.com/post/1708
#
def cal_sma(vals,period,weight):
    print(str(vals))
    print('************************************************')
    if not isinstance(vals, pd.Series):
        return []
    if(len(vals) > period):
        #取得前面几个的平均数
        previousAverage = vals[:period].rolling(window=period,min_periods=period).mean()
        print('pre type:' + str(type(previousAverage)))
        previousAverageList = np.array(previousAverage).tolist()
        print('pre:' + str(previousAverageList))
        for nextSma in pd.Series(vals)[period:]:
            previousAverageList.append(((period - weight) * previousAverageList[-1] + nextSma * weight) / period)
        return previousAverageList
    else:
        return []
#
#
#  https://baike.baidu.com/item/%E7%A7%BB%E5%8A%A8%E5%B9%B3%E5%9D%87%E7%BA%BF/217887?fr=aladdin
#
def cal_ma():
    # 8.15、 8.07、 8.84、 8.10、 8.40、 9.10、 9.20、 9.10、 8.95、 8.70
    testData = [8.15, 8.07, 8.84, 8.10, 8.40, 9.10, 9.20, 9.10, 8.95, 8.70]
    #这里计算的是5日移动平均线
    testRes = pd.Series(testData).rolling(window=5, min_periods=5).mean()
    print('=================' + str(testRes))

    testData2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    testRes2 = pd.Series(testData2).rolling(window=5, min_periods=5).mean()
    print('000000000000000' + str(testRes2))

 #https://baike.baidu.com/item/MACD%E6%8C%87%E6%A0%87/6271283?fromtitle=MACD&fromid=3334786&fr=aladdin
 #
 # 计算MACD
def macd(data, fastperiod=12, slowperiod=26, signalperiod=9):
    #计算fast_ema
    fast_ema = cal_ema(data,fastperiod)
    #计算slow_ema
    slow_ema = cal_ema(data,slowperiod)
    #计算diff
    series_diff = fast_ema - slow_ema
    #计算DEA
    series_dea = cal_ema(series_diff,signalperiod)
    #计算macd
    series_macd = 2 * (series_diff - series_dea)
    print('----------------' + str(series_macd))
    return series_diff,series_dea,series_macd

#获取连接mongodb://zx:zx123456@192.168.1.133:20001,192.168.1.134:20001,192.168.1.135:20001/zx
# document_class={'maxPoolSize':10,'minPoolSize':1,'maxIdleTimeMS':60000,'socketTimeoutMS':5000}
#"mongodb://192.168.1.191:20000,192.168.1.192:20000,192.168.1.193:20000"
#client = pm.MongoClient("mongodb://192.168.1.192:20000")
client = pm.MongoClient("192.168.1.192",20000,maxPoolSize=10,minPoolSize=1,maxIdleTimeMS=60000,socketTimeoutMS=5000)
#连接数据库
db = client.zx
#获取集合
col = db.business_market_kline_1d
#http://192.168.1.183:898/InfoOpSys/market/klineByTime?symbol=000001.SZ&startTime=1492412400000&endTime=1495522800000&resolution=9

#http://192.168.1.156:898/InfoOpSys/market/klineByTime?symbol=000001.SZ&startTime=1492412400000&endTime=1495522800000&resolution=9
colls = db.collection_names(include_system_collections=False)
print(colls)
#获取数据
# cursor = col.find({'symbol':'MAUTD'})
#
# for data in cursor:
#     print(data)
# count = col.find({'symbol':'MAUTD'}).count()
# print('================' + str(count))
sTime = 1492412400000/1000.0
startTime = date.datetime.strftime(date.datetime.utcfromtimestamp(sTime),"%Y-%m-%d %H:%M:%S")
eTime = 1495522800000/1000.0
endTime = date.datetime.strftime(date.datetime.utcfromtimestamp(eTime),"%Y-%m-%d %H:%M:%S")
print(type(startTime))
print(endTime)
print(type(col))
returnFields = {'_id':False}
cursor = col.find({'symbol':'000001.SZ','date':{'$gte':startTime,'$lte':endTime}},projection=returnFields,sort=[('date',1)])
dataList = []
closeList = []
print(type(cursor))
for data in cursor:
   # print(data)
   # print(type(data))
    dataList.append(data)
    closeList.append(data['close'])
    # jsonData = json.loads(data)
    # print(type(jsonData))
#计算ema
cal_ema(dataList,5)
#计算ma
pdDatas = pd.DataFrame(dataList,columns=['date', 'symbol', 'high', 'low', 'close', 'open'])
# maRes = pdDatas['close'].rolling(window=25,min_periods=1).mean()
# print('---------------' + str(maRes))
#
# print('===============' + str(ma(9,pdDatas['close'])))
# rolResult = pd.rolling_mean(pdDatas['close'],window=25,min_periods=1)
# print('99999999999999999999999999999:' + str(rolResult))

#计算sma
# sRes1 = cal_sma(pdDatas['close'],5,2)
# print(str(sRes1))
# print('============================================')
# sRes2 = sma(5,2,pdDatas['close'])
# print(str(sRes2))

#计算macd
macd(pdDatas)




























##################time包 https://blog.csdn.net/QQ331948781/article/details/45079427
# import datetime
# import time
#
# timeStamp = 1427349630000
# timeStamp /= 1000.0
# print
# timeStamp
# timearr = time.localtime(timeStamp)
# otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timearr)
# print
# otherStyleTime


