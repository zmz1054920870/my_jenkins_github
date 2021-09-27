#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 23:53
# @Author  : 超级无敌张铁柱
# @File    : send_email.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# def encryption(st):
#     encode = base64.b64encode(st.encode('utf-8'))
#     return str(encode, 'utf-8')
#
#
# def decrypt(st):
#     decode = base64.b64decode(st)
#     return str(decode, 'utf-8')
#
#
# def send(a, maillist):
#     email_host = 'smtp.exmail.qq.com'  # 邮箱地址
#     email_user = decrypt("aGV4aWFuZ3h1YW5AeGlhb2R1b3RlY2guY29t")  # 发送者账号
#     email_pwd = decrypt("aFhYNTIwLnRpbmc=")  # 发送者的密码
#     # 收件人邮箱，多个账号的话，用逗号隔开
#     me = email_user
#     msg = MIMEText(a)  # 邮件内容
#     msg['Subject'] = '创新效率测试组的bug和测试任务（自动发送，无需回复）'  # 邮件主题
#     msg['From'] = me  # 发送者账号
#     msg['To'] = ','.join(maillist)  # 接收者账号列表
#     smtp = smtplib.SMTP(email_host, port=25)  # 连接邮箱，传入邮箱地址，和端口号，smtp的端口号是25
#     smtp.login(email_user, email_pwd)  # 发送者的邮箱账号，密码
#     smtp.sendmail(me, maillist, msg.as_string())
#     # 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
#     smtp.quit()  # 发送完毕后退出smtp
#     print('email send success.')


class EmailManage(object):

    def __init__(self, filename):
        self.filename = filename

    def send_email(self):
        # 定义SMTP服务器
        smtpserver = 'smtp.163.com'

        # 发送邮件的用户名和客户端密码
        username = 'zmz1054920870@163.com'
        password = 'UPZMWDCEBQULAMUL'

        # 接收邮件的邮箱
        reveiver = '1054920870@qq.com'

        # 邮件的标题或者主题
        subject = '淘宝接口自动化测试报告'

        # 创建邮箱内容对象
        message = MIMEMultipart('related')

        # 邮件的附件，主要用于发送测试报告
        fujian = MIMEText(_text=open(self.filename, 'rb').read(), _subtype='html', _charset='utf8')

        # 添加邮箱内容
        message['from'] = username
        message['to'] = reveiver
        message['subject'] = subject
        message.attach(fujian)

        # 登录smtp服务器并发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)  # connect(self, host='localhost', port=0, source_address=None):

        smtp.login(username, password)
        smtp.sendmail(username, reveiver,
                      message.as_string())  # (self, from_addr, to_addrs, msg, mail_options=[],rcpt_options=[]):

        # 发送完成以后我们就退出这个服务器
        smtp.quit()

if __name__ == '__main__':
    EmailManage('C:\\Users\zmz\\Desktop\\test-tb-jenkins\\report.html').send_email()