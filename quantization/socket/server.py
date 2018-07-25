import threading
import socketserver as SocketServer
import sys
import json

sys.path.append("../common")
from rtthread import Job
import globalvalue as gv

sys.path.append("../script")
import strategymain

import time
users = []

class CWorkingNode:
    def __init__(self):
        pass


PKG_TYPE_CONNECT = b'(*&CONNECT&*)'
PKG_TYPE_DATA = b'(*&DATA&*)'
PKG_TYPE_STOP_JOB = b'(*&STOPJOB&*)'
PKG_TYPE_FINISH_JOB = b'(*&FINISH&*)'
PKG_TYPE_LOG = b'(*&LOG&*)'
PKG_TYPE_STOPERROR = b'(*&STOPERROR&*)'


def print_a():
    print ('a')

def print_b():
    print ('b')
def getData(data):
    refData = ''
    if (data != None):
        startIndex = data.find('(*-', 0);
        endIndex = data.find('-*)', 0);
        if (startIndex == -1 or endIndex == -1):
            print ('参数内容格式错误！！')
        else:
            refData = data[startIndex+3:endIndex]
    return refData





def onStartingStrategy(socket, workParams, workingNode):
    strategymain.onStrategyWork(socket, workParams, workingNode)

def onReceiveWork(socket, params):
    params = params.decode("utf-8"); #解码
    params = getData(params);#去除头尾
    workParams = json.loads(params) #转为JSON
    print (workParams)
    if (workParams.get('type')):
        key = workParams.get('key')
        if (key != None and key != ''):

            if (gv.get_value('work-'+key) != None):
                print ('I am bussy.....')
                return
            clientKey = str(socket.client_address[0])+"-"+str(socket.client_address[1])
            arr = gv.get_value(clientKey)
            if (arr == None):
                arr = []
            arr.append(key)
            gv.set_value(clientKey, arr)


            workingNode = CWorkingNode()
            workingNode.socket = socket
            job = Job(target=onStartingStrategy, args=(socket, workParams, workingNode,))
            workingNode.job = job


            gv.set_value('work-'+key, workingNode)
            job.runThread();
            print ('my new work is starting......', workParams.get('key'))
    else:
        print ('start new work failed......', workParams.get('key'))



   # strBt = json.dumps(workParams) #json转字符串
   # datas = strBt
   # try:
   # datas = datas.decode('unicode_escape') #解码
   # datas = datas.encode(encoding='GBK')#GBK编码二进制
   # socket.wfile.write(datas)#输出二进制


def print_time(socket):
    while 2:
        print(111111111111)
        print(222222222222)
        print(333333333333)
        print(444444444444)
        print(555555555555)
        print(666666666666)
        time.sleep(1)
        print(777777777777777777)
        print(8888888888888888888)
        print(99999999999999999999999999)
        time.sleep(1)
        socket.wfile.write(b"keep aline\n")


class MyTCPHandler(SocketServer.StreamRequestHandler):
    #完成任务工作，将任务从任务列表中移除
    def onFinishJob(self, key):
        self.doFinishJob(key)
        workingNode = gv.get_value('work-' + key)
        if (workingNode != None):
            print ('I am finishing....:' + key)
            gv.remove_key('work-' + key)
            clientKey = str(workingNode.socket.client_address[0]) + "-" + str(workingNode.socket.client_address[1])
            arr = gv.get_value(clientKey)
            if (arr != None):
                for i in range(len(arr)):
                    if (arr[i] == key):
                        del arr[i]
                        gv.set_value(clientKey, arr)
                        return
    #停止任务，结束任务线程
    def doStopJob(self, key):
        workingNode = gv.get_value('work-' + key)
        if (workingNode != None):
            print('I am stoping....:' + key)
            gv.remove_key('work-' + key)
            clientKey = str(workingNode.socket.client_address[0]) + "-" + str(workingNode.socket.client_address[1])
            arr = gv.get_value(clientKey)
            workingNode.job.stop()
            if (arr != None):
                for i in range(len(arr)):
                    if (arr[i] == key):
                        del arr[i]
                        gv.set_value(clientKey, arr)
                        return

    #关闭客户端
    def closeClient(self):
        clientKey = str(self.client_address[0]) + "-" + str(self.client_address[1]);
        arr = gv.get_value(clientKey)
        if (arr != None):
            for i in range(len(arr)):
                workingNode = gv.get_value('work-' + arr[i])
                if (workingNode != None):
                    gv.remove_key('work-' + arr[i])
                pass
            gv.remove_value(clientKey)
        pass


    #接收关闭工作
    def onReceiveStopJob(self, params):
        params = params.decode("utf-8");  # 解码
        params = getData(params);  # 去除头尾
        workParams = json.loads(params)  # 转为JSON
        if (workParams.get('Type')):
            key = workParams.get('key')
            if (key != None and key != ''):
                self.doStopJob(key)


    # 关闭任务会话
    def doStopJobToken(self, key):
        workingNode = gv.get_value('work-' + key)
        if (workingNode != None):
            if (workingNode.socket):
                date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());
                writeData = PKG_TYPE_STOP_JOB+b'(*-{key:"' + bytes(key, 'utf-8') + b'",value:{date:"'+bytes(date, 'utf-8')+ b'"}}-*)\n'
                workingNode.socket.wfile.write(writeData)

    #完成任务
    def doFinishJob(self, key):
        workingNode = gv.get_value('work-' + key)
        if (workingNode != None):
            if (workingNode.socket):
                date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());
                writeData = PKG_TYPE_FINISH_JOB + b'(*-{key:"' + bytes(key, 'utf-8') + b'",value:{date:"'+bytes(date, 'utf-8')+ b'"}}-*)\n'
                workingNode.socket.wfile.write(writeData)


    # 发送数据
    def doWriteData(self, key, data):
        workingNode = gv.get_value('work-' + key)
        if (workingNode != None):
            if (workingNode.socket):
                date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());
                writeData = PKG_TYPE_DATA +  b'(*-{key:"'+bytes(key,'utf-8')+b'",value:{date:"'+bytes(date, 'utf-8')+ b'",data:' + data + b'}}-*)\n'
                workingNode.socket.wfile.write(writeData)

    # 发送日志
    def doWriteLog(self, key, log):
        workingNode = gv.get_value('work-' + key)
        if (workingNode != None):
            if (workingNode.socket):
                log = log.replace('"', '\\"')
                data = bytes(log, 'utf-8')
                logTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());
                writeData = PKG_TYPE_LOG + b'(*-{key:"' + bytes(key, 'utf-8') \
                            + b'",value:{date:"'+ bytes(logTime, 'utf-8')+b'",data:"' + data + b'"}}-*)\n'
                workingNode.socket.wfile.write(writeData)
    def doWriteStopError(self, key, errorInfo):
        workingNode = gv.get_value('work-' + key)
        if (workingNode != None):
            if (workingNode.socket):
                errorInfo = errorInfo.replace('"', '\\"')
                data = bytes(errorInfo, 'utf-8')
                errTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());
                writeData = PKG_TYPE_STOPERROR + b'(*-{key:"' + bytes(key, 'utf-8') + b'",value:{date:"'+ bytes(errTime, 'utf-8')+b'",data:"' + data + b'"}}-*)\n'
                workingNode.socket.wfile.write(writeData)

    def handle(self):
        username = None
        print ('a new connection:')
        while True:
            self.data = self.rfile.readline().strip()
            cur_thread = threading.currentThread()
            print ("RECV from ", self.client_address[0])
            cmd = self.data
            if cmd == None or len(cmd) == 0:
                break;
            print (cmd)
            # business logic here
            try:
                if (cmd.startswith(PKG_TYPE_CONNECT)):
                    result = cmd[len(PKG_TYPE_CONNECT):]
                    params = cmd[len(PKG_TYPE_CONNECT):]
                    onReceiveWork(self, params)
                elif (cmd.startswith(PKG_TYPE_STOP_JOB)):
                    params = cmd[len(PKG_TYPE_STOP_JOB):]
                    self.onReceiveStopJob(params)

                elif cmd.startswith(b'echo'):
                    result = cmd[4:]
                    if (result == b'a'):
                        print_a()
                        gv.get_value(result)()
                    if (result == b'b'):
                        print_b()
                elif cmd.startswith(b'login'):
                    username = cmd[4:]
                    users.append({username:self.wfile})
                    result = username + ' logined.'
                elif cmd == b'quit':

                    break
                else:
                    result = 'error cmd'
                #self.wfile.write(result)
            except:
                print ('error')
        try:
            if username != None:
                users.remove(username)
        except:
            pass
        print (username, ' closed.')
        self.closeClient()
        self.connection.close()


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    print ('new connection')
    pass

if __name__ == "__main__":
    HOST, PORT = "192.168.1.208", 9998
    gv._init()

    server = ThreadedTCPServer((HOST, PORT), MyTCPHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()
    server.serve_forever()