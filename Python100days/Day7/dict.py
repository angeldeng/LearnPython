# 创建字典
scores = {'小小王': 25, '小博': 27}
print(scores)
# 创建字典的构造器语法

items1 = dict(one=1, two=2, three=3, four=4)
# 通过zip函数将两个序列压成字典

items2 = dict(zip(['a', 'b', 'c'], '123'))

# 创建字典的推导式语法
items3 = {num: num**2 for num in range(1, 10)}

print(items1, items2, items3)

#通过键可以获取字典中对应的值
print(scores['小小王'])
print(scores['小博'])

#遍历字典里的键值

for key in scores:
    print(f'{key}:{scores[key]}')

#更新字典里的元素
scores['小小王']=33
scores['会飞']=20
scores.update(志远=30,小月月=22)
print(scores)
# get方法也是通过键获取对应的值但是可以设置默认值
if '喵喵' in scores:
    print(scores['喵喵'])
print(scores.get('喵喵'))

print(scores.get('喵喵',60))

# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('小小王', 100))

print(scores)

#清空字典
scores.clear()
print(scores)







