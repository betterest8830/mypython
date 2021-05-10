
import string
import os
import sys

print(string.ascii_lowercase)
print(os.CLD_CONTINUED)
print(sys.path)
# 总的来说，sys.argv[0] 是获得入口执行文件路径，__file__ 是获得任意模块文件的路径。
print(__file__)
print(os.path.abspath(__file__))
print(sys.argv[0])

def get_module_dir(name):
    path = getattr(sys.modules[name], '__file__', None)
    if not path:
        raise AttributeError('module %s has not attribute __file__'%name)
    return os.path.dirname(os.path.abspath(path))

