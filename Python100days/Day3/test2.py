#输入两个正整数，计算它们的最大公约数和最小公倍数

x=int(input('x='))
y=int(input('y='))
#如果x大于y就交换x和y的值
if x>y:
    x,y=y,x#相互赋值

#从两个数中较大的数开始做递减的循环
for factor in range(x,0,-1):
    if x % factor ==0 and y %factor ==0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break

