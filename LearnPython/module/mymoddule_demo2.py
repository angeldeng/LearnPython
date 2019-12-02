'''注意，如果导入 mymodule 的模块中已经存在同名的__version__，则将发生名字
冲突。
事实上这很可能发生，因为每个模块都用__version__声明它的版本是一种常见的
做法。
因此建议你优先考虑 import 语句，虽然它可能会让你的程序变的更长一些。
你同样可以使用：
from mymodule import *
这将导入模块的所有公有名字，例如 sayhi，但是不会导入__version__因为它以
双下划线开头'''

from mymodule import sayhi,__version__
sayhi()
print('Version',__version__)

'''注意，如果导入 mymodule 的模块中已经存在同名的__version__，则将发生名字
冲突。
事实上这很可能发生，因为每个模块都用__version__声明它的版本是一种常见的
做法。
因此建议你优先考虑 import 语句，虽然它可能会让你的程序变的更长一些。
你同样可以使用：
from mymodule import *
这将导入模块的所有公有名字，例如 sayhi，但是不会导入__version__因为它以
双下划线开头'''
