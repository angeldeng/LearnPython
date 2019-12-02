# f=[x for x in range(1,10)]
# print(f)
# f=[x+y for x in 'ABCDE'for y in'1234567']
# print(f)
# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪
# 所以需要耗费较多的内存空间

# f=[x**2 for x in range (1,1000)]
# print(sys.getsizeof(f))
# print(f)

# y=[1,2,5,78]
# for x in y:
#     print(x)

# 请注意下面的代码创建的不是一个列表而是一个生成器对象
# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)

# f = (x ** 2 for x in range(1, 1000))
# # print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
# print(f)
# for val in f:
#     print(val)

# 除了上面提到的生成器语法，
# Python中还有另外一种定义生成器的方式，
# 就是通过yield关键字将一个普通函数改造成生成器函数。
# 下面的代码演示了如何实现一个生成斐波拉切数列的生成器,
# 所谓斐波拉切数列可以通过下面递归的方法来进行定义：
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()





