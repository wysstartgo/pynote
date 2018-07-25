class ResultVo(object):

    def __init__(self,code,msg,data):
        self.code = code
        self.msg = msg
        self.data = data


    def toJson(self,vo):
        return {
            'code': vo.code,
            'msg': vo.msg,
            'data': vo.data
        }
