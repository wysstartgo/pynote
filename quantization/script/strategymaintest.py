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

class fileItem:
    def __init__(self, version, filename):
        self.version = version
        self.filename = filename

def save_to_file(file_name, contents):
    fh = open(file_name, 'wb+')
    fh.write(contents)
    fh.close()

# 网络获取用户策略代码
def getUserStrategy(content):
    tf = re.match(r'^http?:/{2}\w.+$',content.file)

    fileData = gv.get_value(content.scriptId)
    if (fileData == None or fileData.version != content.version):
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
    else:
        print (fileData.filename)
        return imp.load_source('B', fileData.filename)




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


    def outPutData(self, key, value):
        self._output[key] = value
    def getOutputData(self):
        if (self.sell != None):
            self.outPutData('sell', self.sell)
        if (self.buy != None):
            self.outPutData('buy', self.buy)

        if (self.indication != None):
            self.outPutData('indication', self.indication)
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
    content.startTime = params.get('startTime')
    content.endTime = params.get('endTime')
    content.resolution = params.get('resolution')
    content.count = params.get('count')
    content.version = params.get('version')
    if (content.version == 'null'):
        content.version = 1

    content.scriptId = params.get('scriptId')
    if (content.scriptId == None):
        index = content.file.index('scriptId=') + 9;
        content.scriptId = content.file[index:]
    print (content.scriptId)

    if (content.count == None):
        content.count = 20000


    try:
        print ('I am running')
        workingNode.socket.doWriteLog(content.key, '正在加载执行模块...')
        #B = imp.load_source('B', 'http://127.0.0.1/strategy.py')
        B = getUserStrategy(content)
        import B

        ntime1 = time.time()
        print ('time1:', ntime1 - oldTime)
        B.init(content)
        #url = 'http://192.168.1.183:808/InfoOpSys/market/kline?symbol='+content.security+'&time='+str(content.startTime)+'&endTime='+str(content.endTime)+'&sort=asc&resolution='+str(content.resolution)+'&count=400'
        datas = [];
        loopTime = 3
        while (loopTime > 0):
            loopTime = loopTime - 1
            url = 'http://192.168.1.183:898/InfoOpSys/market/klineByTime?symbol='+content.security+'&startTime='+str(content.startTime)+'&endTime='+str(content.endTime)+'&resolution='+str(content.resolution)
            print (url)
            print (str(loopTime) + ': 请求.....')
            workingNode.socket.doWriteLog(content.key, '正在获取数据...')
            html = getHtml(url)

            workingNode.socket.doWriteLog(content.key, '数据完成...')
            print ('xxxxxxxxxxxxxxxxxxx')
            datas = json.loads(html).get("data")
            if (len(datas) > 0):
                break
            time.sleep(1);
        if (len(datas) <= 0):
            workingNode.socket.doWriteStopError(content.key, '行情数据获取为空...')
            return

        print ('time2:', time.time() - ntime1)
        ntime1 = time.time()

        content.data = {}
        content.data['open'] = [];
        content.data['high'] = [];
        content.data['close'] = [];
        content.data['low'] = [];
        content.data['volume'] = [];
        content.data['amount'] = [];
        content.data['date'] = [];
        #print (datas)
        workingNode.socket.doWriteLog(content.key, '正在解析数据...' + str(len(datas)))
        startTime = datetime.datetime.strptime(datas[0].get('date'), '%Y-%m-%d %H:%M:%S')
        workingNode.socket.doWriteLog(content.key, '获取开始时间...')
        print (startTime)
        print (datas[-1].get('date'))
        endTime = datetime.datetime.strptime(datas[-1].get('date'), '%Y-%m-%d %H:%M:%S')
        workingNode.socket.doWriteLog(content.key, '获取结束时间...')
        print (endTime)
        isReverse = False
        if (endTime < startTime):
            isReverse = True
        print (isReverse)

        for data in datas:
            if not isReverse:
                content.data['open'].append(data.get('open'))
                content.data['date'].append(data.get('date'))
                content.data['high'].append(data.get('high'))
                content.data['low'].append(data.get('low'))

                content.data["close"].append(data.get("close"))

                if (data.get('volume') == None):
                    content.data['volume'].append(0)
                else:
                    content.data['volume'].append(data.get('volume'))

                if (data.get('amount') == None):
                    content.data['amount'].append(0)
                else:
                    content.data['amount'].append(data.get('amount'))
            else:
                content.data['open'].insert(0, data.get('open'))
                content.data['date'].insert(0, data.get('date'))
                content.data['high'].insert(0, data.get('high'))
                content.data['low'].insert(0, data.get('low'))

                content.data["close"].insert(0, data.get("close"))

                if (data.get('volume') == None):
                    content.data['volume'].insert(0, 0)
                else:
                    content.data['volume'].insert(0, data.get('volume'))

                if (data.get('amount') == None):
                    content.data['amount'].insert(0, 0)
                else:
                    content.data['amount'].insert(0, data.get('amount'))

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
