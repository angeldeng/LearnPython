# s1='hello,world!'
# s2='hello,world!'
# #以三个双引号或单引号开头的字符串才可以折行

# s3='''
# hello,
# world!
# '''

# print(s1,s2,s3,end='\t')

s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')