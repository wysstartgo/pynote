def _init():
    global _global_datas
    _global_datas = {}

def set_value(name, value):
    _global_datas[name] = value

def remove_value(name):
    del _global_datas[name]

def get_value(name, defValue = None):
    try:
        return _global_datas[name]
    except KeyError:
        return defValue;
def remove_key(key):
    try:
        del _global_datas[key]
    except:
        pass