# -*- coding: utf-8 -*-
# 简单邮件传输协议
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def SendEmail(emailAddress, emailSubject, info):
    #str=info+info

    # 设置邮箱的域名
    HOST = 'smtp.qq.com'#此行代码作废，因在ssl.py中将第845行的 self.server_hostname指定为'smtp.qq.com'
    message = MIMEMultipart('related')

    # 设置邮件标题
    SUBJECT = emailSubject
    # 设置发件人邮箱
    FROM = '390400239@qq.com'
    # 设置收件人邮箱
    TO = emailAddress+'@qq.com'

    # --------------------------------------发送文本-----------------
    # 发送邮件主体到对方的邮箱中
    message_html = MIMEText('<h2 style="color:red;font-size:100px">'+info+'</h2><img src="cid:big">', 'html', 'utf-8')
    message.attach(message_html)

    # 设置邮件发件人
    message['From'] = FROM
    # 设置邮件收件人
    message['To'] = TO
    # 设置邮件标题
    message['Subject'] = SUBJECT

    # 获取简单邮件传输协议的证书
    email_client = smtplib.SMTP_SSL()
    # 设置发件人邮箱的域名和端口，端口为465
    email_client.connect('smtp.qq.com', '465')
    # ---------------------------邮箱授权码------------------------------
    result = email_client.login(FROM, 'ehrnfkecbbphbjbe')
    print('登录结果', result)
    email_client.sendmail(from_addr=FROM, to_addrs=TO.split(','), msg=message.as_string())
    # 关闭邮件发送客户端

