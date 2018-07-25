import json

import ResultVo as rv


class ResultFactory(object):

    __error_code = '555'

    __error_msg = 'execute failed'

    __success_code = '00000000'

    __success_msg = 'success'

    def __init__(self):
        pass

    @classmethod
    def success(cls,data=[]):
        resultVo = rv.ResultVo(cls.__success_code,cls.__success_msg,data)
        return resultVo

    @classmethod
    def error(cls,data = []):
        return rv.ResultVo(cls.__error_code,cls.__error_msg,data)


vo = ResultFactory.success([1,2,3])
print(json.dumps(vo,default=vo.toJson))