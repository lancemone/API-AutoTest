#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 下午9:40
# @Author  : motao
# @Site    : 
# @File    : read_conf.py
# @Software: PyCharm
import codecs
import os
import configparser

prodir = os.path.split(os.path.realpath(__file__))[0]
confpath = os.path.join(prodir, "config.ini")


class Read_conf:
    def __init__(self):
        fb = open(confpath)
        conf = fb.read()
        # remove BOM
        if conf[:3] == codecs.BOM_UTF8:
            conf = conf[3:]
            file = codecs.open(confpath, "w")
            file.write(conf)
            file.close()
        fb.close()
        self.cf = configparser.ConfigParser()
        self.cf.read(confpath)

    def get_email(self, name):
        '''

        :param name:
        :return:
        '''
        value = self.cf.get("EMAIL", name)
        return value

    def get_db(self, name):
        '''

        :param name:
        :return:
        '''
        value = self.cf.get("DATABASE", name)
        return value

    def get_http(self, name):
        '''

        :param name:
        :return:
        '''
        value = self.cf.get("HTTP", name)
        return value

    def get_params(self, name):
        '''

        :param name:
        :return:
        '''
        value = self.cf.get("PARAMS", name)
        return value

    def get_header(self, name):
        '''

        :param name:
        :return:
        '''
        value = self.cf.get("HEADER", name)
        return value

    def set_header(self, name, value):
        '''

        :param name:
        :param value:
        :return:
        '''
        self.cf.set("HEADER", name, value)
        with open(confpath, "w+") as f:
            self.cf.write(f)

    def set_value(self, v_type, name, value):
        '''

        :param v_type:
        :param name:
        :param value:
        :return:
        '''
        self.cf.set("%s" % v_type, name, value)
        with open(confpath, "w+") as f:
            self.cf.write(f)
