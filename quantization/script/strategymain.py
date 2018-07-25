import imp
import datetime
import time
import urllib3
import ssl
import json
import numpy as np
import sys
import numpy
sys.path.append("../common")
import globalvalue as gv

sys.path.append("../common")
import rtlib
import math
import random
import re

def getTimestamp(date):
    timeArray = time.strptime(date, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp*1000

class CMarketData:
    def __init__(self):
        self.startTime = None
        self.endTime = None
        self.realStartTime = None
        self.realEndTime = None
        self.resolution = None
        self.symbol = None
        self.marketDatas = {}
    def getMarketData(self, startTime, endTime):
        pass

    def requestRemoteMarketData(self, symbol, resolution, startTime, endTime):
        #如果请求不到数据，重试三次
        loopTime = 3
        while (loopTime > 0):
            loopTime = loopTime - 1
            url = 'http://qa.rtdream.cn:898/InfoOpSys/market/klineByTime?symbol=' + self.symbol + '&startTime=' + str(
                startTime) + '&endTime=' + str(endTime) + '&resolution=' + str(resolution)
            print (url)
            print (str(loopTime) + ': 请求.....')
            html = getHtml(url)
            print ('xxxxxxxxxxxxxxxxxxx')
            datas = json.loads(html).get("data")
            if (len(datas) > 0):
                break
            time.sleep(1);
        if (len(datas) <= 0):
            return None
        #数据列表的开始时间
        curStartTime = getTimestamp(datas[0].get('date'))
        print (startTime)
        #数据列表的结束时间
        curEndTime = getTimestamp(datas[-1].get('date'))
        print (endTime)
        #返回数据列表的顺序是否反转，即是否是倒序的
        isReverse = False
        if (curEndTime < curStartTime):
            isReverse = True
        print (isReverse)
        marketDatas = {}
        marketDatas['open'] = []
        marketDatas['high'] = []
        marketDatas['close'] = []
        marketDatas['low'] = []
        marketDatas['volume'] = []
        marketDatas['amount'] = []
        marketDatas['date'] = []
        if (isReverse) :
            marketDatas['realStartTime'] = curEndTime
            marketDatas['realEndTime'] = curStartTime
        else:
            marketDatas['realStartTime'] = curStartTime
            marketDatas['realEndTime'] = curEndTime

        for data in datas:
            if not isReverse:
                #如果是正向，则直接放入marketDatas
                marketDatas['open'].append(data.get('open'))
                marketDatas['date'].append(data.get('date'))
                marketDatas['high'].append(data.get('high'))
                marketDatas['low'].append(data.get('low'))

                marketDatas["close"].append(data.get("close"))

                if (data.get('volume') == None):
                    marketDatas['volume'].append(0)
                else:
                    marketDatas['volume'].append(data.get('volume'))

                if (data.get('amount') == None):
                    marketDatas['amount'].append(0)
                else:
                    marketDatas['amount'].append(data.get('amount'))
            else:
                #反着插入
                marketDatas['open'].insert(0, data.get('open'))
                marketDatas['date'].insert(0, data.get('date'))
                marketDatas['high'].insert(0, data.get('high'))
                marketDatas['low'].insert(0, data.get('low'))

                marketDatas["close"].insert(0, data.get("close"))

                if (data.get('volume') == None):
                    marketDatas['volume'].insert(0, 0)
                else:
                    marketDatas['volume'].insert(0, data.get('volume'))

                if (data.get('amount') == None):
                    marketDatas['amount'].insert(0, 0)
                else:
                    marketDatas['amount'].insert(0, data.get('amount'))

        return marketDatas


    def getMarketKey(self, symbol, resolution):
        return symbol + '_' + resolution

    def addData(self, m, key, index,  isBack):
        if (isBack == 1) :
            self.marketDatas[key] = self.marketDatas[key] + m[key][index:]
        else:
            self.marketDatas[key] = m[key][:index] + self.marketDatas[key]


    def addLast(self, marketData):
        incMarketData = marketData
        splitPos = 0
        isBack = 0
        if (marketData['realStartTime'] > self.realEndTime) :
            splitPos = range(marketData['date'])
            # 直接向后添加
            isBack = 1
        elif (marketData['realEndTime'] < self.realStartTime):
            # 直接向前添加
            isBack = 0
            splitPos = 0
        elif (marketData['realStartTime'] < self.marketDatas['realStartTime']
                and marketData['realEndTime'] > self.marketDatas['realEndTime']):
            # 完全覆盖
            self.marketDatas = marketData
            self.realStartTime = marketData['realStartTime']
            self.realEndTime = marketData['realEndTime']
        elif (marketData['realStartTime'] < self.marketDatas['realStartTime']
              and marketData['realEndTime'] > self.marketDatas['realStartTime']):
            #向前部分覆盖
            isBack = 0
            for subIndex in range(len(marketData['date'])):
                curDate = getTimestamp(marketData['date'][subIndex])
                if (curDate >= self.marketDatas['realStartTime']):
                    splitPos = subIndex
                    break
        elif (marketData['realStartTime'] < self.marketDatas['realEndTime']
              and marketData['realEndTime'] > self.marketDatas['realEndTime']):
            #向后部分覆盖
            isBack = 1
            for subIndex in range(len(marketData['date'])):
                curDate = getTimestamp(marketData['date'][subIndex])
                if (curDate > self.marketDatas['realEndTime']):
                    splitPos = subIndex
                    break
        if (incMarketData['date'] != None):
            self.addData(incMarketData, 'open', splitPos, isBack)
            self.addData(incMarketData, 'high', splitPos, isBack)
            self.addData(incMarketData, 'close', splitPos, isBack)
            self.addData(incMarketData, 'low', splitPos, isBack)
            self.addData(incMarketData, 'volume', splitPos, isBack)
            self.addData(incMarketData, 'amount', splitPos, isBack)
            self.addData(incMarketData, 'date', splitPos, isBack)

            if (isBack == 1):
                self.marketDatas['realEndTime'] = incMarketData['realEndTime']
            else:
                self.marketDatas['realStartTime'] = incMarketData['realStartTime']

            self.realStartTime = self.marketDatas['realStartTime']
            self.realEndTime = self.marketDatas['realEndTime']

    def requestMarketData(self, symbol, resolution, startTime, endTime):
        result = {}
        result['open'] = []
        result['high'] = []
        result['close'] = []
        result['low'] = []
        result['volume'] = []
        result['amount'] = []
        result['date'] = []
        if (self.symbol == None):
            self.symbol = symbol
            self.resolution = resolution
            self.startTime = startTime
            self.endTime = endTime
            self.marketDatas = self.requestRemoteMarketData(symbol, resolution, startTime,endTime)
            self.realStartTime = self.marketDatas['realStartTime']
            self.realEndTime = self.marketDatas['realEndTime']

			#暂时注释
            #gv.set_value(self.getMarketKey(self.symbol, self.resolution), self);

        else:
            if (self.symbol == symbol and self.resolution == resolution):
                # 判断请求是否在数据范围内,处理数据交叉重合问题
                # 1 处理请求不在当前时间范围内的情况
                if (startTime >= self.startTime  and endTime <= self.endTime):
                    pass
                else:
                    marketData =  self.requestRemoteMarketData(symbol, resolution, startTime,endTime)
                    self.addLast(marketData)
                    if (startTime < self.startTime):
                        self.startTime = startTime
                    if (endTime > self.endTime):
                        self.endTime = endTime

        #返回 market数据
        startFlag = -1
        endFlag = -1
        for i in range(len(self.marketDatas['date'])):
            curDate = getTimestamp(self.marketDatas['date'][i])
            if (startFlag == -1):
                if (curDate >= startTime):
                    startFlag = i

            if (startFlag != -1):
                if (curDate <= endTime):
                    endFlag = i+1
        #当curDate在startTime和endTime之间时，取startTime和curDate之间的
        if (startFlag != -1 and endFlag != -1):
            result['open'] = self.marketDatas['open'][startFlag : endFlag]
            result['high'] = self.marketDatas['high'][startFlag : endFlag]
            result['close'] = self.marketDatas['close'][startFlag : endFlag]
            result['low'] = self.marketDatas['low'][startFlag : endFlag]
            result['volume'] = self.marketDatas['volume'][startFlag : endFlag]
            result['amount'] = self.marketDatas['amount'][startFlag : endFlag]
            result['date'] = self.marketDatas['date'][startFlag : endFlag]

        return result








class fileItem:
    def __init__(self, version, filename):
        self.version = version
        self.filename = filename

def save_to_file(file_name, contents):
    fh = open(file_name, 'wb+')
    fh.write(contents)
    fh.close()

def getUserStrategyFromMemory(content):
    tf = re.match(r'^http?:/{2}\w.+$',content.file)
    if tf:
        data = getHtml(content.file)
        if(data == None or len(data) < 10):
            return None
        fileName = '../tmp/' + str(random.randint(10, 100))
        fileitem = fileItem(content.version, fileName)
        gv.set_value(content.scriptId, fileitem)
        import utils
        return utils.import_from_string(data,'B')
    else:
        return imp.load_source('B',content.file)

# 网络获取用户策略代码
def getUserStrategy(content):
    tf = re.match(r'^http?:/{2}\w.+$',content.file)

    if tf:
        data = getHtml(content.file)
        # 保存到临时文件
        if (data == None or len(data) < 10):
            return None
        fileName = '../tmp/' + str(random.randint(10, 100))
        save_to_file(fileName, data)
        fileitem = fileItem(content.version, fileName)
        gv.set_value(content.scriptId, fileitem);

        return imp.load_source('B', fileName)
    else:
        return imp.load_source('B', content.file)

    # fileData = gv.get_value(content.scriptId)
    # if (fileData == None or fileData.version != content.version):
    #     if tf:
    #         data = getHtml(content.file)
    #         # 保存到临时文件
    #         if (data == None or len(data) < 10):
    #             return None
    #         fileName = '../tmp/' + str(random.randint(10, 100))
    #         save_to_file(fileName, data)
    #         fileitem = fileItem(content.version, fileName)
    #         gv.set_value(content.scriptId, fileitem);
    #         return imp.load_source('B', fileName)
    #     else:
    #         return imp.load_source('B', content.file)
    # else:
    #     print (fileData.filename)
    #     return imp.load_source('B', fileData.filename)




def getHtml(url):
    http = urllib3.PoolManager();
    r = http.request('GET',url)
    print (r.status)
    html = r.data
    return html
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)
class CQuantMainContent:
    def __init__(self):
        self._output = {}
        self.portfolio = {}
        self.portfolio['cash'] = 100000
        self.portfolio['initCash'] = 100000
        self.portfolio['holding'] = 0;
        self.sell = None
        self.buy = None
        self.plots = None
        self.indication = {}
        self.Info = None
        self.canvasKey = None
        pass
    def doAddOutIndication(self, indName, indData,  indInfo='', style={"lineType":'LINE', "color":'red'}):
        self.indication[indName] = {}
        self.indication[indName]['name'] = indName
        self.indication[indName]['info'] = indInfo
        self.indication[indName]['style'] = style
        if (hasattr(indData, 'getRawData')):
            self.indication[indName]['data'] = indData.getRawData()
        else:
            self.indication[indName]['data'] = indData
    def setCanvas(self, canvaKey):
        self.canvasKey = canvaKey

    def outPutData(self, key, value):
        self._output[key] = value
    def getOutputData(self):
        if (self.sell != None):
            self.outPutData('sell', self.sell)
        if (self.buy != None):
            self.outPutData('buy', self.buy)

        if (self.indication != None):
            self.outPutData('indication', self.indication)

        if (self.canvasKey != None):
            self.outPutData('canvasKey', self.canvasKey)

        if (self.plots != None):
            self.outPutData('plots', self.plots);
        myClassJson = json.dumps(self._output,cls=NumpyEncoder)
        return myClassJson
    def doSell(self, price, value):
        if (self.sell != None):
            sellCount = value;
            if (sellCount > self.portfolio['holding']):
                sellCount = self.portfolio['holding']
            if (sellCount > 0):
                self.sell[self.curIndex-self.baseIndex] = self.sell[self.curIndex-self.baseIndex] + sellCount
                self.portfolio['cash'] = self.portfolio['cash'] + sellCount * price #+ (sellCount * price)*0.001 - 900
                self.portfolio['holding'] = self.portfolio['holding'] - sellCount
    #输出点
    def doPlotShape(self, plotParams):
        if (self.plots == None):
            self.plots = [];
        self.plots.append(plotParams);
        pass

    def doBuy(self, price, value):
        if (self.buy != None):

            buyCount = value;
            if (self.portfolio['cash']/price < 100):
                return
            if (self.portfolio['cash']/price < value):
                buyCount = int(math.floor(self.portfolio['cash']/price)/100)*100
            if (buyCount > 0):
                self.buy[self.curIndex-self.baseIndex] = self.buy[self.curIndex-self.baseIndex] + buyCount
                self.portfolio['cash'] = self.portfolio['cash']  - buyCount * price# - 900
                self.portfolio['holding'] = self.portfolio['holding'] + buyCount

def onStrategyWork(socket, params, workingNode):

    oldTime = time.time()
    print (oldTime)

    content = CQuantMainContent()
    content.key = params.get('key')
    content.file = params.get('file')
    content.security = params.get('symbol')
    content.sort = params.get('sort')
    content.startTime = int(params.get('startTime'))
    content.endTime = int(params.get('endTime'))
    content.resolution = str(params.get('resolution'))
    content.count = params.get('count')
    content.version = params.get('version')
    if (content.version == 'null'):
        content.version = 1

    content.scriptId = params.get('scriptId')
    if (content.scriptId == None):
        if (content.file.index('scriptId=')) :
            index = content.file.index('scriptId=') + 9;
            content.scriptId = content.file[index:]
    print (content.scriptId)

    if (content.count == None):
        content.count = 20000


    try:
        print ('I am running')
        workingNode.socket.doWriteLog(content.key, '正在加载执行模块...')
        #B = imp.load_source('B', 'http://127.0.0.1/strategy.py')
        #B = getUserStrategy(content)
        #import B
        B = getUserStrategyFromMemory(content)

        ntime1 = time.time()
        print ('time1:', ntime1 - oldTime)
        B.init(content)
        print ('time111:', time.time() - ntime1)
        ntime1 = time.time()
        marketData = CMarketData()
        marketData = gv.get_value( marketData.getMarketKey(content.security, content.resolution))
        if (marketData == None):
            marketData = CMarketData()
			
        print ('time2:', time.time() - ntime1)
        ntime1 = time.time()
		
        content.data = marketData.requestMarketData(content.security, content.resolution, content.startTime, content.endTime)


        print (len(marketData.marketDatas['date']))
        print (len(content.data['date']))

        workingNode.socket.doWriteLog(content.key, '数据解析完成...')
        content.buy = [0 for col in range(len(content.data['date']))]
        content.sell = [0 for col in range(len(content.data['date']))]
        content.curIndex = 0
        content.baseIndex = 0

        print ('time3:', time.time() - ntime1)
        ntime1 = time.time()

        content.outPutData("date", content.data['date'])

        workingNode.socket.doWriteLog(content.key, '正在执行数据...')
        #指标计算
        if (hasattr(B, 'handle_indication')):
            #进行指标的计算，并将计算结果
            B.handle_indication(content)

        print ('time4:', time.time() - ntime1)
        ntime1 = time.time()
        while content.curIndex < len(content.data['date']):
            content.portfolio['lastprice'] = content.data['close'][content.curIndex]
            B.handle_bar(content)
            content.curIndex = content.curIndex  + 1
        print ('time5:', time.time() - ntime1)
        ntime1 = time.time()
        workingNode.socket.doWriteLog(content.key, '数据执行完成...')
        outputData = content.getOutputData()
        oData = bytes(outputData, 'GBK')

        workingNode.socket.doWriteData(content.key, oData)
        print ('time6:', time.time() - ntime1)

        newTime = time.time()
        print (newTime)
        print (content.scriptId, newTime - oldTime)
    except:
        info = sys.exc_info()
        try:
            print (str(info[0]) ,":", str(info[1]))
            workingNode.socket.doWriteStopError(content.key, '格式异常：'+str(info[0]) + ':'+ str(info[1]))
        except:
            pass

    finally:
        workingNode.socket.onFinishJob(content.key)
