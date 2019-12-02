zoo=('python','elephant','penguin')     #小括号可选
print('Number of cages in the new zoo is',len(zoo))
new_zoo=('monkey','camel',zoo)
print('Number of cages in the new zoo is',len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',len(new_zoo)-1+len(new_zoo[2]))

'''代码如何工作：
变量 zoo 引用一个元组。我们看到 len 函数可以得到元组的长度。这也表明元组
同样是一个序列类型。
因为老动物园歇菜了，于是我们将这些动物转移到一个新的动物园。因此元组
new_zoo 既包含已有的动物又包含从老动物园转移过来的新动物。
言归正传，注意一个包含在其它元组内的元组并不会丢失它的身份。
(注：包含元组会引用被包含元组，即在包含元组内对被包含元组的操作会反应
到被包含元组自身之上，有点绕口。。。)
像列表一样，我们可以通过一对方括号指定元素的位置访问这个元素。这叫做索
引操作符。
我们通过 new_zoo[2]访问 new_zoo 的第三个元素，通过 new_zoo[2][2]访问
new_zoo 的第三个元素的第三个元素。
一但你理解这种语言风格，这样的操作太安逸了.
虽然小括号是可选的，但我强烈建议你坚持使用小括号，这样一眼就能看出它是
个元组，尤其还能避免出现歧义。
例如，print(1, 2, 3)和 print((1, 2, 3))是不同的 – 前者打印 3 个数字而后者打印一
个元组(包含 3 个数字).'''


'''拥有 0 个或 1 个元素的元组
一个空元组通过空小括号创建，例如 myempty = ()。
不过，指定一个单元素元组就不那么直观了。你必须在其仅有的一个元素后跟随
一个逗号，这样 python 才能区分出
你要的是元组而不是一个被小括号包围的对象的表达式。例如你想要一个包含值
为 2 的单元素元组，则必须写成 singleton = (2, )'''
