#This is my shopping list
shoplist=['apple','mango','carror','banana']
print('I have',len(shoplist),'items to purchase')
print('These items are',end='')
for item in shoplist:
    print(item,end=' ')
print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now',shoplist)
print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is',shoplist)
print('The first item I will buy is',shoplist[0])
olditem=shoplist[0]
del shoplist[0]
print('I bought the',olditem)
print('My shopping list is now',shoplist)


'''变量 shoplist 是某个购物人的购物清单。
我们只在 shoplist 中存储被购买物品的名字的字符串，但你也可以为列表增加任
何其它种类的对象，包括数字甚至是其它列表。
我们通过 for…in 迭代列表元素，现在你一定意识到一个列表也是一个序列了吧。
有关序列的特点我们会在后节讨论。
注意 print 的 end 关键字实参，它指定我们希望以空格结束输出而不是通常的换
行。
接下来我们使用列表对象的 append 方法为列表添加一个新的元素。
为了确定元素真的被添加进去了，我们简单的将列表传给 print 函数，print 函数
整洁的将列表内容打印出来。
随后我们使用列表的 sort 方法对列表进行排序，紧记 sort 会影响列表本身而不是
返回一个被修改后的列表。
这与字符串的工作方式不同。这也是为什么说类标是可变类型而字符串是不可变
类型的原因。
然后当在市场购买一样东西后，我们希望将其从列表中删除，del 语句正是用武
之地。
在这里我们指出希望删除列表中的哪个元素，del 就将这个元素从列表中删除。
我们指定的是希望删除列表的第一个元素，因此我们使用 del shoplist[0](回想一
下，python 的索引从 0 开始)'''
