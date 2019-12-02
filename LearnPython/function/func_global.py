x=50
def func(x):
    global x    #定义变量为全局变量
    print('x is',x)
    x=2     #此时变量x被定义(函数内必须没有同名变量)
    print('Change local x to',x)
func(x)
print('x is still',x)   #全局变量

#并不鼓励这种方法,应该尽量避免,会让代码读者难以弄清变量到底定义在哪里?