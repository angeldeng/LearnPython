'''现在你已经知道通过定义函数可以在你的程序中复用代码。但当你想在你编写的
其他程序中复用大量函数怎么办呢？
也许你可以猜到了，办法就是利用模块。
有各种编写模块的方式，但最简单的方式是创建一个以.py 为后缀的文件并包含
所需的函数与变量。
另一种方式是以编写 python 解释器的本地语言编写模块。
例如 C 语言编写的模块被编译后可供运行于标准 python 解释器上的 python 代码
使用。
模块可以被其它程序导入以使用其提供的功能。这也是为什么我们可以使用
python 标准库。
我们先来看看如何使用标准库模块'''

import sys
print('The command line arguments are')
for i in sys.argv:
    print (i)
print('\n\nThePYTHONPATHis',sys.path,'\n')

'''工作流程：
首先我们使用 import 语句导入 sys 模块。本质上这告诉 python 我们希望使用这
个模块。
sys 模块包含 python 解释器与其工作环境(即系统)相关的功能。
当 python 执行 import sys 语句时，它将查找 sys 模块。本例中 sys 是内建模块之
一，因此 python 知道在哪能找到它。
如果导入的不是一个编译模块，即不是用 python 编写的模块，python 解释器会
在变量 sys.path 中列出的目录中查找它'''