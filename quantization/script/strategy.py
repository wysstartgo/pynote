import tushare as ts
import sys
import numpy as np
import talib
import time
import matplotlib.pyplot as plt
from nose.tools import assert_equals, assert_true, assert_raises
sys.path.append("../common")
import globalvalue as gv
import rtlib
import talib
from talib import func
from talib.test_data import series, assert_np_arrays_equal, assert_np_arrays_not_equal
def init(content):
    k = 1
    m = 20
    content.a = 'yes'
    content.b = 'no'
    print (content)
def handle_indication(content):
    prices = rtlib.attribute_history(content, 0, ['close','high','low','open', 'volume', 'date'])
    content.kdj = rtlib.IND_KDJ(prices['close'], prices['high'], prices['low'], 9)
    content.macd = rtlib.IND_MACD(prices['close'])
    print (content.kdj[0].getRawData())
    print (content.kdj[1].getRawData())
    print (content.kdj[2].getRawData())

    content.doAddOutIndication('K', content.kdj[0].getRawData(), 'LINE', 'red', 'kdj 信息1')
    content.doAddOutIndication('D', content.kdj[1], 'LINE', 'blue', 'kdj 信息2')
    content.doAddOutIndication('J', content.kdj[2], 'LINE', 'yellow', 'kdj 信息3')

    content.macdma = content.macd[2].ma(20)



def handle_bar(content):
    if (content.curIndex <= 5):
        return
    prices = rtlib.attribute_history(content, 1, ['close', 'high', 'low', 'open', 'volume', 'date'])
    current_price = prices['close'][-1]



    #判断kdj交叉点
    if (rtlib.SYS_UPCROSS(content.macdma[content.curIndex - 10], content.macdma[content.curIndex], 0)):
        content.doBuy(current_price, 10000)

    if (rtlib.SYS_DOWNCROSS(content.macdma[content.curIndex - 10], content.macdma[content.curIndex], 0)):
        content.doSell(current_price, 10000)


def handle_bar1(content):
    close_data = rtlib.attribute_history(content, 5, ['close'])
    prices = rtlib.attribute_history(content, 52, ['close','high','low','open'])
    MA5 = close_data['close'].mean()
    current_price = close_data['close'][-1]
    if (current_price > 1.03*MA5):
        content.doSell(current_price, 1000)
    elif current_price < MA5 * 1.01 :
        content.doBuy(current_price, 1000)
    #DMA= rtlib.IND_CR(prices['close'],prices['high'],prices['low'], 14)

    rtlib.IND_WMS(prices['close'], prices['high'], prices['low'], 14)
    #DMA = rtlib.IND_DMA(prices['close'],6, 12)
    BIAS = rtlib.IND_BIAS(prices['close'], 6)

    rtlib.IND_TRIX(prices['close'],12, 20)

    rtlib.IND_PRICEOSC(prices['close'], 5, 10)

    rtlib.IND_MTM(prices['close'], 6, 12)

    kdj = rtlib.IND_KDJ(prices['close'], prices['high'], prices['low'], 9)

    rtlib.IND_DDI(prices['high'], prices['low'], 13, 30, 10, 5)

    rtlib.IND_ASI(prices['open'], prices['close'], prices['high'], prices['low'],12)

    rtlib.IND_RSI(prices['close'], 6)

    rtlib.IND_BOLL(prices['close'], 26, 2)
    rtlib.IND_ARBR(prices['open'], prices['close'], prices['high'], prices['low'], 14)

    rtlib.IND_PSY(prices['close'], 12, 6)

    rtlib.IND_BBI(prices['close'], 3, 6, 12, 24)

    rtlib.IND_CR(prices['close'], prices['high'], prices['low'], 26)

    rtlib.IND_ATR(prices['close'], prices['high'], prices['low'], 12)

    tp = rtlib.IND_PRICEOSC(prices['close'], 12, 26)
    #print (DMA)



