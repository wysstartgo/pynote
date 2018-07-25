import rtlib;
#初始化内容，用户可以再content中传递自定义属性
def init(content):
    pass

#计算用户自定义指标
def handle_indication(content):
    prices = rtlib.attribute_history(content, 0, ['close','high','low','open', 'volume', 'date'])
    content.kdj = rtlib.IND_KDJ(prices['close'], prices['high'], prices['low'], 9)
    content.macd = rtlib.IND_MACD(prices['close'])
    content.macdma = content.macd[2].ma(20)
    #将指标进行输出
    content.doAddOutIndication('K', content.kdj[0].getRawData(), 'kdj 信息1',{'lineType':'LINE', 'color':'#FF0000'})
    content.doAddOutIndication('D', content.kdj[1],  'kdj 信息2',{'lineType':'LINE', 'color':'#00FF00'})
    content.doAddOutIndication('J', content.kdj[2],  'kdj 信息3',{'lineType':'LINE', 'color':'#0000FF'})

#周期计算
def handle_bar(content):
    if (content.curIndex <= 5):
        return
    prices = rtlib.attribute_history(content, 1, ['close', 'high', 'low', 'open', 'volume', 'date'])
    current_price = prices['close'][-1]

    #判断kdj交叉点
    if (rtlib.SYS_UPCROSS(content.macdma[content.curIndex - 10], content.macdma[content.curIndex], 0)):
        # 输出买点
        content.doBuy(current_price, 10000)

    if (rtlib.SYS_DOWNCROSS(content.macdma[content.curIndex - 10], content.macdma[content.curIndex], 0)):
        # 输出卖点
        content.doSell(current_price, 10000)