from flask import Flask, request

app = Flask(__name__)


@app.route('/',methods=['GET'])
def hello_world():
    test = request.get_data()
    test = request.args.get('test')
    print(str(test))
    return 'Hello World!' + str(test)

#
#执行脚本
@app.route('/executeScript',methods=['GET'])
def execute_Script():
    #http: // 192.168.1.156: 898 / InfoOpSys / market / klineByTime
    marketUrl = 'http://192.168.1.174/Market/market/klineByTime'
    #symbol表示品种代码
    symbol = request.args.get('symbol')
    startTime = request.args.get('startTime')
    endTime = request.args.get('endTime')
    resolution = request.args.get('resolution')

    pass


def getDataFromRemote(symbol=None,startTime=None,endTime=None,resolution=None):
    if(symbol == None | startTime == None | endTime == None | resolution == None):
        return
    # url = marketurl + '?symbol=' + symbol + '&startTime=' + str(
    #     startTime) + '&endTime=' + str(endTime) + '&resolution=' + str(resolution)


if __name__ == '__main__':
    app.run()
