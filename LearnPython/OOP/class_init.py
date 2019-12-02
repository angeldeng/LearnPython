class Person:
    def __init__(self,name):
        self.name=name
    def sayHi(self):
        print('Hello,my name is',self.name)
p=Person('Swaroop')
p.sayHi()


'''这里我们定义一个带有名为 name 形参的__init__方法(除了寻常的 self)。
然后我们又创建了一个名为 name 的字段。注意它们是两个不同的变量尽管都
叫‟name‟。点号允许我们将它们区分开来。
重点是，我们并没有显式的调用__int__方法，而是在创建类实例时在类名后面的
小括号中指定实参。这就是__init__的特殊之处。
初始化之后，我们就可以在方法中使用 self.name 字段了，方法 sayHi 演示了这
点。'''