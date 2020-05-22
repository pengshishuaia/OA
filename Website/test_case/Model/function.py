import HTMLTestRunner
from email.header import Header
from email.mime.text import MIMEText
from HTMLTestRunner import HTMLTestRunner  # 导入生成HTML报告的包
from selenium import webdriver
import os, sys
import time
import smtplib
from test_login import *
import unittest


# 截图
def insert_img(driver, filename):
    func_path = os.path.dirname(__file__)  # 获取当前文件的路径
    print(func_path)

    base_dir = os.path.dirname(func_path)  # 获取当前文件的上级目录
    print(base_dir)

    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    print(base_dir)

    base = base_dir.split("/Website")[0]
    print(base)

    filepath = base + "/Website/test_report/screenshot/" + filename
    print(filepath)
    driver.get_screenshot_as_file(filepath)


# 发送邮件
def send_mail(last_report):
    f = open(last_report, 'rb')
    mail_content = f.read()
    f.close()

    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'
    # 发送邮箱账号/密码
    user = '18910503484'
    password = 'wowangle23'
    # 发送邮箱
    sender = '18910503484@163.com'
    # 接收邮箱
    receiver = '381833817@qq.com'
    # 邮件主题
    subject = 'selenium自动化测试报告'

    msg = MIMEText(mail_content, 'html', 'utf-8')
    # 邮件标题
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver
    # 连接发送邮件
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    # smtp = smtplib.SMTP()
    # smtp.helo(smtpserver)
    # smtp.ehlo(smtpserver)
    # smtp.connect(smtpserver)
    smtp.login(user, password)
    print('开始发送')
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('发送成功')


# 查找最新的报告
def latest_report(report_dir):
    # 查询文件目录下的文件列表
    lists = os.listdir(report_dir)
    print(lists)
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    print("最新的测试报告是" + lists[-1])
    file = os.path.join(report_dir, lists[-1])
    print(file)
    return file
