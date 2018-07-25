import json
import NumpyEncoder
import math

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