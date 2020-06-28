# coding=utf-8
from random import choice
from collections.abc import Iterable
from Common.FontColor import outcome
from datetime import datetime, timedelta
import random
import string
import time


def random_choice(data):
    '''
    随机取值
    :param data:
    :return:
    '''
    if isinstance(data, Iterable) and not isinstance(data, dict):
        result = choice(data)
        return result
    else:
        outcome('red', "该对象不可迭代,请检查确认....")


def get_data_time(value):
    '''
    获取当前日期前任意天数日期
    :param value:
    :return:
    '''
    today = datetime.now()
    date_time = timedelta(days=value)
    re_date = (today + date_time).strftime('%Y-%m-%d')
    return re_date


def random_char(index=1):
    '''
    随机生成一个字符
    :param index:
    :return:
    '''
    seeds = string.digits
    random_str = random.sample(seeds, index)
    result = "".join(random_str)
    return result

def thead_sort():
    '''
    表头排序
    :return:
    '''
    result = choice(['', 'asc', 'desc'])
    return result


def random_str(value: str):
    '''
    字符串时间格式
    :param value:
    :return:
    '''
    return value+str(int(time.time()*1000))


def randint_str(value: str, start, end):
    '''
    随机数
    :param value:
    :param start:
    :param end:
    :return:
    '''
    return value + str(random.randint(start, end))

def show_sort():
    '''
    展示排序
    :return:
    '''
    result = choice(['TITLE_DESC', 'default', 'TITLE_ASC', 'PUB_DATE_ASC', 'PUB_DATE_DESC'])
    return result


def get_hour_second(value):
    '''
    获取当前日期前任意天数日期
    :param value:
    :return:
    '''
    today = datetime.now()
    date_time = timedelta(days=value)
    re_date = (today + date_time).strftime('%Y-%m-%d %H:%M:%S')

    return re_date
