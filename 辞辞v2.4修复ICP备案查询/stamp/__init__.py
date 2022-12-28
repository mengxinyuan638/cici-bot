"""本模块主要作用是发送邮件，有两种模式
    - 1:纯文字
    - 2:html形式
需要注意：本模块html需要配合模板使用

类Stmp_sand(to,title,my_msg)有三个参数

参数：
    - to 要发送的邮箱地址
    - title 邮件标题
    - my_msg 要发送的文字消息，如果是html形式，该参数为消息主体
内置方法：
    - mail(纯文字发信)
    - html(html发信)
方法返回值：
    - True(发信成功)
    - False(发信失败)

writen by 萌新源 at 2022/12/28
"""

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


my_sender = ''  # 填写发信人的邮箱账号
my_pass = ''  # 发件人邮箱授权码
html_file = './tem/mxy.html'  #在这里填写你的发信模板
report_html = open(html_file, "r", encoding="utf-8")
mail_msg = report_html.read()

class Stmp_send:
    def __init__(self,to,title,my_msg):
        self.my_user = to
        self.title = title
        self.msg = my_msg

    def html(self):
        """发送html模板"""
        ret = True
        try:
            msg = mail_msg.replace('{title}',self.title)
            msg = msg.replace('{msg}',self.msg)
            msg = MIMEText(msg, 'html', 'utf-8')  # 填写邮件内容
            msg['From'] = formataddr(["tracy", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["test", self.my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = self.title # 邮件的标题
            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
            server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱授权码
            server.sendmail(my_sender, [self.my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret = False
        return ret

    def mail(self):
        """普通的文字邮件"""
        ret = True
        try:
            msg = MIMEText(self.msg, 'plain', 'utf-8')  # 填写邮件内容
            msg['From'] = formataddr(["tracy", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["test", self.my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = self.title  # 邮件的标题
            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
            server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱授权码
            server.sendmail(my_sender, [self.my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret = False
        return ret
