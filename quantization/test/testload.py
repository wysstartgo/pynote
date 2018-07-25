import imp
import sys

class StringImporter(object):

   def __init__(self, modules):
       self._modules = dict(modules)


   def find_module(self, fullname, path):
      if fullname in self._modules.keys():
         return self
      return None

   def load_module(self, fullname):
       if not fullname in self._modules.keys():
           raise ImportError(fullname)

       new_module = imp.new_module(fullname)
       module = self._modules[fullname]
       print('===============================')
       print(new_module.__dict__)
       print('===============================')
       # exec module in new_module.__dict__
       exec(module)
       # if module in new_module.__dict__:
       #     print('=======================')
       return new_module

if __name__ == '__main__':
    fileName = '../tmp/100'
    # B = imp.load_source('B',fileName)
    # import B
    # B.testPrint()
    with open(fileName,mode = 'r',encoding='utf-8') as f:
        content = f.read()

    modules = {}
    modules['B'] = content
    # print(content)
    sys.meta_path.append(StringImporter(modules))

    import B
    B.testPrint()


    # otherFileName = '../tmp/82'
    # C = imp.load_compiled('C',otherFileName)
    # import C
    # C.printC()
