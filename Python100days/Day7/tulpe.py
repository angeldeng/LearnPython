#Python中的元组与列表类似也是一种容器数据类型，
# 可以用一个变量（对象）来存储多个数据，
# 不同之处在于元组的元素不能修改，
# 在前面的代码中我们已经不止一次使用过元组了。
# 顾名思义，我们把多个元素组合到一起就形成了一个元组，
# 所以它和列表一样可以保存多条数据。
# 下面的代码演示了如何定义和使用元组。


#定义元组
tup=('小小王',25,True,'山西')
print(tup)
print(tup[0])
print(tup[3])

#遍历元组
for item in tup:
    print(item)

#重新给元组赋值,原有数组会被垃圾回收机制回收
tup=('小博',27,True,'湖北')
print(tup)

#将元组转换成列表
listtup=list(tup)
print(listtup)

#转换成列表之后我们可以修改他的元素
listtup[0]='邓邓'
listtup[1]='32'
print(listtup)

#再转换成元组
newtup=tuple(listtup)
print(newtup)


