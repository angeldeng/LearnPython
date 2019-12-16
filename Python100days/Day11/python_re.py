#验证输入用户名和QQ号是否有效并给出对应提示

# import re

# def main():
#     username=input('请输入用户名:')
#     qq=input('请输入QQ号:')
#     m1=re.match(r'^[0-9a-zA-Z_]{6,20}$',username)
#     if not m1:
#         print('请输入正确的用户名')
#     m2=re.match(r'^[1-9]\d{4,11}$',qq)
#     if not m2:
#         print('请输入正确的QQ号')
#     if m1 and m2:
#         print('你输入的信息是有效的!')

# if __name__=='__main__':
#     main()


#过滤不良内容
import re


def main():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)  # 你丫是*吗? 我*你大爷的. * you.


if __name__ == '__main__':
    main()




