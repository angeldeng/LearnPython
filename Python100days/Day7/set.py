# 集合

set1 = {1, 2, 3, 3, 2, 2}
# 集合会自动去重
print(set1)
print(type(set1))
print('length=', len(set1))

set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 创建集合的推导式语法

# set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
# print(set4)


print(set1 & set2)
print(set1 | set2)
# print(set1 - set2)
print(set1.difference(set2))
print(set1 ^ set2)

#判断子集和超集合
print(set2<set1)
print(set3<set1)
print(set3>=set1)

