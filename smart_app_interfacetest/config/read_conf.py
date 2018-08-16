#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 下午9:40
# @Author  : motao
# @Site    : 
# @File    : read_conf.py
# @Software: PyCharm

import os

prodir = os.path.split(os.path.realpath(__file__))[0]
confpath = os.path.join(prodir, "config.ini")


class Read_conf:
    def __init__(self):
        fb = open(confpath)
        conf = fb.read()
