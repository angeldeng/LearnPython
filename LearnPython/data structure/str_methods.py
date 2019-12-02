name = 'Swaroop' # 这是一个字符串对象
if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')
if 'a' in name:
    print('Yes, it contains the string "a"')
if name.find('war') != -1:
    print('Yes, it contains the string "war"')
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))

'''在这里我们看到了许多字符串方法的用法。
startswith 方法用于确定字符串是否以指定的字符串开头。而 in 操作检查一个字
符串是否是另一个字符串的一部分。
find 方法用来寻找给定的字符串在字符串中的位置，如果没找到对应的子串则返
回-1。
str 类还有一个简洁的连接序列中每个字符串并返回连接后的字符串的方法 join，
其中每个字符串都将以指定的字符串分隔。'''