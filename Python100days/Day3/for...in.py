#for 循环实现1-100求和

'''
sum=0
for x in range(1,101):
    sum+=x
print(sum)
'''

#for 循环实现1-100的偶数求和

# sum=0
# for x in range(2,101,2):
#     sum+=x
# print(sum)

#使用分支结构的方式来实现

sum=0
for x in range(1,101):
    if x % 2 ==0:
        sum+=x
print(sum)