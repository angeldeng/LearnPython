shoplist=['apple','mango','carrot','banana']
name='swaroop'

print('Item 0 is',shoplist[0])  #列表
print('Item 1 is',shoplist[1])
print('Item 2 is',shoplist[2])
print('Item 3 is',shoplist[3])
print('Item -1 is',shoplist[-1])
print('Item -2 is',shoplist[-2])
print('Character 0 is',name[0]) #字符串

print('Item 1 to 3 is',name[1:3])
print('characters 2 to end is',name[2:])
print('characer 1 to -1 is',name [1:-1])
print('characer start to end is',name [:])

'''首先我们看看如何使用索引得到序列的单个元素。这也被称作下标操作。
正如上面的代码，每当你在序列旁的方括号中指定一个数字的时候，python 会获
取这个索引所对应的序列元素。
回想一下，python 的索引从 0 开始计算。因此 shoplist[0]获取序列 shplist 的第一
个元素，而 shoplist[3]获取第四个元素。
索引也可以是负数，这时候位置将从序列尾开始计算。所以，shoplist[-1]引用序
列的最后一个元素，shoplist[-2]为倒数第二个。
切片操作的使用方法是先指定序列名后跟一对方括号，其中包含一对可选的由分
号分隔的数字。
注意这与你至今使用的索引操作非常相似。记住数字是可选的，但分号不可以省
略。
切片操作中的第一个数字（分号前）指出切片的开始位置而第二个数字（分号后）
指定将在哪个位置结束。
如果省略第一个数字则 python 将以序列的起点为开始处，而省略第二个数字时
切片会停止在序列的结尾处。
注意切片将在开始处开始，结束于结尾处之前，即包括开始处但不包括结尾处。
（注：比如 a[1:10]，返回的是 a[1]到 a[9]不包括 a[10]）。
因此，shoplist[1:3]开始于索引 1，包括索引 2 但止于索引 3，即返回一个包含两
个元素的切片。与之类似 shoplist[:]将返回整个序列的拷贝。
你还能以负索引切片。负数代表从序列的末尾开始反向计算位置。例如 shooplist[: 
-1]返回整个序列，但不包括未末的元素。
另外你还可以为切片提供第三个实参，它代表步长（默认为 1）。'''

shoplist = ['apple', 'mango', 'carrot', 'banana']
print(shoplist[::1],shoplist[::2],shoplist[::3],shoplist[::-1]) #步长默认为1,::1时则输出他本身



