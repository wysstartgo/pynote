import time
import numpy

#自定义数据结构
class RtArrayObject:
    def __init__(self, value=[]):
        self.data = value
    def __getitem__(self, key):
        return self.data[key]

    def __get__(self):
        return self.data

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
            if ( i < number):
                arr.append(None)
            else:
                arr.append(self[i-numpy])

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

    #获取原始数据数组
    def getRawData(self):
        return self.data

def ARRAY_MAX(**args):
    arr = []

    if (len(args) > 0):
        v0 = args[0]
        for i in range(len(v0)):
            tmp = []
            for j in range(len(args)):
                tmp.append(args[j][i])
            arr.append(max(tmp))

    return RtArrayObject(arr)


print (time.time())
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

str = '" 2 2 " b 2'
print (str.replace('"', '\\"'))

arr1 = [1,2,3,4,5]
arr2 = [1,2,3,4,6]
arr3 = [3,5,6,7,8]

print (max(arr1))


arx = ARRAY_MAX({'key1':arr1,'key2':arr2,'key3':arr3})
a1 = RtArrayObject(arr1)
a2 = RtArrayObject(arr2)

a3 = a1 + a2

print (a3.getRawData())

a4= a3+100

print (a4.getRawData())
