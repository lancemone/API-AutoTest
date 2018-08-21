#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/18 下午7:39
# @Author  : motao
# @Site    : 
# @File    : api_module.py
# @Software: PyCharm


import requests
import urllib3
import os
from smart_app_interfacetest.config import read_conf
from smart_app_interfacetest.lib.LogOut import MyLog as Log

conf = read_conf.Read_conf()


class Api_module:
    def __init__(self):
        urllib3.disable_warnings()
        global host, timeout
        host = conf.get_http("host")
        timeout = float(conf.get_http("timeout"))
        self.header = {
            "authority": conf.get_header("authority"),
            "user-agent": conf.get_header("user-agent"),
            "content-type": conf.get_header("content-type"),
            "Connection": conf.get_header("Connection")
        }
        self.url = None
        self.verify = False
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.files = {}

    def set_url(self, path):
        '''
        :param path:
        :return:
        '''
        self.url = ''.join(self.host, path)
        return self.url

    def set_header(self, name=None, value=None):
        '''

        :param name:
        :param value:
        :return:
        '''
        if name is None and value is None:
            return self.header
        else:
            self.header[name] = value
            return self.header

    def set_file(self, filename=[]):
        '''

        :param filename:
        :return:
        '''
        for i in range(len(filename)):
            file = filename[i]
            file_i_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), "common"), file)
            for x in range(len(filename)):
                try:
                    if os.path.splitext(file_i_path) is ".png" or ".jpg":
                        self.files[None] = ("file%s" % x, ("file%s.%s") % (x, os.path.splitext(file_i_path)),
                                            open(file_i_path, "rb"), "image/png")
                    else:
                        self.files[None] = ("file%s" % x, ("file%s.%s") % (x, os.path.splitext(file_i_path)),
                                            open(file_i_path, "rb"))
                except:
                    self.logger.error("读取文件出错!")
                    raise
                finally:
                    return self.files

    def https_get(self, url, value_name, headers):
        '''
        :param url:
        :param method:
        :param header:
        :param kwargs:
        :return:
        '''
        try:
            r = requests.get(url=url, heders=headers, verify=self.verify, timeout=self.timeout)
            if value_name is "status_code":
                return r.status_code
            if value_name is "json":
                return r.json()
            if value_name is "header":
                return r.headers
            if value_name is "raise":
                return r.raise_for_status()
        except TimeoutError:
            self.logger.error("Time Out!")
            return None

    def https_post(self, url, header, json, value_name, files=[]):
        '''

        :param url:
        :param header:
        :param data:
        :param value_name:
        :param filename:
        :return:
        '''
        if files is [] or None:
            try:
                r = requests.post(url=url, headers=header, json=json, verify=self.verify, timeout=timeout)
                if value_name is "status_code":
                    return r.status_code
                if value_name is "json":
                    return r.json()
                if value_name is "header":
                    return r.headers
                if value_name is "raise":
                    return r.raise_for_status()
            except TimeoutError:
                self.logger.error("Time Out!")
                return None
        else:
            try:
                r = requests.post(url=url, headers=header, json=json, files=files, verify=self.verify, timeout=timeout)
                if value_name is "status_code":
                    return r.status_code
                if value_name is "json":
                    return r.json()
                if value_name is "header":
                    return r.headers
                if value_name is "raise":
                    return r.raise_for_status()
            except TimeoutError:
                self.logger.error("Time Out!")
                return None
