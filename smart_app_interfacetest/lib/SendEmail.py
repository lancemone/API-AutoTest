#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/1 下午6:48
# @Author  : motao
# @Site    : 
# @File    : SendEmail.py
# @Software: PyCharm

# 邮件发送模板

import smtplib
import time
import os
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from smart_app_interfacetest.config.read_conf import Read_conf
from smart_app_interfacetest.lib import log_conf

config = Read_conf()
logger = log_conf.logger

# ================定义发送邮件附件=================
def send_file(file_new):
    smtpserver = config.get_email("smtp_server")
    username = config.get_email("sender")
    password = config.get_email("mail_pass")
    sender = config.get_email("sender")
    receiver = config.get_email("receiver")
    port = config.get_email("mail_port")
    # subject = '**自动化测试报告'
    file = open(file_new, 'r', encoding='UTF-8').read()
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    subject = "--API自动化测试报告--" + now
    # text = MIMEText(sendfile, "base64", "utf-8")   第一个是邮件正文，第二个是设置文本格式，第三个则用于设置文本编码
    text = MIMEText(file, "html", "utf-8")
    # 邮件内容
    msgRoot = MIMEMultipart()
    msgRoot["Subject"] = Header(subject, 'utf-8')
    # msgRoot["From"] = _format_addr(sender)
    # msgRoot["To"] = _format_addr(receiver)
    msgRoot["From"] = sender
    msgRoot["To"] = ','.join(receiver)
    msgRoot.attach(text)
    # 添加附件
    att = MIMEApplication(open(file_new, 'rb').read())
    att["Content-Type"] = "application/octet-stream"
    att.add_header("Content-Disposition", "attachment", filename='API自动化测试报告.html')
    # att["ContenT-Disposition"] = "attachment;filename = 'API自动化测试报告.html '"
    msgRoot.attach(att)

    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msgRoot.as_string())
        smtp.quit()
        logger.info('Mail Send Successful')
    except smtplib.SMTPException:
        logger.info('Mail Send Fail')


# ======查找测试目录，找到最新生成的测试报告文件======
def new_report(test_report):
    lists = os.listdir(test_report)  # 列出目录下的所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "/" + fn))  # linux
    # lists.sort(key=lambda fn: os.path.getmtime(test_report+"\\"+fn))    # 按时间排序win
    file_new = os.path.join(test_report, lists[-1])  # 获取最新的report文件
    logger.info(file_new)
    return file_new
