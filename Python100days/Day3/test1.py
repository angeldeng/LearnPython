#输入一个正整数是不是素数

# a=int(input('请输入一个整数'))

# if a%a>1 and a%1>1:
#     print('这个数是素数')
# else:
#     print('这个数不是素数')


from math import sqrt
num=int(input('请输入一个正整数'))
end=int(sqrt(num))
is_prime=True
for x in range(2,end+1):
    if num %x ==0:
        is_prime=False 
        break
if  is_prime and num !=1:
    print('%d是素数'%num)
else:
    print('%d不是素数'%num)

    

