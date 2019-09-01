#Smtplib模块方法
import smtplib   #smtplib 用于邮件发信动作
from_addr='……@qq.com'   #发信方的信息：发信邮箱，QQ邮箱授权码
password='……y'

to_addr='……@qq.com'    #1.0版收信方邮箱

to_addrs = []             #2.0用while循环收集收件人信息
while True:
    a=input('请输入收件人邮箱：')
    #输入收件人邮箱
    to_addrs.append(a)
    #写入列表
    b=input('是否继续输入，n退出，任意键继续：')
    #询问是否继续输入
    if b == 'n':
        break

import csv    #3.0引用csv模块收集收信人信息。
data = [['qxq', '……@qq.com'],['xy', '……@qq.com']]
#待写入csv文件的内容
with open('C:\\Users\\qxq\\Desktop\\test.txt', 'w', newline='') as f:  #写入数据
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

import csv
with open('C:\\Users\\qxq\\Desktop\\test.txt', 'r') as f:  #读取数据
    reader = csv.reader(f)
    for row in reader:
        to_addrs=row[1]


smtp_server='smtp.qq.com'    #发信服务器
server=smtplib.SMTP_SSL()     #开启发信服务，这里使用的是加密传输
server.connect(smtp_server,465)
server.login(from_addr,password)    #登录发信邮箱
server.sendmail(from_addr,to_addr,msg.as_string())     #发送邮件
server.quit()     #关闭服务器


#写邮件正文内容的email模块
from email.mime.text import MIMEText
msg=MIMEText('send by python 是猪','plain','utf-8')

#补充邮件主题和收发件人信息
from email.header import Header
msg['From']=Header(from_addr)
msg['To']=Header(to_addr)
msg['Subject']=Header('python test')

#丰富正文内容
text='''脑残徐徐你好！
我是全全
全全圆圆的全全'''
msg=msg=MIMEText(text,'plain','utf-8')

#群发邮件
to_addrs = ['……@qq.com','……@qq.com']  #收件人信箱改为列表
msg['To'] = Header(to_addrs)   #会报错
msg['to'] = Header(",".join(to_addrs))    #Header的第一个参数必须为字符串或者字节，以逗号连接





#1.0版本收发邮件
import smtplib     #smtplib 用于邮件发信动作
from email.mime.text import MIMEText        #email构建邮件内容
from email.header import Header          #构建邮件头
import csv   # 引用csv模块，用于读取邮箱信息

from_addr = input('请输入登录邮箱：')   #发信方的信息：发信邮箱，QQ邮箱授权码
password = input('请输入邮箱授权码：')

smtp_server='smtp.qq.com'    #发信服务器

text='''脑残徐徐你好！
我是全全
全全圆圆的全全'''
# 待写入csv文件的收件人数据：人名+邮箱
data = [['qxq', '……@qq.com'],['xy', '……@qq.com']]
# 写入收件人数据
with open('C:\\Users\\qxq\\Desktop\\test.txt', 'w', newline='') as f:  #写入数据
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
# 读取收件人数据，并启动写信和发信流程
with open('C:\\Users\\qxq\\Desktop\\test.txt', 'r') as f:  #读取数据
    reader = csv.reader(f)
    for row in reader:
        to_addrs=row[1]

        msg=MIMEText(text,'plain','utf-8')       # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码


        msg['From']=Header(from_addr)    #邮件头信息
        msg['To'] = Header(",".join(to_addrs))
        msg['Subject']=Header('python test')

        server = smtplib.SMTP_SSL(smtp_server)   #开启发信服务，此处使用加密传输
        server.connect(smtp_server,465)

        server.login(from_addr,password)    #登录发信邮箱

        try:
            server.sendmail(from_addr,to_addrs,msg.as_string())     #发送邮件
            print('恭喜，发送成功')
        except:
            print('发送失败，请重试')
        server.quit()     #关闭服务器

