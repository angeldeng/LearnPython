x=50
def func(x):
    print('x is',x)
    x=2     #局部变量
    print('Change local x to',x)
func(x)
print('x is still',x)   #全局变量
