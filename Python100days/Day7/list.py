#[]定义列表，多个元素用，分隔，可以使用for循环进行遍历也可以使用[],[:]运算符取出列表中的一个或者多个元素


# list1 = [1, 3, 5, 7, 100]
# print(list1) # [1, 3, 5, 7, 100]
# # 乘号表示列表元素的重复
# list2 = ['hello'] * 3
# print(list2) # ['hello', 'hello', 'hello']
# # 计算列表长度(元素个数)
# print(len(list1)) # 5
# # 下标(索引)运算
# print(list1[0]) # 1
# print(list1[4]) # 100
# # print(list1[5])  # IndexError: list index out of range
# print(list1[-1]) # 100
# print(list1[-3]) # 5
# list1[2] = 300
# print(list1) # [1, 3, 300, 7, 100]
# # 通过循环用下标遍历列表元素
# for index in range(len(list1)):
#     print(list1[index])
# # 通过for循环遍历列表元素
# for elem in list1:
#     print(elem)
# # 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
# for index, elem in enumerate(list1):
#     print(index, elem)




# list1=[1,3,5,7,100]
# #添加元素
# list1.append(200)
# list1.insert(1,400)
# #合并两个列表
# list1=list1+[1000,2000]
# print(list1)
# if 3 in list1:
# 	list1.remove(3)
# if 1234 in list1:
#     list1.remove(1234)
# print(list1)
# # 从指定的位置删除元素
# list1.pop(0)
# list1.pop(len(list1) - 1)
# print(list1)
# # 清空列表元素
# list1.clear()
# print(list1) # []


#list的切片操作

# fruits=['grape','apple','strawberry','waxberry']
# fruits+=['pitaya', 'pear', 'mango']

# #列表切片
# fruits2=fruits[1:4]
# print(fruits2)
# # 可以通过完整切片操作来复制列表
# fruits3=fruits[:]
# print(fruits3)
# fruits4=fruits[-3:-1]
# print(fruits4)
# # 可以通过反向切片操作来获得倒转后的列表的拷贝
# fruits5=fruits[::-1]
# print(fruits5)

#列表排序
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2=sorted(list1)
#sorted函数返回列表排序后的拷贝不回修改传入的列表
#函数的设计就应该像sorted函数一样尽可能不生产副作用
list3=sorted(list1,reverse=True)
#通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表排序
list4=sorted(list1,key=len)
print(list1)
print(list2)
print(list3)
print(list4)



