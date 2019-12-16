# from smtplib import SMTP
# from email.header import Header
# from email.mime.text import MIMEText

# def main():
#     #发送者
#     sender='287845794@qq.com'
#     receivers='1522799613@qq.com'
#     message=MIMEText('小小王你最棒','plain','utf-8')
#     message['From']=Header('老邓','utf-8')
#     message['To']=Header('小小王','utf-8')
#     message['Subject']=Header('python发送邮件','utf-8')
#     smtper=SMTP('smtp.qq.com',587)
#     smtper.login(sender, 'djgaiwf871010')
#     smtper.sendmail(sender, receivers, message.as_string())
#     print('邮件发送完成!')


# if __name__ == '__main__':
#     main()



# import smtplib

# sender = '287845794@qq.com'
# receivers = ['1522799613@qq.com']

# message = """
# This is a test e-mail message.
# """

# try:
#    smtpObj = smtplib.SMTP('smtp.qq.com',587)
#    smtpObj.sendmail(sender, receivers, message)         
#    print ("Successfully sent email")
# except SMTPException:
#    print ("Error: unable to send email")



# from email.mime.text import MIMEText
# from email.header import Header
# from smtplib import SMTP_SSL


# #qq邮箱smtp服务器
# host_server = 'smtp.qq.com'
# #sender_qq为发件人的qq号码
# sender_qq = '287845794@qq.com'
# #pwd为qq邮箱的授权码
# pwd = 'h**********bdc' ## h**********bdc
# #发件人的邮箱
# sender_qq_mail = '7697****@qq.com'
# #收件人邮箱
# receivers = ['yiibai.com@gmail.com','****su@gmail.com']

# #邮件的正文内容
# mail_content = '你好，这是使用python登录qq邮箱发邮件的测试'
# #邮件标题
# mail_title = 'Maxsu的邮件'


# #ssl登录
# smtp = SMTP_SSL(host_server)
# #set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
# smtp.set_debuglevel(1)
# smtp.ehlo(host_server)
# smtp.login(sender_qq, pwd)

# msg = MIMEText(mail_content, "plain", 'utf-8')
# msg["Subject"] = Header(mail_title, 'utf-8')
# msg["From"] = sender_qq_mail
# msg["To"] = Header("接收者测试", 'utf-8') ## 接收者的别名
# smtp.sendmail(sender_qq_mail, receivers, msg.as_string())
# smtp.quit()