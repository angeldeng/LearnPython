class Robot:
    '''Represents a robot, with a name.'''
# 一个类变量用于记录机器人的数量
    population = 0
    def __init__(self, name):
        '''Initializes the data.'''
        self.name = name
        print('(Initializing {0})'.format(self.name))
        # When this person is created, the robot
        # adds to the population
        Robot.population += 1
    def __del__(self):
        '''I am dying.'''
        print('{0} is being destroyed!'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{0} was the last one.'.format(self.name))
        else:
            print('There are still {0:d} robots working.'.format(Robot.population))
    def sayHi(self):
        '''Greeting by the robot.
        Yeah, they can do that.'''
        print('Greetings, my masters call me {0}.'.format(self.name))
    def howMany():
        '''Prints the current population.'''
        print('We have {0:d} robots.'.format(Robot.population))
    howMany = staticmethod(howMany)

droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()
droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()
print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")
del droid1
del droid2
Robot.howMany()

'''代码如何工作：
这个例子很长但有助于演示类和对象变量的本质。
population 属于 Robot 类因此它是个类变量。变量 name 属于对象(使用 self 赋值)
因此它是个对象变量。
于是乎，我们使用 Robot.population 引用类变量 populatin 而不是 self.population.。
而在方法中引用对象变量 name 时使用 self.name 语法。
记住这个类变量和类对象中简单的差异吧。还要注意对象变量会隐藏同名的类变
量！
howMany 实际上是一个属于类的方法而不是对象。这意味着我们可以将及其定
义为 classmethod 也可以定义为 staticmethod，
这取决于我们是否需要知道我们是哪个类的一部分。因为我们无需类似信息，所
以我们使用 staticmethod。
另外我们还可以通过装饰符(decorators)达到同样的效果：
@staticmethod
def howMany():
Prints the current population.
print('We have {0:d} robots.'.format(Robot.population))
装饰符可以被想象成调用一条显式语句的捷径，就像在这个例中看到的一样。
73 / 99
观察__init__方法，它用于以一个指定的名字初始化 Robot 实例。其内部对
population 累加 1，因为我们又添加了一个机器人。
同时观察 self.name，它的值特定于每个对象，这也指出了类对象的本质。
记住，你只能使用 self 引用相同对象的变量和方法。这被称作属性引用。
本例中，我们还在类与方法中使用了文档字符串。我们可以在运行时使用
Robot.__doc__和 Robot.sayhi.__doc__分别访问类和方法的文档字符串。
就像__init__方法，这里还有另一个特殊方法__del__，当对象挂掉的时候将被调
用。
对象挂掉是指对象不再被使用了，它占用的空间将返回给系统以便重复使用。
在__del__中我们只是简单的将 Robot.population 减 1。
当对象不再被使用时__del__方法将可以被执行，但无法保证到底啥时执行它。
如果你想显式执行它则必须使用 del 语句，就象本例中做的那样。（注：本例中
del 后对象的引用计数降为 0）。'''