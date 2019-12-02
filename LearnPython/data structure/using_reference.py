print('Simple Assignment')
shoplist=['apple','mango','carrot','banana']
mylist=shoplist    #只是指向相同对象的另一个名字
del shoplist[0] #我购买了第一个水果,把它从清单删除
print('shoplist is',shoplist)
print('mylist is',mylist)
# 注意列表 shoplist 和 mylist 打印了相同的内容，其中都不包括‟apple‟，因为它
# 们指向的是相同的对象。
print('Copy by making a full slice')
mylist = shoplist[:] # 以全切片创造一个列表的完整拷贝
del mylist[0] # 删除第一个元素
print('shoplist is', shoplist)
print('mylist is', mylist)
# 注意现在两个列表指向不同的对象（注：回忆一下，切片操作会返回一个新的对象！）

'''大多数的解释已经包含在注释中了。
记住，如果你想创建一个诸如列表这样的序列或复杂对象(不是象整数那样的简
单对象)的拷贝，必须使用切片操作。
如果你只是简单的用变量名指向另一个变量名，两者实际上将引用相同的对象，
如果你不注意这点将会招来麻烦！'''

