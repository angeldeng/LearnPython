简介
(注: OOP 代表面向对象编程，OO 代表面向对象，以后全部使用英文缩写)
迄今为止我们编写的所有程序都是围绕函数创建的，函数即操纵数据的语句块。
这称作面向过程编程。
除此之外还有另一种组织程序的方法，将数据与功能组合到一起封装进被称为对
象的东西中。这叫做 OOP。
大多数时候你可以使用过程性编程，但当编写大型程序或问题更倾向以 OO 方式
解决时，你还可以使用 OOP 技术。
类和对象是 OOP 的两个重要特征。类用于创建新的类型，而对象是类的实例。
这就象你创建 int 类型的变量，这些变量就是 int 类的实例(对象)

静态语言程序员请注意
注意在 python 中就算整数也被当作对象(int 类的对象)。
这与 C++和 Java(版本 1.5 之前)是不同的，它们中的整数属于原始本地类型。具
体详见 help(int)。
而 C#和 java 1.5 程序员会发现这与装箱(boxing)和拆箱(unboxing)的概念类似。
对象可以使用属于这个对象的变量存储数据。属于对象或类的变量称作字段
(fields)。
对象同样可以利用属于类的函数实现所需的功能。这些函数被称作类的方法
(method)。
这些术语非常重要，因为它们帮助我们将独立的函数和变量与属于类或对象的函
数和变量区分开来。
字段与方法统称为类属性。
字段分为两种类型 – 它们既可以属于类的实例/对象也可以属于类本身，两者分
别称为实例变量与类变量。
一个类通过关键字 class 创建。字段与方法被列在类的缩进块里。


self
类方法与普通函数只有一个特殊区别 – 类方法必须增加一个额外的形参，而且它
必须处于第一个形参的位置，
但是在调用类方法时不要为这个额外的形参传值，python 会自动代劳。这个特别
的变量引用对象本身，按照惯例它被命名为 self。
尽管你可以随便为这个形参取名字，但我强烈建议你使用 self – 其它名字会让人
皱眉头的。
使用标准名字是有很多好处的 – 任何你的代码的读者都会立即明白它代表什么，
甚至当你使用标准名字时专业的 IDE 都会更好的帮助你。

_init__方法
在 python 的类中，有很多方法名拥有特殊意义。我们现在看看__init__方法的特
别之处。
__init__方法在类对象被实例化时立即执行。此方法专用于初始化对象。另外注
意方法名中的双下划线前后缀。


类和对象变量
我们已经讨论了类与对象的功能(方法)部分，现在就来学习数据部分。
数据即字段，只不过是绑定在类和对象的名字空间中的普通变量。这意味着这些
名字只在其所属类和对象的上下文中合法有效。这就是它们被称作名字空间的原
因。
有两种字段类型 – 类变量和对象变量，它们根据所有者是类还是对象而区分开
来。
类对象是共享的 – 它们可以被一个类的所有实例存取。即一个类对象在类中只存
在一个拷贝，任何对象对其的修改都会反映到所有对象上。
而每个独立的类对象/实例都拥有自己的对象变量。这样每个对象都有属于自己
的字段拷贝即这些字段非共享，不同对象中的同名对象变量彼此没有任何关联。


继承
OOP 的主要好处就是代码重用，而达此目的的方法之一是利用继承机制。最好
将继承想象为实现类与类之间的类型与子类型关系。
假设你想要编写一个程序用来追踪大学里的师生情况。师生有很多共同的特征比
如名字，年龄和地址等。
他们还拥有一些不同的特征例如教师的薪水课程假期，学生的成绩学费等。
你可以分别为师生创建两个独立的类并分别处理之，但增加一个共同的特征意味
两个类都要增加。很快这种设计方式就会变的笨重臃肿。
更好的办法是创建一个称为 SchoolMember 的通用类，然后让教师和学生类分别
继承它即成为 SchoolMember 的子类型。之后再增加各自的专有特征。
这样做有很多优点，我们为 SchoolMember 增加或修改任何功能都会自动反映到
它的子类型中。
例如，你可以为教师和学生类增加一个 ID 卡字段，这只需简单的将其加入
SchoolMember 即可。不过子类型中的改变不会影响到其他子类型
另一个好处是如果你能够以 SchoolMember 对象引用教师或学生对象，这对于统
计学校人数之类的情形很有用。
这被称作多态，在任何需要父类型的地方其子类型都可以被替换成父类型，即对
象可以被当做父类的实例。
另外我们可以复用父类代码而无需在不同的类中重复这些代码，但使用我们先前
讨论的独立类时就不得不重复了。
本例中的 SchoolMember 类被称为基类或超类。Teacher 和 Student 类叫做派生类
或子类。