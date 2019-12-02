def func_other():
    x=2
    print('x is',x)
    def func_inner():
        nonlocal x      #非局部作用域  在函数中的函数里定义变量时,该变量既不是全局也不是局部
        x=5             #必须使用nonlocal定义为非局部变量才可以进行存取
    func_inner()
    print('Changed local x to',x)
func_other()
