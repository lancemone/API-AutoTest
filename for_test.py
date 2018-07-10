#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 下午4:45
# @Author  : motao
# @Site    : 
# @File    : for_test.py
# @Software: PyCharm


# 根据输入内容打印出重复元素

def to_list():
    lst = input("请输入若干数字，每个数据之间使用','分隔:")
    list_input = lst.split(",")  # 对输入字符串进行分割处理
    list_input = [int(list_input[i]) for i in range(len(list_input))]  # for循环，把每个字符转成int值
    return list_input


def output_duplicate_values(lst_input):
    lst_unduplicate = []
    lst_duplicate = []
    for i in lst_input:
        if not i in lst_unduplicate:
            lst_unduplicate.append(i)
        else:
            lst_duplicate.append(i)
    print('重复的数据为', lst_duplicate)


data_input = to_list()
duplicate_values = output_duplicate_values(data_input)
