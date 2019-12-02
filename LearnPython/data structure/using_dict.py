# 'ab'是'a'ddress'b'ook 的缩写

ab={'Swaroop':'swaroop@swaroopch.com',
    'Larry':'larry@wall.org',
    'Matsumoto':'matz@ruby-lang.org',
    'Spammer':'spammer@hotmail.com'
}
print('Swaroop\'s address is',ab['Swaroop'])

#删除一个键值对
del ab['Spammer']
print('\nThere are {0} contacts in the address-book\n'.format(len(ab)))
for name, address in ab.items():
    print('Contact {0} at {1}'.format(name, address))

# 添加一个键值对
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:    # OR ab.has_key('Guido')
    print("\nGuido's address is", ab['Guido'])

'''代码如何工作：
我们使用先前介绍的语法创建字典 ab。然后使用在列表和元组部分讨论过的索
引操作符指定字典键访问键值对。多简单的语法阿。
我们的老朋友 del 语句可以帮助我们删除键值对。只需简单的为索引操作符指定
被删除的键，再将其传给 del 语句就哦了。
执行删除操作时我们无需理会键所对应的值。
接下来我们使用字典的 items 方法访问字典的键值对，它会返回一个包含键值对
元组的列表 – 值跟在键后面。
在 for…in 循环中我们检索每个键值对并将它们分别赋给变量 name 和 address，
之后在循环体中打印它们。
利用索引操作符访问一个键并对其赋予一个值我们可以增加一个新的键值对，就
象本例中的 Guido 那样。
通过 dict 类的 has_key 可以检查字典中是否存在某个键值对。你可以执行 help(dict)
找到字典所有方法的列表'''