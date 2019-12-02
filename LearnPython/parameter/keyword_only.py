#可变参数
#只能以关键字赋值的形参
def total(initial=5,*numbers,vegetables): #如果我们希望某些关键字形参只能通过关键字实参得到
#def total(initial=5,*,vegetables):        与上一行意义相同                                         #而不是按照实参的位置
                                          #得到，可以将其声明在星号形参后面
    count=initial
    for number in numbers:
        print(number)       #实际numbers 赋予了三个值1,2,3
        count+=initial      #count作为关键字 
    count+=vegetables
    return count
print(total(10,1,2,3,vegetables=50))