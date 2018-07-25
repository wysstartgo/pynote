import threading
import time
import inspect
import ctypes
import globalvalue as gv
class Job(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(Job, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True

    def _async_raise(self,tid, exctype):
        """raises the exception, performs cleanup if needed"""
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")

    def runThread(self):
        self.start()

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self._async_raise(self.ident, SystemExit)

def print_time():
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
        print ('n2:'+gv.get_value('n2'))

if __name__ == "__main__":
    #在这里target指明了线程的入口
    t = Job(target=print_time)
    t.runThread()


    gv.set_value('n1', '112321312');

    print ('n1:'+gv.get_value('n1'))
    gv.set_value('n2', '22222222222');
    i = 0;
    while 1:
        time.sleep(1)
        print ('im working{}',i)
        i = i + 1;
        if (i==3):
            t.stop()
            print("stoped")
        pass