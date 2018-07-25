import urllib3
import ssl
import json
import time
import talib
import  numpy
import math


#自定义数据结构
class RtArrayObject:
    def __init__(self, data = []):
        self.data = data
    def __getitem__(self, key):
        return self.data[key]
    def initIndication(self):
        self.__macd = None
    def __setitem__(self, key, value):
        self.initIndication()
        self.data[key] = value
    def setData(self, data):
        self.initIndication()
        self.data = data
    def insert(self, key, value):
        self.initIndication()
        self.data.insert(key, value)
    def append(self, value):
        self.initIndication()
        self.data.append(value)
    def length(self):
        if (self.data == None):
            return 0
        else:
            return len(self.data)

    def setKey(self, key):
        self.key = key
    def getKey(self):
        return self.key

    def toJson(self):
        return {self.key : self.data}



    def __add__(self, obj):
        arr = []
        if (isinstance(obj, RtArrayObject)):
            for i in range(self.length()):
                if (self[i] != None and obj[i] != None):
                    arr.append(self[i] + obj[i])
                else:
                    arr.append(None)
        else:
            for i in range(self.length()):
                if (self[i] != None):
                    arr.append(self[i] + obj)
                else:
                    arr.append(None)
        return RtArrayObject(arr)

    def __sub__(self, obj):
        arr = []
        if (isinstance(obj, RtArrayObject)):
            for i in range(self.length()):
                if (self[i] != None and obj[i] != None):
                    arr.append(self[i] - obj[i])
                else:
                    arr.append(None)
        else:
            for i in range(self.length()):
                if (self[i] != None):
                    arr.append(self[i] - obj)
                else:
                    arr.append(None)
        return RtArrayObject(arr)

    def __mul__(self, obj):
        arr = []
        if (isinstance(obj, RtArrayObject)):
            for i in range(self.length()):
                if (self[i] != None and obj[i] != None):
                    arr.append(self[i] * obj[i])
                else:
                    arr.append(None)
        else:
            for i in range(self.length()):
                if (self[i] != None):
                    arr.append(self[i] * obj)
                else:
                    arr.append(None)
        return RtArrayObject(arr)

    def __neg__(self):
        arr = []
        for i in range(self.length()):
            if (self[i] != None):
                arr.append(-self[i])
            else:
                arr.append(None)

        return RtArrayObject(arr)

    def __truediv__(self, obj):
        arr = []
        if (isinstance(obj, RtArrayObject)):
            for i in range(self.length()):
                if (self[i] != None and obj[i] != None and obj[i] != 0):
                    arr.append(self[i] / obj[i])
                else:
                    arr.append(None)
        else:
            for i in range(self.length()):
                if (self[i] != None and obj != 0):
                    arr.append(self[i] / obj)
                else:
                    arr.append(None)
        return RtArrayObject(arr)

    def REF(self, number):
        arr = []
        for i in range(self.length()):
            if (i < number):
                arr.append(None)
            else:
                arr.append(self[i - numpy])

        return RtArrayObject(arr)

    def __and__(self, obj):
        arr = []
        for i in range(self.length()):
            if (self[i] != None and obj[i] != None):
                if (self[i] and obj[i]):
                    arr.append(True)
                else:
                    arr.append(False)
            else:
                arr.append(None)

        return RtArrayObject(arr)

    def __or__(self, obj):
        arr = []
        for i in range(self.length()):
            if (self[i] != None and obj[i] != None):
                if (self[i] or obj[i]):
                    arr.append(True)
                else:
                    arr.append(False)
            else:
                arr.append(None)

        return RtArrayObject(arr)

    def __lt__(self, obj):
        arr = []
        if (isinstance(obj, RtArrayObject)):
            for i in range(self.length()):
                if (self[i] != None and obj[i] != None and obj[i] != 0):
                    if (self[i] < obj[i]):
                        arr.append(True)
                    else:
                        arr.append(False)
                else:
                    arr.append(None)
        else:
            for i in range(self.length()):
                if (self[i] != None and obj != 0):
                    if (self[i] < obj):
                        arr.append(True)
                    else:
                        arr.append(False)
                else:
                    arr.append(None)
        return RtArrayObject(arr)

    def __le__(self, obj):
        arr = []
        if (isinstance(obj, RtArrayObject)):
            for i in range(self.length()):
                if (self[i] != None and obj[i] != None and obj[i] != 0):
                    if (self[i] <= obj[i]):
                        arr.append(True)
                    else:
                        arr.append(False)
                else:
                    arr.append(None)
        else:
            for i in range(self.length()):
                if (self[i] != None and obj != 0):
                    if (self[i] <= obj):
                        arr.append(True)
                    else:
                        arr.append(False)
                else:
                    arr.append(None)
        return RtArrayObject(arr)

    def __gt__(self, obj):
        arr = []
        if (isinstance(obj, RtArrayObject)):
            for i in range(self.length()):
                if (self[i] != None and obj[i] != None and obj[i] != 0):
                    if (self[i] > obj[i]):
                        arr.append(True)
                    else:
                        arr.append(False)
                else:
                    arr.append(None)
        else:
            for i in range(self.length()):
                if (self[i] != None and obj != 0):
                    if (self[i] > obj):
                        arr.append(True)
                    else:
                        arr.append(False)
                else:
                    arr.append(None)
        return RtArrayObject(arr)

    def __ge__(self, obj):
        arr = []
        if (isinstance(obj, RtArrayObject)):
            for i in range(self.length()):
                if (self[i] != None and obj[i] != None and obj[i] != 0):
                    if (self[i] >= obj[i]):
                        arr.append(True)
                    else:
                        arr.append(False)
                else:
                    arr.append(None)
        else:
            for i in range(self.length()):
                if (self[i] != None and obj != 0):
                    if (self[i] >= obj):
                        arr.append(True)
                    else:
                        arr.append(False)
                else:
                    arr.append(None)
        return RtArrayObject(arr)

    def __eq__(self, obj):
        arr = []
        if (isinstance(obj, RtArrayObject)):
            for i in range(self.length()):
                if (self[i] != None and obj[i] != None and obj[i] != 0):
                    if (self[i] == obj[i]):
                        arr.append(True)
                    else:
                        arr.append(False)
                else:
                    arr.append(None)
        else:
            for i in range(self.length()):
                if (self[i] != None and obj != 0):
                    if (self[i] == obj):
                        arr.append(True)
                    else:
                        arr.append(False)
                else:
                    arr.append(None)
        return RtArrayObject(arr)

    def __ne__(self, obj):
        arr = []
        if (isinstance(obj, RtArrayObject)):
            for i in range(self.length()):
                if (self[i] != None and obj[i] != None and obj[i] != 0):
                    if (self[i] != obj[i]):
                        arr.append(True)
                    else:
                        arr.append(False)
                else:
                    arr.append(None)
        else:
            for i in range(self.length()):
                if (self[i] != None and obj != 0):
                    if (self[i] != obj):
                        arr.append(True)
                    else:
                        arr.append(False)
                else:
                    arr.append(None)
        return RtArrayObject(arr)

    def sum(self, number):
        arr = []
        for i in range(self.length()):
            if (number == 0):
                subIndex = 0
                while subIndex <= i:
                    if (self[i - subIndex] != None):
                        total = total + self[i - subIndex]
                    subIndex = subIndex + 1
                if (total != None):
                    arr.append(total)
                else:
                    arr.append(None)

            elif (i >= number):
                total = 0
                subIndex = 0
                while subIndex <= number:
                    if (self[i - subIndex] != None):
                        total = total + self[i - subIndex]
                    subIndex = subIndex + 1
                if (total != None):
                    arr.append(total)
                else:
                    arr.append(None)
            else:
                arr.append(None)
        return RtArrayObject(arr)

    def count(self, number):
        arr = []
        for i in range(self.length()):
            total = 0
            subIndex = 0

            period = number
            if (i < number):
                period = i

            while subIndex < period:
                if (self[i - subIndex] != None and self[i-subIndex]):
                    total = total + 1
                subIndex = subIndex + 1
            if (total != None):
                arr.append(total)
            else:
                arr.append(None)

        return RtArrayObject(arr)

    #区间最低值
    def LLV(self, number):
        arr = []
        for i in range(self.length()):
            if (i >= number):
                mindata = None
                subIndex = 0
                while subIndex < number:
                    if (self[i - subIndex] != None):
                       if (mindata == None or self[i-subIndex] < mindata):
                           mindata = self[i-subIndex]
                    subIndex = subIndex + 1
                arr.append(mindata)
            else:
                arr.append(None)
        return RtArrayObject(arr)

    #区间最高值
    def HHV(self, number):
        arr = []
        for i in range(self.length()):
            if (i >= number):
                maxdata = None
                subIndex = 0
                while subIndex < number:
                    if (self[i - subIndex] != None):
                        if (maxdata == None or self[i - subIndex] > maxdata):
                            maxdata = self[i - subIndex]
                    subIndex = subIndex + 1
                arr.append(maxdata)
            else:
                arr.append(None)
        return RtArrayObject(arr)


    def abs(self):
        arr = []
        for i in range(self.length()):
            if (self[i] != None):
                arr.append(abs(self[i]))
            else:
                arr.append(None)
        return RtArrayObject(arr)



    # 平均值
    def mean(self):
        sumValue = 0
        sumCount = 0
        for item in self.data:
            sumValue = sumValue + item
            sumCount = sumCount + 1
        return sumValue/sumCount
    #行情差值序列
    def equal_diffrence(self):
        arr = []
        for i in range(self.length()):
            if (i == 0):
                arr.append(0)
            else:
                arr.append(self.data[i] - self.data[i-1])

        return arr
    #行情变化率序列
    def ratio(self):
        arr = []
        for i in range(self.length()):
            if (i == 0):
                arr.append(0)
            else:
                arr.append((self.data[i] - self.data[i-1])/self.data[i-1])
        return arr
    #获取原始数据数组
    def getRawData(self):
        return self.data



    #计算EMA
    def ema(self, count, data = None):
        closeValue = data
        if (data != None and isinstance(data, RtArrayObject)):
            closeValue = data.getRawData()
        if (closeValue == None):
            closeValue = self.data
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
        return RtArrayObject(result)


    # 计算MACD
    def macd(self, fastperiod=12, slowperiod=26, signalperiod=9):

        result = []
        fast_ema = self.ema(fastperiod)
        slow_ema = self.ema(slowperiod)
        DIFF = []
        for i in range(fast_ema.length()):
            if (fast_ema[i] != None) and (slow_ema[i] != None):
                v = fast_ema[i] - slow_ema[i]
            else:
                v = None
            DIFF.append(v)
        DEA = self.ema(signalperiod, DIFF)

        MACD = []
        for i in range(len(DIFF)):
            if (DIFF[i] != None and DEA[i] != None) :
                MACD.append(DIFF[i] - DEA[i])
            else:
                MACD.append(None)
        return  DIFF, DEA, MACD
    #计算MA
    def ma(self, timeperiod, data=None):
        closeValue = data
        if (data != None and isinstance(data, RtArrayObject)):
            closeValue = data.getRawData()
        if (closeValue == None):
            closeValue = self.data
        lastNumber = 0
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

        return RtArrayObject(result)

    #计算SMA 权重MA
    def sma(self, maperiod, weight, data=None):
        closeValue = data
        if (data != None and isinstance(data, RtArrayObject)):
            closeValue = data.getRawData()
        if (closeValue == None):
            closeValue = self.data
        lastNumber = 0
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

        return RtArrayObject(result)

def ARRAY_MAX(*args):
    arr = []

    if (len(args) > 0):
        v0 = args[0]
        for i in range(v0.length()):
            tmp = []
            for j in range(len(args)):
                if (isinstance(args[j], RtArrayObject)):
                    if (args[j][i] != None):
                        tmp.append(args[j][i])
                else:
                    tmp.append(args[j])
            if (len(tmp) > 0):
                arr.append(max(tmp))
            else:
                arr.append(None)

    return RtArrayObject(arr)

def ARRAY_MIN(*args):
    arr = []

    if (len(args) > 0):
        v0 = args[0]
        for i in range(v0.length()):
            tmp = []
            for j in range(len(args)):
                if (args[j][i] != None):
                    tmp.append(args[j][i])
            if (len(tmp) > 0):
                arr.append(min(tmp))
            else:
                arr.append(None)

    return RtArrayObject(arr)

def ARRAY_STD(close, N):
    arr = RtArrayObject();
    MA = close.ma(N)
    for i in range(close.length()):
        if (i>=N):
            sumdif = 0
            total = 0
            for subIndex in range(N):
                if (MA[i - subIndex] == None):
                    continue
                else:
                    dif = close[i - subIndex] - MA[i - subIndex]
                    sumdif = sumdif + dif * dif
                    total = total + 1
            if (total > 0):
                arr.append(math.sqrt(sumdif / total))
            else:
                arr.append(None)
        else:
            arr.append(None)
    return arr

def ARRAY_IF(arr1, v1, v2):
    arr = []
    for i in range(arr1.length()):
        if (arr1[i] != None):
            if (arr1[i]):
                if (isinstance(v1, RtArrayObject)):
                    arr.append(v1[i])
                else:
                    arr.append(v1)
            else:
                if (isinstance(v2, RtArrayObject)):
                    arr.append(v2[i])
                else:
                    arr.append(v2)
        else:
            arr.append(None)
    return RtArrayObject(arr)

def ARRAY_AND(arr1, arr2):
    arr = []
    for i in range(arr1.length()):
        if (arr1[i] != None and arr2[i] != None):
            if (arr1[i] and arr2[i]):
                arr.append(True)
            else:
                arr.append(False)
        else:
            arr.append(None)
    return RtArrayObject(arr)

def ARRAY_OR(arr1, arr2):
    arr = []
    for i in range(arr1.length()):
        if (arr1[i] != None and arr2[i] != None):
            if (arr1[i] or arr2[i]):
                arr.append(True)
            else:
                arr.append(False)
        else:
            arr.append(None)
    return RtArrayObject(arr)



def getHtml(url):
    http = urllib3.PoolManager();
    r = http.request('GET',url)
    print (r.status)
    if (r.status == 200):
        html = r.data
        return html
    return ''

def ARRAY_PLUS(arr1, arr2):
    arr = []
    for i in range(len(arr1)):
        if (arr1[i] != None and arr2[i] != None):
            arr.append(arr1[i] + arr2[i])
        else:
            arr.append(None)
    return arr

def ARRAY_MINUS(arr1, arr2):
    arr = []
    for i in range(len(arr1)):
        if (arr1[i] != None and arr2[i] != None):
            arr.append(arr1[i] - arr2[i])
        else:
            arr.append(None)
    return arr

def ARRAY_MULTIPLY_n(arr1, number):
    arr = []
    for i in range(len(arr1)):
        if (arr1[i] != None):
            arr.append(arr1[i]*number)
        else:
            arr.append(None)
    return arr

def ARRAY_MULTIPY(arr1, arr2):
    arr = []
    for i in range(len(arr1)):
        if (arr1[i] != None and arr2[i] != None):
            arr.append(arr1[i] * arr2[i])
        else:
            arr.append(None)
    return arr

def ARRAY_DIV_n(arr1, number):
    arr = []
    for i in range(len(arr1)):
        if (arr1[i] != None and number != 0):
            arr.append(arr1[i] / number)
        else:
            arr.append(None)
    return arr


def ARRAY_DIV(arr1, arr2):
    arr = []
    for i in range(len(arr1)):
        if (arr1[i] != None and arr2[i] != None):
            arr.append(arr1[i] / arr2[i])
        else:
            arr.append(None)
    return arr

def ARRAY_REF(arr1, period):
    arr = []
    for i in range(arr1.length()):
        if ( (i - period >=0) and (i-period < arr1.length())):
            arr.append(arr1[i-period])
        else:
            arr.append(None)
    return RtArrayObject(arr)

#请求行情数据
def query_history(context, security, endTime, bars, resolution):

    if (context.data == None) :
        context.data = {}
    num = 0

    longTime = time.mktime(time.strptime(endTime,"%Y-%m-%d %H:%M:%S"))*1000
    longTime = int(longTime)
    url = 'http://192.168.1.193:8080/InfoOpSys/market/kline?symbol=' + security + '&time=' \
          + str(longTime) + '&sort=desc&resolution=' + str(resolution) + '&count=' + str(bars)
    html = getHtml(url)
    if (html != ''):
        datas = json.loads(html).get("data")

        if (context.data['open'] == None):
            context.data['open'] = []
        if (context.data['open'] == None):
            context.data['high'] = []
        if (context.data['open'] == None):
            context.data['close'] = []
        if (context.data['open'] == None):
            context.data['low'] = []
        if (context.data['open'] == None):
            context.data['volume'] = []
        if (context.data['open'] == None):
            context.data['amount'] = []
        if (context.data['open'] == None):
            context.data['date'] = []
        for data in datas:
            context.data['open'].insert(0, data.get('open'))
            context.data['date'].insert(0, data.get('date'))
            context.data['high'].insert(0, data.get('high'))
            context.data['low'].insert(0, data.get('low'))

            context.data["close"].insert(0, data.get("close"))

            if (data.get('volume') == None):
                context.data['volume'].insert(0, 0)
            else:
                context.data['volume'].insert(0, data.get('volume'))

            if (data.get('amount') == None):
                context.data['amount'].insert(0, 0)
            else:
                context.data['amount'].insert(0, data.get('amount'))
            num = num + 1

    return num



#请求行情历史数据
def attribute_history(context, bars, fields):
    """
       attribute_history(context, bars, fields)

           行情历史数据获取，历史数据如果满足需求，则

           Inputs:
               context: 上下文数据内容，包含：
                        1、行情代码 security、行情k线数据，
                        单位时间长度, 几天或者几分钟, 现在支持 1：1分钟；2：3分钟；3：5分钟；4：15分钟；5：30分钟；6：1小时；7：2小时；8：4小时；9：1日；10：1周；11：1月
               count: 数量, 返回的结果集的行数
               
               fields: 股票属性的list, 支持SecurityUnitData里面的所有基本属性，包含：[‘open’, ’ close’, ‘low’, ‘high’, ‘volume’]
           Parameters:
               fastperiod: 12
               slowperiod: 26
               signalperiod: 9
           Outputs:
               macd
               macdsignal
               macdhist
       """

    #获取所有行情数据
    if (bars == 0):
        result = {}
        for field in fields:
            result[field] = RtArrayObject()
            result[field].setData(context.data[field])
        return result


    if (context.data == None):
        context.data = {}

    if (context.curIndex - bars < 0):
        difcount = bars - context.curIndex
        endDate = context.data['date'][0]
        num = query_history(context, context.security, endDate, difcount, context.resolution)
        if (num > 0) :
            context.curIndex = context.curIndex + num
            context.baseIndex = context.baseIndex + num
        else:
            bars = 0


    startIndex = context.curIndex - bars
    if (startIndex < 0):
        startIndex = 0
    result = {}
    for field in fields:
        result[field] = RtArrayObject()
        result[field].setData(context.data[field][startIndex:context.curIndex+1])
    return result

def IND_ADX(high, low, close, number):
    t_high = numpy.array(high.getRawData())
    t_low = numpy.array(low.getRawData())
    t_close = numpy.array(close.getRawData())

    adx = talib.ADX(t_high, t_low, t_close, number)

    return adx

# EMA(指数平均数指标) 计算
def IND_EMA(close, count):
    return close.ema(count)
#MACD计算
def IND_MACD(close, fastperiod=12, slowperiod=26, signalperiod=9):
    DIFF = close.ema(fastperiod) - close.ema(slowperiod)
    DEA = DIFF.ema(signalperiod)
    MACD = (DIFF - DEA) * 2
    DIFF.setKey("DIFF")
    DEA.setKey("DEA")
    MACD.setKey("MACD")
    return DIFF, DEA, MACD

#DMA （平均线差指标）
def IND_DMA(close, faseperiod, slowperiod):
    MA_fast = close.ma(faseperiod)
    MA_Slow = close.ma(slowperiod)

    DMA = MA_fast - MA_Slow
    AMA = close.ma(faseperiod, DMA)
    return DMA, AMA


#BIAS指标计算
def IND_BIAS(close, timeperiod):
    BIAS = []
    ema = close.ema(timeperiod)

    BIAS = ((close - ema)*100)/ema

    return BIAS



#OSC(震荡量) 指标
def IND_OSC(close, timeperiod):
    ma = close.ma(timeperiod);
    OSC = ARRAY_MINUS(close.getRawData(), ma)

    return OSC

#MTM 动量指标
def IND_MTM(close, timeperiod, maperiod):
    MTM = close - ARRAY_REF(close, timeperiod)
    MTMMA = close.ma(maperiod, MTM)
    return MTM, MTMMA

#DMI（动向指标）
def IND_DMI(close, high, low, timeperiod, smoothperiod):
    ref_c1 = ARRAY_REF(close, 1)
    TR = (ARRAY_MAX(high-low, (high-ref_c1).abs(), (low - ref_c1).abs())).ma(timeperiod)
    HD = high - ARRAY_REF(high, 1)
    LD = ARRAY_REF(low, 1) - low
    DMP = ARRAY_IF(HD>0, ARRAY_IF(HD>LD, HD, 0), 0).sum(timeperiod)
    DMM = ARRAY_IF(LD>0, ARRAY_IF(LD>HD, LD, 0), 0).sum(timeperiod)

    PDI = DMP*100/TR
    MDI = DMM*100/TR
    ADX = ((MDI-PDI).abs()/(MDI+PDI)*100).ma(smoothperiod)
    ADXR = (ADX + ARRAY_REF(ADX,smoothperiod))/2



    return PDI, MDI, ADX, ADXR


#KDJ 计算
def IND_KDJ(close, high, low, N, M1=3, M2=3):
    K = [];
    D = [];
    J = []
    RSV = (close - low.LLV(N))*100/(high.HHV(N) - low.LLV(N))

    K = RSV.sma(M1, 1)
    D = K.sma(M2, 1)
    J = (K*3) - (D*2)
    return K,D,J

#WMS 指标
def IND_WMS(close, high, low, N):
    WMS = (high.HHV(N) - close)*100/(high.HHV(N) - low.LLV(N))

    return WMS

#TRIX 三重指数平滑平均线
def IND_TRIX(close, timeperiod, smoothperiod):
    tr  = close.ema(timeperiod).ema(timeperiod).ema(timeperiod)
    trref = ARRAY_REF(tr,1)
    TRIX = (tr-trref)*100/trref
    MATRIX = TRIX.ma(smoothperiod)
    return TRIX, MATRIX


#ASI 振动升降指标
def IND_ASI(open, close, high, low, timeperiod):
    LC = ARRAY_REF(close, 1)
    LL = ARRAY_REF(low, 1)
    LO = ARRAY_REF(open, 1)
    AA = (high - LC).abs()
    BB = (low - LC).abs()
    CC = (high - LL).abs()
    DD = (LC - LO).abs()
    R = ARRAY_IF( ARRAY_AND(AA>BB, AA>CC), AA+BB/2+DD/4, ARRAY_IF(ARRAY_AND(BB>CC, BB>AA), BB+AA/2+DD/4, CC+DD/4))
    EE = close - LC
    FF = close - open
    GG = LC - LO

    X = EE + FF/2 +GG
    K = ARRAY_MAX(AA, BB)
    L = 3
    SI = X*K*(50/3)/R
    ASI = SI.ma(timeperiod)
    return ASI

# UD 两天之间收盘价格差计算：isU True计算正价格差； False计算负价格差
def IND_UD(close, timeperiod, isU):
    UD = [];
    for i in range(close.length()):
        if ( i < 1 ):
            UD.append(None)
        else:
            difValue = close[i] - close[i-1]
            if ( (isU and (difValue > 0)) or ( (isU == False) and (difValue < 0) ) ):
                UD.append(difValue)
            else:
                UD.append(0)
    return UD

#RIS计算
def IND_RSI(close, timeperiod):
    lastClose = ARRAY_REF(close, 1)
    RSI = ARRAY_MAX(close - lastClose, 0).sma(timeperiod, 1)*100 / (close-lastClose).abs().sma(timeperiod, 1)

    return  RSI

#BOLL 布林指标
def IND_BOLL(close, period, factor):
    MID = close.ma(period)
    UPPER = MID + ARRAY_STD(close, period) * factor
    LOWER = MID - ARRAY_STD(close, period) * factor
    return MID

#ARBR 情绪指标
def IND_ARBR(open, close, high,low, timeperiod):
    AR = (high-open).sum(timeperiod)*100/(open-low).sum(timeperiod)
    LC = ARRAY_REF(close, 1)
    BR = ARRAY_MAX(high-LC, 0).sum(timeperiod)*100 / ARRAY_MAX(LC-low, 0).sum(timeperiod)
    return AR,BR

#PSY 心理线
def IND_PSY( close, timeperiod, maperiod):
    PSY = (close>ARRAY_REF(close, 1)).count(timeperiod)*100/timeperiod
    PSYMA = close.ma(maperiod, PSY)
    return PSY, PSYMA
#CCI顺势指标
def IND_CCI(close, high, low, timeperiod):
    TP = (high + low + close) / 3
    MA = close.ma(timeperiod)
    MD = (MA - close).abs().ma(timeperiod)
    CCI = (TP - MA)/MD/0.015
    return CCI


#CR量能指标
def IND_CR(close, high, low, timeperiod):
    mid = []
    CR = []
    MID = (close*2 + high + low) / 4
    LM = ARRAY_REF(MID, 1)
    CR = ARRAY_MAX(high-LM, 0).sum(timeperiod) * 100 / ARRAY_MAX(LM - low, 0).sum(timeperiod)
    return CR

#BBI指标
def IND_BBI(close, ma1, ma2, ma3,ma4):
    MA1 = close.ma(ma1)
    MA2 = close.ma(ma2)
    MA3 = close.ma(ma3)
    MA4 = close.ma(ma4)

    BBI = (MA1 + MA2 + MA3 + MA4)/4

    return BBI

#ATR 指标
def IND_ATR(close, high, low, timeperiod):
    LC = ARRAY_REF(close,1)
    TR = ARRAY_MAX( (high-low).abs(), (LC-low).abs(), (LC - high).abs())
    ATR = TR.ma(timeperiod)
    return ATR

#SAR指标
def IND_SAR(open, close, high,low):
    AF = 0.02
    SAR = []
    A_RISE = []
    A_EP = []

    for i in range(close.length()):
        if (i == 0):
            if ( (close.length() > 1) and (close[1] != None) and (open[1] != None) and (low[0] != None) and (high[0] != None) ):
                rise = False
                if (close[1] - open[1] > 0):
                    rise = True
                EP = high[0]
                if (rise):
                    EP = low[0]
                SAR.append(EP)
                A_RISE.append(rise)
                A_EP.append(EP)
            else:
                SAR.append(None)
                A_RISE.append(False)
                A_EP.append(None)
        else:
            if (close[i] != None and open[i] != None and low[i] != None and high[i] != None and SAR[i-1] != None):
                rise = False
                if (close[i] - open[i] > 0):
                    rise = True
                EP = low[i-1]
                if (rise):
                    EP = high[0]
                if (A_RISE[i-1] == rise):
                    if (A_EP[i-1] != None):
                        if (rise):
                            if (EP > A_EP[i-1]):
                                AF = AF + 0.02
                        else:
                            if (EP < A_EP[i - 1]):
                                AF = AF + 0.02
                else:
                    AF = 0.02

                #加速因子AF最高不超过0.2， 当AF>0.2时，AF需重新由0.02起算
                if (AF > 0.2):
                    AF = 0.02

                SAR.append(SAR[i-1] + AF * (EP - SAR[i-1]))
                A_EP.append(EP)
                A_RISE.append(rise)
            else:
                SAR.append(None)
                A_EP.append(None)
                A_RISE.append(False)

    return SAR

#ROC 指标
#算法：
#收盘价减N日前的收盘价，再除以N日前的收盘价，放大100倍，得ROC线；求ROC的M日移动平均，得ROCMA线
#参数：N ，间隔天数；M，计算移动平均的天数。一般取12、6。
#用法：
#1.ROC向下跌破零，卖出信号；ROC向上突破零，买入信号
#2.股价创新高，ROC未配合上升，显示上涨动力减弱
#3.股价创新低，ROC未配合下降，显示下跌动力减弱
#4.股价与ROC从低位同时上升，短期反弹有望
#5.股价与ROC从高位同时下降，警惕回落
def IND_ROC(close, timeperiod, maperiod, emaperiod):
    LCN = ARRAY_REF(close, timeperiod)
    ROC = (close - LCN)*100/LCN

    ROCMA = ROC.ma(maperiod)
    ROCEMA = ROC.ema(emaperiod)

    return ROC, ROCMA, ROCEMA

#CDP 逆市操作指标
def IND_CDP(close, high, low):
    PT = ARRAY_REF(high,1) - ARRAY_REF(low, 1)
    CDP = (high + low + close) / 3
    AH = CDP + PT
    AL = CDP - PT
    NH = CDP * 2 - low
    NL = CDP * 2 - high

    return AH,NH,CDP,NL,AL

#DDI 方向标准离差指数
#.分析DDI柱状线，由红变绿(正变负)，卖出信号；由绿变红，买入信号。
def IND_DDI(high, low, N, N1, M, M1):
    TR = ARRAY_MAX((high-ARRAY_REF(high,1)).abs(), (low - ARRAY_REF(low, 1)).abs())
    DMZ = ARRAY_IF((high+low)<=(ARRAY_REF(high,1) + ARRAY_REF(low, 1)), 0, ARRAY_MAX( (high-ARRAY_REF(high,1)).abs(), (low - ARRAY_REF(low,1)).abs()))
    DMF = ARRAY_IF((high+low)>=(ARRAY_REF(high,1) + ARRAY_REF(low, 1)), 0, ARRAY_MAX( (high-ARRAY_REF(high,1)).abs(), (low - ARRAY_REF(low,1)).abs()))
    DIZ = DMZ.sum(N)/(DMZ.sum(N) + DMF.sum(N))
    DIF = DMF.sum(N)/(DMF.sum(N) + DMZ.sum(N))
    DDI =DIZ - DIF
    ADDI = DDI.sma(N1, M)
    AD = ADDI.ma(M1)

    return DDI.getRawData(), ADDI.getRawData(), AD

#DMA 平均线差
#算法：
#收盘价的短期平均与长期平均的差除以短期天数，得DMA；DMA的M日平均为AMA。
#参数：SHORT 短期天数  LONG 长期天数　M 计算移动平均的天数
#一般为10、50、10
def IND_DMA(close, short, long, M):
    DDD = close.ma(short) - close.ma(long)
    AMA = DDD.ma(M)

#指数平滑移动平均线
#主图叠加指标
#收盘价的P1日、P2日、P3日、P4日指数平滑移动平均线
#一般取5日、10日、20日、60日
def IND_EXPMA(close, p1, p2, p3, p4):
    MA1 = close.ema(p1);
    MA2 = close.ema(p2);
    MA3 = close.ema(p3);
    MA4 = close.ema(p4);
    return MA1,MA2,MA3,MA4

#均线系统
def IND_MID(close, vol):
    M = vol.sum(0)
    MID = ARRAY_IF(M, vol*close.sum(0), close)
    return MID

#移中平均线
def IND_MMV(close, N1):
    MA1 = close.ma(N1)
    MA2 = ARRAY_REF(MA1, -(N1+1)/2)

#量变动速率
#算法：
#成交量减N日前的成交量，再除以N日前的成交量，放大100倍，得VROC线
#参数：N 间隔天数,一般取12
#用法：
#1.VROC向下跌破零，卖出信号；VROC向上突破零，买入信号
#2.股价创新高，VROC未配合上升，显示上涨动力减弱
#3.股价创新低，VROC未配合下降，显示下跌动力减弱
#4.股价与VROC从低位同时上升，短期反弹有望
#5.股价与VROC从高位同时下降，警惕回落
def IND_VROC(vol, N):
    LV = ARRAY_REF(vol, N)
    return ( (vol - LV)*100/LV)

#Price Oscillator
#算法：
#先求收盘价短期(SHORT)均线与长期(LONG)均线的差，再求差值与收盘价短期均线的比，最后将比值乘100。
#参数：
#SHORT、LONG分别为短期、长期平均天数，一般为12、26
def IND_PRICEOSC(close, short, long):
    return (close.ma(short) - close.ma(long))*100/close.ma(short)


#三减六日乖离
#算法：
#B36　收盘价的3日移动平均线与6日均线的差离
#B612 收盘价的6日均线与12日均线的差离
#用法：
#　　乖离值围绕多空平衡点零上下波动，正数达到某个程度无法再往上升时，是卖出时机；反之，是买进时机。
#　　多头走势中，行情回档多半在三减六日乖离达到零附近获得支撑，即使跌破，也很快能够拉回。
def IND_B3612(close):
    B36 = close.ma(3) - close.ma(6)
    B612 = close.ma(6) - close.ma(12)
    return B36, B612

#量相对强弱
#算法：先求
#相对强弱值＝N日内成交量增加幅度总和／减少幅度总和
#VRSI线：100-100/(1+相对强弱值)
#参数：N  统计天数，一般取6
#用法：
#1.VRSI在50以上准确性较高
#2.盘整时，VRSI一底比一底高，多头势强，后市可能续涨；反之，是卖出信号
#3.股价尚在盘整阶段，而VRSI已整理完成，股价将随之突破
def IND_VRSI(vol, N):
    LV = ARRAY_REF(vol, 1);
    VRSI = ARRAY_MAX(vol - LV, 0).sma(N, 1) * 100 / (vol - LV).abs().sma(N, 1)
    return VRSI

#动向速度比率
def IND_SRDM(high, low, N):
    LH = ARRAY_REF(high, 1)
    LL = ARRAY_REF(low, 1)
    cond = ARRAY_MAX((high-LH).abs(), (low - LL).abs())
    DMZ = ARRAY_IF((high-low) <= (LH + LL), 0, cond)
    DMF = ARRAY_IF((high+low)>= (LH + LL), 0, cond)
    ADMZ = DMZ.ma(10)
    ADMF = DMF.ma(10)

    DIFADM = ADMZ - ADMF

    SRDM = ARRAY_IF(ADMZ>ADMF, DIFADM/ADMZ, ARRAY_IF(ADMZ==ADMF, 0, DIFADM/ADMF))
    ASRDM = SRDM.sma(N, 1)

    return SRDM, ASRDM


#随机指标
#算法：对每一交易日求RSV(未成熟随机值)
#RSV=(收盘价－最近N日最低价)/(最近N日最高价－
#     最近N日最低价)×100
#K线：RSV的M1日移动平均   D线：K值的M2日移动平均
#参数：N、M1、M2 天数，一般取9、3、3
#用法：
#1.D>70，超买；D<30，超卖。
#2.线K向上突破线D，买进信号；线K向下跌破线D，卖出信号。
#3.线K与线D的交叉发生在70以上，30以下，才有效。
#4.KD指标不适于发行量小，交易不活跃的股票；
#5.KD指标对大盘和热门大盘股有极高准确性。
def IND_KD(close, high,low, N, M1, M2):
    RSV = (close - low.LLV(N))*100 / (high.HHV(N) - low.LLV(N))
    K = RSV.sma(M1, 1)
    D = K.sma(M2, 1)
    return K,D

#慢速KD
#算法：先求未成熟随机值RSV
#RSV＝(收盘价－N日来最低价)/(N日来最高价－最低价)×100
#FASTK线　RSV的M1日均线
#K线　FASTK的M2日均线
#D线　K线的M3日均线　
#参数：N、M1、M2、M3 天数，一般为9、3、3、5
def IND_SLOWKD(close, high,low, N=9, M1=3, M2=3,M3=5):
    RSV = (close - low.LLV(N)) * 100 / (high.HHV(N) - low.LLV(N))
    FASTK = RSV.sma(M1, 1)
    K = FASTK.sma(M2, 1)
    D = K.sma(M3, 1)

#异同离差乖离率
#公式描述：
#先计算乖离率BIAS，然后计算不同日的乖离率之间的离差，
#最后对离差进行指数移动平滑处理。

#特点：原理和构造方法与乖离率类似，用法也与乖离率相同。
#优点是能够保持指标的紧密同步，而且线条光滑，信号明确，能够有效的过滤掉伪信号。
def IND_DBCD(close, N, M, T):
    MA = close.ma(N)
    BIAS = (close - MA)/MA
    DIF = BIAS - ARRAY_REF(BIAS, M)
    DBCD = DIF.sma(T,1)
    MM = DBCD.ma(5)
    return DBCD, MM

#Detrended Price Oscillator
#算法：收盘价减收盘价的20日均线在11天前的值
def IND_DPO(close):
    return  close - ARRAY_REF(close.ma(20), 11)

#VR容量比率
def IND_VR(close, vol, N):
    LC = ARRAY_REF(close, 1)
    VR = ARRAY_IF(close>LC, vol, 0).sum(N) * 100 / ARRAY_IF(close <= LC, vol, 0).sum(N)
    return VR

#威廉变异离散量
def IND_WVAD(open,close,high,low,vol):
    WVAD = (close - open) * vol / (high - low)
    return WVAD

#Price/Volume Trend
#从上市第一天起，对每一交易日先求收盘价与昨收的差，再求差值与昨收的比，最后求比值与当日成交量的乘积。将每天算得的这个值逐日累加。
def IND_PVT(close, vol):
    LC = ARRAY_REF(close, 1)
    PVT = ((close - LC)/LC*vol).sum(0)
    return PVT

#能量潮
#算法：
#从上市第一天起，逐日累计股票总成交量，若当日收盘价高于昨收，则前OBV加当日成交量为当日OBV，否则减当日成交量为当日OBV。
#用法：
#1.股价上升，OBV线下降，显示买盘无力
#2.股价下跌，OBV线上升，显示买盘旺盛，反弹有望
#3.OBV缓慢上升，显示买盘渐强，买进信号
#4.OBV急速上升，显示买盘力量将尽，卖出信号
#5.OBV线由正转负，为下跌趋势，卖出信号；反之，买进信号
#6.OBV线长用于观察股价何时脱离盘局及突破后的未来走势
def IND_OBV(close, vol):
    LC = ARRAY_REF(close, 1)
    OBV = (ARRAY_IF(close>LC, vol, ARRAY_REF(close<LC, -vol, 0))).sum(0)
    return OBV

#麦克指标
def IND_MIKE(close, high, low, N):
    TYP = (high + low + close) / 3
    LL = low.LLV(N)
    HH = high.HHV(N)
    WR = TYP + (TYP - LL)
    MR = TYP + (HH - LL)
    SR = HH * 2 - LL
    WS = TYP - (HH - TYP)
    MS = TYP - (HH - LL)
    SS = LL * 2 - HH

    return WR,MR,SR,WS,MS,SS

#Envalops
#主图叠加指标
#算法：
#收盘价的N日移动平均向上浮动6 % 得UPPER线，向下浮动6 % 得LOWER线。
#参数：N　设定计算移动平均的天数，一般为14天
def IND_ENV(close, N):
    UPPER = close.ma(N) * 1.06
    LOWER = close.ma(N) * 0.94

#多空布林线
#UPR线为压力线,对股价有压制作用,DWN线为支撑线,对股价具有
#支撑作用,BBI线为中轴线。
#N、P为参数：
#N为统计天数，P为轨道宽度。
#缺损值为10和3
#用法：
#轨道收敛时为买入信号；
#轨道发散，且股价超越上轨时为卖出信号；
#股价跌穿下轨时为卖出信号；
def IND_BBIBOLL(close, N, P):
    BBI = (close.ma(3) + close.ma(6) + close.ma(12) + close.ma(24)) / 4
    UPR = BBI + ARRAY_STD(BBI, N) * P
    DWN = BBI + ARRAY_STD(BBI, N) * P
    return BBI, UPR, DWN

#动态买卖气指标
#该指标在+1到-1之间波动,
#低于-0.5时为很好的买入点,高于+0.5时需注意风险.
def IND_ADTM(open, high, low, N, M):
    LO = ARRAY_REF(open, 1)
    DTM = ARRAY_IF(open <= LO, 0, ARRAY_MAX(high-open, open - LO))
    DBM = ARRAY_IF(open >= LO, 0, ARRAY_MAX(open-low, open-LO))
    STM = DTM.sum(N)
    SBM = DBM.sum(N)
    ADTM = ARRAY_IF(STM>SBM, STM-SBM/STM, ARRAY_IF(STM == SBM, 0 (STM-SBM)/SBM))
    MA1 = ADTM.ma(N)
    return ADTM, MA1






################################################公共运算函数######################################################
#向上交叉于某一个点
def SYS_UPCROSS(v1, v2, crossValue):
    if (v1 == None or v2 == None or crossValue == None):
        return False;
    if (v1 <= crossValue and v2 > crossValue):
        return True
    else:
        return False

#向下交叉于某一个点
def SYS_DOWNCROSS(v1, v2, crossValue):
    if (v1 == None or v2 == None or crossValue == None):
        return False;

    if (v1 >= crossValue and v2 < crossValue):
        return True
    else:
        return False