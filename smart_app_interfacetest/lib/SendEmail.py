#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/1 下午6:48
# @Author  : motao
# @Site    : 
# @File    : SendEmail.py
# @Software: PyCharm

# 邮件发送模板

import smtplib
import unittest
import time
import os
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from smart_app_interfacetest.lib.HTMLTestRunner import HTMLTestRunner
from smart_app_interfacetest import config


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((
        Header(name, 'utf-8').encode(),
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))


# ================定义发送邮件附件=================
def send_file(file_new):
    smtpserver = config.smtp_server
    username = config.sender
    password = config.mail_pass
    sender = config.sender
