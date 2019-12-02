#if else举例
username=(input('请输入用户名：'))
password=(input('请输入密码：'))

if username=='admin'and password=='123456':
    print('身份验证成功')
else:
    print('身份验证失败')

#也可以继续嵌套

#elif后面可以直接跟条件