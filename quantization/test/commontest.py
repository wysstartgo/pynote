import numpy as np
import pandas as pd

def ARRAY_REF(arr1, period):
    arr = []
    for i in range(len(arr1)):
        if ( (i - period >=0) and (i-period < len(arr1))):
            arr.append(arr1[i-period])
        else:
            arr.append(None)
    return arr

#
#在股市中，REF代表过去的意思，用法是：REF(X,A),引用A周期前的X值例如：REF(CLOSE,1)表示上一周期的收盘价，在日线上就是昨收。
#REF（c，1） 昨天收盘价
#REF（c，10） 10天前收盘价
#REF（v，8） 8天前成交量
#
def REF(arr1,period):
    #需要切片的长度
    sliceLen = len(arr1) - period
    arr = arr1[:sliceLen]
    for i in range(period):
        arr.insert(i,None)
    return arr

arr1 = [1,2,3,4,5]
print(str(ARRAY_REF(arr1,3)))

print(str(REF(arr1,3)))

#
#求两个数组中相同索引位置上的最大值
#
def MAX(arr1,arr2):
    return np.array([arr1, arr2]).max(axis=0).tolist()

a1 = [1, 4, 9]
a2 = [2, 3, 6]
print('max:' + str(MAX(a1,a2)))

#
#求两个数组相同索引位置上的最小值
#
def MIN(arr1,arr2):
    return np.array([arr1, arr2]).min(axis=0).tolist()

print('min:' + str(MIN(a1,a2)))


def sum(data, number):
    arr = []
    for i in range(len(data)):
        if (number == 0):
            subIndex = 0
            while subIndex <= i:
                if (data[i - subIndex] != None):
                    total = total + data[i - subIndex]
                subIndex = subIndex + 1
            if (total != None):
                arr.append(total)
            else:
                arr.append(None)

        elif (i >= number):
            total = 0
            subIndex = 0
            while subIndex <= number:
                if (data[i - subIndex] != None):
                    total = total + data[i - subIndex]
                subIndex = subIndex + 1
            if (total != None):
                arr.append(total)
            else:
                arr.append(None)
        else:
            arr.append(None)
    return arr

#
# 求window内数据的总和
#
def SUM(arr,window):
    return pd.Series(arr).rolling(window=window,min_periods=window).sum().tolist()

#[0,1,2,3,4,5,6,7,8,9]
ll = [i for i in range(10)]
print(str(sum(ll,5)))

print(str(SUM(ll,5)))

#
#传入的是bool类型的数组
def count(data, number):
    arr = []
    for i in range(len(data)):
        total = 0
        subIndex = 0

        period = number
        if (i < number):
            period = i + 1

        while subIndex < period:
            if (data[i - subIndex] != None and data[i - subIndex]):
                total = total + 1
            subIndex = subIndex + 1
        if (total != None):
            arr.append(total)
        else:
            arr.append(None)

    return arr


se1 = pd.Series([1,4,5,9,7])
se2 = pd.Series([2,3,6,8,0])
print(str(count(se1 > se2,5)))

inArr = [True,False,False,True,True,False]
print(str(count(inArr,2)))
# print('------' + str(np.bool(inArr)))
def checkTrueOrFalse(x):
    if(x):
        return int(1)
    else:
        return int(0)
#
#传入的是布尔类型的数组
#window是时间窗
#
def countBoolInWindow(inArr,window):
    #获取窗口内的为true的总数
    bools = pd.Series(inArr,dtype=np.int32).map(checkTrueOrFalse).rolling(window=window,min_periods=1).sum().tolist()
    return bools

bools = countBoolInWindow(inArr,2)
print(str(bools))


# 区间最低值
def old_LLV(data, number):
    arr = []
    for i in range(len(data)):
        if (i >= number):
            mindata = None
            subIndex = 0
            while subIndex < number:
                if (data[i - subIndex] != None):
                    if (mindata == None or data[i - subIndex] < mindata):
                        mindata = data[i - subIndex]
                subIndex = subIndex + 1
            arr.append(mindata)
        else:
            arr.append(None)
    return arr

#
#区间最低价
def LLV(inArr,window):
    return pd.Series(inArr).rolling(window=window,min_periods=window).min().tolist()

print(str(old_LLV(ll,5)))
print(str(LLV(ll,5)))

#
#区间最高价
def HHV(inArr,window):
    return pd.Series(inArr).rolling(window=window,min_periods=window).max().tolist()

print(str(HHV(ll,5)))

#
#取绝对值
def ABS(inArr):
    return pd.Series(inArr).abs().tolist()

print(str(ABS([-1,2,-3])))

#
#取平均值
def mean(inArr):
    #或者pd.Series([1,2,3]).mean().tolist()
    return np.array(inArr).mean(axis=0).tolist()

print(str(mean([1,2,3])))
print(str(pd.Series([1,2,3]).mean()))

#
# 行情差值序列
#
def equal_diffrence(data):
    # newArr = [data[i] - data[i - 1] for i in range(len(data)) if i > 0]
    # newArr.insert(0,0)
    arr = []
    for i in range(len(data)):
        if (i == 0):
            arr.append(0)
        else:
            arr.append(data[i] - data[i - 1])
    return arr

#行情变化率序列
def ratio(data):
    arr = []
    for i in range(len(data)):
        if (i == 0):
            arr.append(0)
        else:
            arr.append((data[i] - data[i-1])/data[i-1])
    return arr

#
# 练习: DataFrame Apply()
# 注意：为使计算能够正确进行，我们应该在 .std() 函数中将“ddof”参数的值设置为 0。
#
# 注意，计算得出的默认标准偏差类型在 numpy 的 .std() 和 pandas 的 .std() 函数之间是不同的。
# 默认情况下，numpy 计算的是总体标准偏差，ddof = 0。
# 另一方面，pandas 计算的是样本标准偏差，ddof = 1。
# 如果我们知道所有的分数，那么我们就有了总体——因此，要使用 pandas 进行归一化处理，我们需要将“ddof”设置为 0。
#STD为标准差
def STD(closeArr,window):
    return pd.Series(closeArr).rolling(window=window,min_periods=window).std().tolist()

print(str(STD([1,2,3,4,5,6,7,8,9],5)))

#
#第一个数组是一个布尔类型的，v1和v2有一个是数组，有一个是数值
#
def ARRAY_IF(arr1, v1, v2):
    arr = []
    for i in range(len(arr1)):
        if (arr1[i] != None):
            if (arr1[i]):
                if (type(v1) == list):
                    arr.append(v1[i])
                else:
                    arr.append(v1)
            else:
                if (type(v2) == list):
                    arr.append(v2[i])
                else:
                    arr.append(v2)
        else:
            arr.append(None)
    return arr

def ARRAY_AND(arr1, arr2):
    arr = []
    for i in range(len(arr1)):
        if (arr1[i] != None and arr2[i] != None):
            if (arr1[i] and arr2[i]):
                arr.append(True)
            else:
                arr.append(False)
        else:
            arr.append(None)
    return arr

#
#判断arr1和arr2中的值是不是None，如果为None则为False，否则为True
# 然后取得到的两个布尔数组的并集
#
def AND(arr1,arr2):
    return (np.array(arr1) != None) & (np.array(arr2) != None)


res = AND([1,None,2],[None,2,3])
print(str(res))

def ARRAY_OR(arr1, arr2):
    arr = []
    for i in range(len(arr1)):
        if (arr1[i] != None and arr2[i] != None):
            if (arr1[i] or arr2[i]):
                arr.append(True)
            else:
                arr.append(False)
        else:
            arr.append(None)
    return arr

#
#判断arr1和arr2中的值是不是None，如果为None则为False，否则为True
# 然后取得到的两个布尔数组的交集
#
def OR(arr1,arr2):
    return (np.array(arr1) != None) | (np.array(arr2) != None)

#取两个数组的和
def ARRAY_PLUS(arr1, arr2):
    arr = []
    for i in range(len(arr1)):
        if (arr1[i] != None and arr2[i] != None):
            arr.append(arr1[i] + arr2[i])
        else:
            arr.append(None)
    return arr

#
#求两个数组的和
def PLUS(arr1,arr2):
    return np.array(arr1) + np.array(arr2)

arr1 = [1,2,3]
arr2 = [4,5,6]
print(str(ARRAY_PLUS(arr1,arr2)))
print(str(PLUS(arr1,arr2)))

def ARRAY_MINUS(arr1, arr2):
    arr = []
    for i in range(len(arr1)):
        if (arr1[i] != None and arr2[i] != None):
            arr.append(arr1[i] - arr2[i])
        else:
            arr.append(None)
    return arr

#
#取两个数组的差
def MINUS(arr1,arr2):
    return np.array(arr1) - np.array(arr2)

print(str(ARRAY_MINUS(arr1,arr2)))

print(str(MINUS(arr1,arr2)))

def ARRAY_MULTIPLY_n(arr1, number):
    arr = []
    for i in range(len(arr1)):
        if (arr1[i] != None):
            arr.append(arr1[i]*number)
        else:
            arr.append(None)
    return arr

#
#数组中的每个值都乘以n
def MULTIPLY_N(arr1,n):
    return np.array(arr1) * n

print(str(ARRAY_MULTIPLY_n(arr1,2)))
print(str(MULTIPLY_N(arr1,2)))

def ARRAY_MULTIPY(arr1, arr2):
    arr = []
    for i in range(len(arr1)):
        if (arr1[i] != None and arr2[i] != None):
            arr.append(arr1[i] * arr2[i])
        else:
            arr.append(None)
    return arr

#
#两个数组相乘
def MULTIPY(arr1,arr2):
    return np.array(arr1) * np.array(arr2)

print(str(ARRAY_MULTIPY(arr1,arr2)))
print(str(MULTIPY(arr1,arr2)))

def ARRAY_DIV_n(arr1, number):
    arr = []
    for i in range(len(arr1)):
        if (arr1[i] != None and number != 0):
            arr.append(arr1[i] / number)
        else:
            arr.append(None)
    return arr

#
#arr1中的每个元素都除以N
def DIV_N(arr1,N):
    return np.array(arr1) / N

print(str(ARRAY_DIV_n(arr2,2)))
print(DIV_N(arr2,2))

def ARRAY_DIV(arr1, arr2):
    arr = []
    for i in range(len(arr1)):
        if (arr1[i] != None and arr2[i] != None):
            arr.append(arr1[i] / arr2[i])
        else:
            arr.append(None)
    return arr

#
#将两个数组中对应索引位置上的值相除
def DIV(arr1,arr2):
    return np.array(arr1) / np.array(arr2)

print(str(ARRAY_DIV(arr2,arr1)))
print(str(DIV(arr2,arr1)))

#
#closeArr表示传入的收盘价的数组
#window表示计算的天数
#EMA（Exponential Moving Average）是指数平均数指标。也叫EXPMA指标，它也是一种趋向类指标，指数平均数指标是以指数式递减加权的移动平均。
# 计算指数移动平均数
def IND_EMA(closeArr,window):
    return pd.Series(closeArr).ewm(span=window,min_periods=1,adjust=False).mean().tolist()

#
#计算MACD
#MACD称为指数平滑移动平均线，是从双指数移动平均线发展而来的，
# 由快的指数移动平均线（EMA12）减去慢的指数移动平均线（EMA26）得到快线DIF，
# 再用2×（快线DIF-DIF的9日加权移动均线DEA）得到MACD柱。MACD的意义和双移动平均线基本相同，
# 即由快、慢均线的离散、聚合表征当前的多空状态和股价可能的发展变化趋势，但阅读起来更方便。
# 当MACD从负数转向正数，是买的信号。当MACD从正数转向负数，是卖的信号。当MACD以大角度变化，
# 表示快的移动平均线和慢的移动平均线的差距非常迅速的拉开，代表了一个市场大趋势的转变。
#
def IND_MACD(closeArr, fastWindow=12, slowWindow=26, signalWindow=9):
    # 计算fast_ema
    fast_ema = IND_EMA(closeArr, fastWindow)
    # 计算slow_ema
    slow_ema = IND_EMA(closeArr, slowWindow)
    # 计算diff
    series_diff = fast_ema - slow_ema
    # 计算DEA
    series_dea = IND_EMA(series_diff, signalWindow)
    # 计算macd
    series_macd = 2 * (series_diff - series_dea)
    print('----------------' + str(series_macd))
    return series_diff, series_dea, series_macd

#
#https://baike.baidu.com/item/SMA%E5%9D%87%E7%BA%BF/7238642
#https://www.joinquant.com/post/1708
# SMA(X,N,M)，求X的N日移动平均，M为权重。算法：若Y=SMA(X,N,M) 则 Y=(M*X+(N-M)*Y')/N，其中Y'表示上一周期Y值，N必须大于M。
#计算SMA
#
def IND_SMA(vals, window, weight):
    if not isinstance(vals, pd.Series):
        return []
    if(len(vals) > window):
        #取得前面几个的平均数
        previousAverageList = vals[:window].rolling(window=window, min_periods=window).mean().tolist()
        for nextSma in pd.Series(vals)[window:]:
            previousAverageList.append(((window - weight) * previousAverageList[-1] + nextSma * weight) / window)
        return previousAverageList
    else:
        return []

#
# 移动平均线，Moving Average，简称MA，MA是用统计分析的方法，将一定时期内的证券价格（指数）加以平均，
# 并把不同时间的平均值连接起来，形成一根MA，用以观察证券价格变动趋势的一种技术指标。
#  https://baike.baidu.com/item/%E7%A7%BB%E5%8A%A8%E5%B9%B3%E5%9D%87%E7%BA%BF/217887?fr=aladdin
#
def IND_MA(closeArr,window):
    #这里计算的是window日移动平均线
    return pd.Series(closeArr).rolling(window=window, min_periods=window).mean().tolist()

#
#乖离率
#BIAS1 : (CLOSE-MA(CLOSE,L1))/MA(CLOSE,L1)*100;
#BIAS2 : (CLOSE-MA(CLOSE,L2))/MA(CLOSE,L2)*100;
#BIAS3 : (CLOSE-MA(CLOSE,L3))/MA(CLOSE,L3)*100;
#
#
def IND_BIAS(closeArr,window):
    #先计算MA
    EMA = pd.Series(IND_EMA(closeArr,window))
    #根据MA计算BIAS
    BIAS = pd.Series(closeArr).sub(EMA).div(EMA)
    return BIAS

#print(pd.Series([1,2,3]).mul(2))

print(IND_BIAS([1,2,3,4,6,7,8,9,10],5))

#OSC(震荡量) 指标
def IND_OSC(closeArr, window):
    MA = IND_MA(closeArr,window)
    OSC = MINUS(closeArr,MA)
    return OSC

#MTM 动量指标
#A:C-REF(C,N);
#MI:SMA(A,N,1);
# 算法：
# MTM线　　当日收盘价与N日前的收盘价的差
# MTMMA线　对上面的差值求N日移动平均
# 参数：N 间隔天数，也是求移动平均的天数，一般取6
# 用法：
# 1.MTM从下向上突破MTMMA，买入信号
# 2.MTM从上向下跌破MTMMA，卖出信号
# 3.股价续创新高，而MTM未配合上升，意味上涨动力减弱
# 4.股价续创新低，而MTM未配合下降，意味下跌动力减弱
# 5.股价与MTM在低位同步上升，将有反弹行情；反之，从高位同步
# 下降，将有回落走势。
def IND_MTM(closeArr,N,M):
    #MTM = pd.Series(closeArr).sub(pd.Series(REF(closeArr,N)))
    MTM = np.array(closeArr) - np.array(REF(closeArr,N)).tolist()
    MTMMA = IND_MA(MTM,M)
    return MTM, MTMMA

# (标准算法)
# 用法：市场行情趋向明显时，指标效果理想。
# PDI(上升方向线)    MDI(下降方向线)  ADX(趋向平均值)
# 1.PDI线从下向上突破MDI线，显示有新多头进场，为买进信号；
# 2.PDI线从上向下跌破MDI线，显示有新空头进场，为卖出信号；
# 3.ADX值持续高于前一日时，市场行情将维持原趋势；
# 4.ADX值递减，降到20以下，且横向行进时，市场气氛为盘整；
# 5.ADX值从上升倾向转为下降时，表明行情即将反转。
# 参数：N　统计天数； M  间隔天数，一般为14、6
# ADXR线为当日ADX值与M日前的ADX值的均值　　　
# TR := SUM(MAX(MAX(HIGH-LOW,ABS(HIGH-REF(CLOSE,1))),ABS(LOW-REF(CLOSE,1))),N);
# HD := HIGH-REF(HIGH,1);
# LD := REF(LOW,1)-LOW;
# DMP:= SUM(IF(HD>0 AND HD>LD,HD,0),N);
# DMM:= SUM(IF(LD>0 AND LD>HD,LD,0),N);
# PDI: DMP*100/TR;
# MDI: DMM*100/TR;
# ADX: MA(ABS(MDI-PDI)/(MDI+PDI)*100,M);
# ADXR:(ADX+REF(ADX,M))/2
def IND_DMI(closeArr,highArr,lowArr,N,M):
    #构造一个pandas的dataFrame
    pdData = pd.DataFrame({'close':closeArr,'high':highArr,'low':lowArr})
    closeArrRef = REF(closeArr,1)
    pdData['closeRef'] = closeArrRef
    pdData['TR'] = SUM(MAX(MAX(pdData['high'].sub(pdData['low']),ABS(pdData['high'].sub(pdData['closeRef']))),ABS(pdData['low'].sub(pdData['closeRef']))),N)
    pdData['highRef'] = REF(highArr,1)
    HD = pdData['high'] - pdData['highRef']
    pdData['lowRef'] = REF(lowArr,1)
    LD = pdData['lowRef'] - pdData['low']
    pdData['DMP'] = SUM(ARRAY_IF(((HD > 0) & (HD > LD)).tolist(), HD.tolist(), 0), N)
    pdData['DMM'] = SUM(ARRAY_IF(((LD > 0) & (LD > HD)).tolist(),LD.tolist(),0),N)
    pdData['PDI'] = pdData['DMP'] * 100/pdData['TR']
    pdData['MDI'] = pdData['DMM'] * 100/pdData['TR']
    pdData['ADX'] = IND_MA(ABS(pdData['MDI'] - pdData['PDI'])/(pdData['MDI'] + pdData['PDI']) * 100,M)
    pdData['ADXRef'] = REF(pdData['ADX'].tolist(),M)
    pdData['ADXR'] = (pdData['ADX'] + pdData['ADXRef'])/2
    return pdData['PDI'],pdData['MDI'],pdData['ADX'],pdData['ADXR']



a1 = [1,2,3,4,5,6,7,8,9]
a2 = [4,5,6,1,2,3,5,9,0]
a3 = [7,8,9,10,2,20,25,5,9]
a4 = [0,0,0]
bL = [True,False,True]

# ifRes = ARRAY_IF(bL,a1,1)
#
# pdData = pd.DataFrame({'close':a1,'open':a2,'high':a3})
# pdData['www'] = a4
# print(str(pdData))
#
# print(str(MAX(pdData['high'],pdData['open'])))
#
# print(str(pdData['open'] - pdData['close']))
# print(str(pdData['open'].sub(pdData['close'])))
# print(str(pdData['close'] > 0))
# print(str(pdData['close'] * 100 /pdData['open']))

print(str(IND_DMI(a1,a2,a3,2,2)))

print(str(isinstance(a1,list)))

#
# KDJ指标计算
def IND_KDJ(closeArr,highArr,lowArr,N,M1=3,M2=3):
    pdData = pd.DataFrame({'close':closeArr,'high':highArr,'low':lowArr})
    pdData['RSV'] = (pdData['close'] - LLV(pdData['close'],N)) * 100 /(HHV(pdData['high'],N) - LLV(pdData['low'],N))
    pdData['K'] = IND_SMA(pdData['RSV'].tolist(),M1,1)
    pdData['D'] = IND_SMA(pdData['K'].tolist(),M2,1)
    pdData['J'] = (pdData['K'] * 3) - (pdData['J'] * 2)
    return pdData['K'],pdData['D'],pdData['J']