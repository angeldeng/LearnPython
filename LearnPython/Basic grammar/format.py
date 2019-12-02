age=25
name='Swaroop'
print('{0} is {1} years old'.format(name,age))
print('why is {0} playing with that python?'.format(name))
'''format 如何工作?
一个 string 可以含有某些格式说明符, 随后调用的 format 将用你提供给它的参数替换对
应的格式说明符.
观察上面的例子, {0}对应变量 name 它也是 format 的第 1 个参数. 与之类似{1}对应
format 的第 2 个参数 age.
注意我们也可以使用字符串连接达到同样的目的: name + ' is ' + str(age) + ' years 
old'.
但是这种方式太乱啊, 很容易出错. 而且需要手动将变量转换为字符串而 format 可以为我
们代劳.
最后, 使用 format 我们可以改变最终生成的字符串而不必修改传给 format 的变量, 反之
一样'''
#format 的本质就是将其参数替换到字符串中的格式说明符,\
# 下面是一些更复杂的使用方式:

print('{0:.3}'.format(1/3))
