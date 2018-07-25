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
            if (i >= number):
                total = 0
                subIndex = 0
                while subIndex < number:
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
        if (self.__macd == None or (self.__macd['key'] != str(fastperiod)+'-' + str(slowperiod) + '-' + str(signalperiod))):
            self.__macd = {}
            self.__macd['key'] = str(fastperiod)+'-' + str(slowperiod) + '-' + str(signalperiod)
        else:
            return  self.__macd['DIFF'], self.__macd['DEA'],self.__macd['MACD']

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
        self.__macd['DIFF'] = DIFF
        self.__macd['DEA'] = DEA
        self.__macd['MACD'] = MACD
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
                if (args[j][i] != None):
                    tmp.append(args[j][i])
            if (len(tmp) > 0):
                arr.append(max(tmp))
            else:
                arr.append(None)

    return RtArrayObject(arr)

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
        if (i >= period):
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
    return close.macd(fastperiod, slowperiod, signalperiod)

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
    #for i in range(close.length()) :
    #    if (close[i] != None and ema[i] != None and ema[i] != 0 ) :
    #         BIAS.append( (close[i]-ema[i])*100 / ema[i] )
    #    else:
    #         BIAS.append(None)

    return BIAS

#PRICEOSC 指标
#算法：
#先求收盘价短期(SHORT)均线与长期(LONG)均线的差，再求差值与收盘价短期均线的比，最后将比值乘100。
#参数：
#SHORT、LONG分别为短期、长期平均天数，一般为12、26
def IND_PRICEOSC(close, fastperiod, slowperiod):
    data =close.getRawData()
    fast_ma = close.ma(fastperiod)
    slow_ma = close.ma(slowperiod)

    PRICEOSC = (fast_ma-slow_ma)*100/fast_ma
    return PRICEOSC

#OSC(震荡量) 指标
def IND_OSC(close, timeperiod):
    ma = close.ma(timeperiod);
    OSC = ARRAY_MINUS(close.getRawData(), ma)

    #for i in range(close.length()):
    #    if (i < timeperiod) :
    #        OSC.append(None)
    #    else:
    #        if (ma[i] != None and close[i] != None):
    #            OSC.append(close[i] - ma[i])
    #        else:
    #            OSC.append(None)
    return OSC

#MTM 动量指标
def IND_MTM(close, timeperiod, maperiod):
    MTM = ARRAY_MINUS(close.getRawData(), ARRAY_REF(close, timeperiod))

    #for i in range(close.length()):
    #    if (i < timeperiod):
    #        MTM.append(None)
    #    else:
    #        if (close[i] != None and close[i-timeperiod] != None):
    #            MTM.append(close[i] - close[i-timeperiod])
    #        else:
    #            MTM.append(None)
    MTMMA = close.ma(maperiod, MTM)
    return MTM, MTMMA

#DMI（动向指标）
def IND_DMI(close, high, low, timeperiod, smoothperiod):
    TR1 = (ARRAY_MAX(high-low, (high-ARRAY_REF(close,1)).abs(), (low - ARRAY_REF(close, 1)).abs())).ma(timeperiod)
    HD1 = high - ARRAY_REF(high, 1)
    LD1 = ARRAY_REF(low, 1) - low
    DMP1 = ARRAY_IF(HD1>0, ARRAY_IF(HD1>LD1, HD1, 0), 0).sum(timeperiod)
    DMM1 = ARRAY_IF(LD1>0, ARRAY_IF(LD1>HD1, LD1, 0), 0).sum(timeperiod)

    PDI1 = DMP1*100/TR1
    MDI1 = DMM1*100/TR1
    ADX1 = ((MDI1-PDI1).abs()/(MDI1+PDI1)*100).ma(smoothperiod)
    ADXR1 = (ADX1 + ARRAY_REF(ADX1,smoothperiod))/2


    PDI = []
    MDI = []
    ADX = []
    ADXR = []
    dm_posi = []
    dm_nega = []
    tr = []
    for i in range(close.length()):
        if (i < 1):
            dm_posi.append(None)
            dm_nega.append(None)
            tr.append(None)
        else:
            dm_posi_tmp = high[i] - high[i-1]
            if (dm_posi_tmp > 0):
                dm_posi.append(dm_posi_tmp)
            else:
                dm_posi.append(0)

            dm_nega_tmp = low[i] - low[i-1]
            if (dm_nega_tmp > 0):
                dm_nega.append((dm_nega_tmp))
            else:
                dm_nega.append(0)
            tr_a = abs(high[i] - low[i])
            tr_b = abs(high[i] - close[i-1])
            tr_c = abs(low[i] - close[i-1])
            tr.append(max(tr_a, tr_b, tr_c))


    dm_posi_ma = close.ma(timeperiod, dm_posi)
    dm_nega_ma = close.ma(timeperiod, dm_nega)
    tr_ma = close.ma(timeperiod, tr)
    for i in range(dm_posi_ma.length()):
        if (dm_posi_ma[i] != None and tr_ma[i] != None and tr_ma[i] != 0):
            PDI.append(dm_posi_ma[i]*100/tr_ma[i])
        else:
            PDI.append(None)

    for i in range(dm_nega_ma.length()):
        if (dm_nega_ma[i] != None and tr_ma[i] != None and tr_ma[i] != 0):
            MDI.append(dm_nega_ma[i]*100/tr_ma[i])
        else:
            MDI.append(None)
    dx = []
    for i in range(len(PDI)):
        if (PDI[i] != None and MDI[i] != None and (PDI[i]+MDI[i]) != 0):
            dx.append((PDI[i]-MDI[i])*100/(PDI[i] + MDI[i]))

    ADX = close.ma(smoothperiod, dx)

    for i in range(ADX.length()):
        if ( (i < smoothperiod) or (ADX[i] == None) or (ADX[i-smoothperiod] == None) ):
            ADXR.append(None)
        else:
            ADXR.append( (ADX[i] + ADX[i-smoothperiod]) / 2)
    return PDI, MDI, ADX, ADXR


#RSV(未成熟随机值)
def IND_RSV(close, timeperiod):
    RSV = []
    for i in range(close.length()):
        if (i < timeperiod -1):
            RSV.append(None)
        else:
            data_n = []
            subIndex = i - timeperiod + 1
            Ln = None
            Hn = None
            while (subIndex <= i):
                data_n.append(close[subIndex])
                if (Ln == None):
                    Ln = close[subIndex]
                elif (Ln > close[subIndex]):
                    Ln = close[subIndex]
                if (Hn == None):
                    Hn = close[subIndex]
                elif (Hn < close[subIndex]):
                    Hn = close[subIndex]
                subIndex = subIndex + 1

            if (Ln == Hn):
                RSV.append(0)
            else:
                RSV.append((close[i] - Ln)*100/(Hn - Ln))
    return RSV

#KDJ 计算
def IND_KDJ(close, timeperiod):
    K = [];
    D = [];
    J = []
    RSV = IND_RSV(close, timeperiod)
    for i in range(len(RSV)):
        if (RSV[i] != None):
            if (i > 0 and K[i-1] != None):
                K.append(K[i-1]*2/3 + RSV[i]/3)
            else:
                K.append(50*2/3 + RSV[i]/3)

            if (i > 0 and D[i-1] != None):
                D.append(D[i-1]*2/3 + K[i]/3)
            else:
                D.append(50*2/3 + K[i]/3)

            J.append(3*K[i] - 2*D[i])
        else:
            K.append(None)
            D.append(None)
            J.append(None)

    return K,D,J

#WMS 指标
def IND_WMS(high, low, close, timeperiod):
    WMS = []

    for i in range(close.length()):
        if (i < timeperiod) :
            WMS.append(None)
        else:
            max_high = None
            min_low = None
            for subIndex in range(timeperiod):
                if (high[i-subIndex] != None):
                    if (max_high == None):
                        max_high = high[i - subIndex]
                    elif (max_high < high[i - subIndex]) :
                        max_high = high[i - subIndex]

                if (low[i-subIndex] != None):
                    if (min_low == None):
                        min_low = low[i-subIndex]
                    elif (min_low > low[i - subIndex]):
                        min_low = low[i-subIndex]

            if ( (max_high != None) and (min_low != None) and (close[i] != None) and max_high != min_low) :
                WMS.append( (max_high - close[i])* 100/(max_high - min_low)  )
            else:
                WMS.append(None)
    return WMS

#TRIX 三重指数平滑平均线
def IND_TRIX(close, timeperiod, smoothperiod):
    tr  = IND_EMA(close, timeperiod)
    TRIX = []
    MATRIX = []

    for i in range(tr.length()):
        if ( i < 1):
            TRIX.append(None)
        else:
            if ( (tr[i] != None) and (tr[i-1] != None) and (tr[i-1] != 0) ):
                TRIX.append( (tr[i] - tr[i-1])*100/tr[i-1])
            else:
                TRIX.append(None)
    MATRIX = close.ma(smoothperiod, TRIX)

    return TRIX, MATRIX


#ASI 振动升降指标
def IND_ASI(open, close, high, low, timeperiod):
    si = []
    ASI = []

    for i in range(close.length()):
        if (i < 1):
            si.append(None)
        else:
            if ( (open[i] != None) and (open[i-1] != None) and \
                         (close[i] != None) and (close[i - 1] != None) \
                        (high[i] != None) and (high[i - 1] != None) \
                        (low[i] != None) and (low[i - 1] != None)):
                A = abs(high[i] - close[i-1])
                B = abs(close[i-1] - low[i])
                C = abs(high[i] - low[i-1])
                D = abs(close[i-1] - open[i-1])
                E = abs(close[i] - close[i-1])
                F = abs(close[i] - open[i])
                G = abs(close[i-1] - open[i-1])

                X = E + F/2 + G
                K = max(A, B)
                M = max(A,B,C)
                R = None
                if (M == A):
                    R = A + B/2 + D/4
                elif (M == B):
                    R = B + A/2 + D/4
                else:
                    R = C + D/4
                if (R == 0):
                    si.append(None)
                else:
                    L = 3
                    si.append(50 * X / R * K / L)
            else:
                si.append(None)

    ASI = close.ma(timeperiod, si)
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
    RSI = []

    U = IND_UD(close, timeperiod, True)
    D = IND_UD(close, timeperiod, False)

    ma_u = close.ma(timeperiod, U)
    ma_d = close.ma(timeperiod, D)

    for i in range(len(ma_u)):
        if (ma_u[i] != None and ma_d[i] != None and ma_d[i] != 0 and ((1 + ma_u[i]/ma_d[i]) != 0)):
            RSI.append(100 - 100 / (1 + ma_u[i]/ma_d[i]))

    return  RSI

#BOLL 布林指标
def IND_BOLL(close, period, factor):
    MA = close.ma(period)
    md = []
    for i in range(MA.length()):
        if (i < period):
            md.append(None)
        else:
            sumdif = 0
            total = 0
            for subIndex in range(period):
                if (MA[i-subIndex] == None):
                    continue
                else:
                    dif = close[i-subIndex] - MA[i-subIndex]
                    sumdif = sumdif + dif * dif
                    total = total + 1
            if (total > 0):
                md.append(sumdif/total)
            else:
                md.append(None)
    UP = []
    for i in range(MA.length()):
        if (i < 1):
            UP.append(None)
            continue
        if (MA[i-1] == None or md[i] == None):
            UP.append(None)
            continue
        else:
            UP.append(MA[i-1] + md[i] * factor)

    DN = []
    for i in range(len(md)):
        if (i < 1):
            DN.append(None)
        else:
            if (MA[i-1] != None and md[i] != None):
                DN.append(MA[i-1] - factor * md[i])
            else:
                DN.append(None)

    return MA, UP, DN

#ARBR 情绪指标
def IND_ARBR(open, close, high,low, timeperiod):
    AR = []
    BR = []
    for i in range(close.length()):
        if (i < timeperiod):
            AR.append(None)
            BR.append(None)
        else:
            ar_numerator = 0
            ar_denominator = 0
            br_numerator = 0
            br_denominator = 0
            for subIndex in range(timeperiod):
                ar_numerator = ar_numerator + high[i-subIndex] - open[i-subIndex]
                ar_denominator = ar_denominator + open[i-subIndex] - low[i-subIndex]
                if (i-subIndex-1>=0):
                    br_numerator = br_numerator + high[i-subIndex] - close[i-subIndex-1]
                    br_denominator = br_denominator + close[i-subIndex-1] - low[i-subIndex]
            if (ar_denominator != 0):
                AR.append(ar_numerator*100/ar_denominator)
            else:
                AR.append(None)
            if (br_denominator !=0):
                BR.append(br_numerator*100/br_denominator)
            else:
                BR.append(None)

    return AR,BR

#PSY 心理线
def IND_PSY(open, close, timeperiod, maperiod):
    PSY = []

    for i in range(close.length()):
        if (i < timeperiod):
            PSY.append(None)
        else:
            sumvalue = 0
            total = 0
            for subIndex in range(timeperiod):
                if (close[i-subIndex] != None and open[i-subIndex] != None):
                    if ( (close[i-subIndex] - open[i-subIndex]) > 0):
                        sumvalue = sumvalue + 1
                    total = total + 1
            if (total > 0):
                PSY.append(sumvalue*100/total)
            else:
                PSY.append(None)

    PSYMA = close.ma(maperiod, PSY)
    return PSY, PSYMA
#CCI顺势指标
def IND_CCI(close, high, low, timeperiod):
    ma = close.ma(timeperiod)
    md = []
    tp = []
    for i in range(close.length()):
        if (high[i] != None and close[i] != None and low[i] != None):
            tp.append( (high[i] + low[i] + close[i])/3)
        else:
            tp.append(None)

        if (i < timeperiod):
            md.append(None)
        else:
            sumValue = 0
            total = 0
            for subIndex in range(timeperiod):
                if (ma[i-subIndex] != None and close[i-subIndex] != None):
                    sumValue =sumValue + abs(ma[i-subIndex] - close[i-subIndex])
                    total = total + 1
            if (total > 0):
                md.append(sumValue/total)
            else:
                md.append(None)

    CCI = []
    for i in range(ma.length()):
        if (tp[i] != None and ma[i] != None and md[i] != None and md[i] > 0):
            CCI.append((tp[i] - ma[i])/md[i]/0.015)
        else:
            CCI.append(None)
    return CCI

#CR量能指标
def IND_CR(close, high, low, timeperiod):
    mid = []
    CR = []

    for i in range(close.length()):
        if (close[i] != None and high[i] != None and low[i] != None):
            mid.append( (close[i]*2 + high[i] + low[i])/4)
        else:
            mid.append(None)

    for i in range(close.length()):
        if (i < timeperiod):
            CR.append(None)
        else:
            sum_p1 = 0
            sum_p2 = 0
            for subIndex in range(timeperiod):
                if (high[i-subIndex] != None \
                    and (i-subIndex-1) >= 0 \
                    and mid[i-subIndex-1] != None\
                    and low[i-subIndex] != None):
                    sum_p1 = sum_p1 + high[i-subIndex] - mid[i-subIndex-1]
                    sum_p2 = sum_p2 + mid[i-subIndex-1] - low[i-subIndex]

            if (sum_p2 != 0):
                CR.append(sum_p1*100/sum_p2)
            else:
                CR.append(None)

    return CR

#BBI指标
def IND_BBI(close, ma1, ma2, ma3,ma4):
    MA1 = close.ma(ma1)
    MA2 = close.ma(ma2)
    MA3 = close.ma(ma3)
    MA4 = close.ma(ma4)

    BBI = []
    for i in range(close.length()):
        if ( (MA1[i] != None) and (MA2[i] != None) and (MA3[i] != None) and (MA4[i] != None)):
            BBI.append( (MA1[i]+MA2[i]+MA3[i]+MA4[i])/4 )
        else:
            BBI.append(None)


    return BBI

#ATR 指标
def IND_ATR(close, high, low, timeperiod):
    tr = []
    for i in range(close.length()):
        if (i < 1):
            tr.append(None)
        else:
            if (close[i] != None and high[i] != None and low[i] != None and close[i-1] != None):
                tr1 = high[i] - low[i]
                tr2 = close[i-1] - low[i]
                tr3 = high[i] = close[i-1]
                tr.append(max(tr1,tr2,tr3))
            else:
                tr.append(None)
    ATR = close.ma(timeperiod, tr)
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
def IND_ROC(close, timeperiod, maperiod, emaperiod):
    ROC = []
    ROCMA = []
    ROCEMA = []

    for i in range(close.length()):
        if ( i < timeperiod):
            ROC.append(None)
        else:
            if (close[i] != None and close[i-timeperiod] != None and close[i-timeperiod] != 0):
                ROC.append( (close[i] - close[i-timeperiod])*100/close[i-timeperiod] )
            else:
                ROC.append(None)

    ROCMA = close.ma(maperiod, ROC)
    ROCEMA = close.ema(emaperiod, ROC)

    return ROC, ROCMA, ROCEMA

#CDP 逆市操作指标
def IND_CDP(close, high, low):
    CDP = []
    for i in range(close.length()):
        if (i < 1):
            CDP.append(None)
        else:
            last = i - 1
            if (high[last] != None and low[last] != None and close[last] != None):
                CDP.append((high[last] + low[last] + close[last] * 2) / 4)
            else:
                CDP.append(None)
    AH = []
    for i in range(len(CDP)):
        if (i<1):
            AH.append(None)
        else:
            last = i - 1
            if (high[last] != None and low[last] != None and CDP[last] != None):
                AH.append(CDP[last] + high[last] - low[last])
            else:
                AH.append(None)
    AL = []
    for i in range(len(CDP)):
        if (i < 1):
            AL.append(None)
        else:
            last = i - 1
            if (high[last] != None and low[last] != None and CDP[last] != None):
                AL.append(CDP[last] - (high[last] - low[last]))
            else:
                AL.append(None)
    NH = []
    for i in range(len(CDP)):
        if (i < 1):
            NH.append(None)
        else:
            last = i - 1
            if (low[last] != None and CDP[last] != None):
                NH.append(CDP[last] * 2  - low[last])
            else:
                NH.append(None)
    NL = []
    for i in range(len(CDP)):
        if (i < 1):
            NL.append(None)
        else:
            last = i - 1
            if (high[last] != None and CDP[last] != None):
                NL.append(CDP[last] * 2  - high[last])
            else:
                NL.append(None)

    return AH,NH,CDP,NL,AL

#DDI 方向标准离差指数
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
def IND_DMA(close, short, long):
    DDD = close.ma(short)


