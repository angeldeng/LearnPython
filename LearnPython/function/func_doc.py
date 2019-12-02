#文档字符串,通常被称为docstrings
#文档字符串是一个你应该利用的重要的工具，因为它帮助你更好的注释程序使得
#程序更易于理解。
#更神奇的是你甚至可以在程序运行时取得文档字符串！
def printMax(x,y):
    '''Prints the maximum of two numbers.
    The two values must be integers.'''
    x=int(x)    #convert to integers,if possible
    y=int(y)
    if x>y:
        print(x,'is maximum')
    else:
        print(y,'is maximum')
printMax(3,5)
print(printMax.__doc__)

'''一个函数的第一个逻辑行的字符串将成为这个函数的文档字符串。
注意类和模块同样拥有文档字符串，在后面相应的章节我们会学到它们。
根据惯例，文档字符串是一个多行字符串，其中第一行以大写字母开头，并以句
号结尾。
接下来的第二行为空行，从第三行开始为详细的描述。
我强烈建议你在你的正规函数中遵循这个编写文档字符串的惯例。
我们可以通过使用函数的__doc__属性(注意双下划线)存取 printMax 的文档字符
串。
记住 python 中的一切都是对象，其中也包括函数。在后面的类一章我们会学到
更多。
如果你在 python 使用过 help()，其实你已经看到过文档字符串的应用了！
help()只是取出函数的__doc__属性，然后以一种整洁的方式显示给你。'''