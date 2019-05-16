# -*- coding: utf-8 -*-
# 简单邮件传输协议
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def SendEmail():
# 设置邮箱的域名
  HOST = 'smtp.qq.com'
message = MIMEMultipart('related') 


  # 设置邮件标题
  SUBJECT = 'csdn博客代码'
  # 设置发件人邮箱
  FROM = '390400239@qq.com'
  # 设置收件人邮箱
  TO = '390400239@qq.com'
  

  # --------------------------------------发送文本-----------------
  # 发送邮件主体到对方的邮箱中
  message_html = MIMEText('<h2 style="color:red;font-size:100px">CSDN博客超级好</h2><img src="cid:big">', 'html', 'utf-8')
  message.attach(message_html)

  # -------------------------------------发送图片--------------------
  # rb  读取二进制文件
  # 要确定当前目录有1.jpg这个文件
  #image_data = open('1.jpg', 'rb')
  # 设置读取获取的二进制数据
  #message_image = MIMEImage(image_data.read())
  # 关闭刚才打开的文件
  #image_data.close()
  #message_image.add_header('Content-ID', 'big')
  # 添加图片文件到邮件信息当中去
  # message.attach(message_image)

  # -------------------------------------添加文件---------------------
  # 要确定当前目录有table.xls这个文件
  #message_xlsx = MIMEText(open('table.xls', 'rb').read(), 'base64', 'utf-8')
  # 设置文件在附件当中的名字
  #message_xlsx['Content-Disposition'] = 'attachment;filename="test1111.xlsx"'
  #message.attach(message_xlsx) 

  # 设置邮件发件人
  message['From'] = FROM
  # 设置邮件收件人
  message['To'] = TO
  # 设置邮件标题
  message['Subject'] = SUBJECT 

  # 获取简单邮件传输协议的证书
  email_client = smtplib.SMTP_SSL()
  # 设置发件人邮箱的域名和端口，端口为465
  email_client.connect(HOST, '465')
  # ---------------------------邮箱授权码------------------------------
  result = email_client.login(FROM, 'ehrnfkecbbphbjbe')
  print('登录结果', result)
  email_client.sendmail(from_addr=FROM, to_addrs=TO.split(','), msg=message.as_string())
  # 关闭邮件发送客户端

