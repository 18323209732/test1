
# coding=utf-8
import requests
from random import randint,choice
import random,os,re
import sys
from datetime import *
import json
import requests
import time
from random import randint
from datetime import date,timedelta
from Common.ReadYaml import ReadPublic

def Public_path():
    path = os.path.dirname(os.path.abspath('.')) + '/content/Public.yaml'
    # print(path)
    return path


def print_debug_info(o):
    """
    打印打印日期，文件名，行，函数名的方法
    :param o:
    :return:
    """
    try:
        raise Exception
    except :
        f = sys.exc_info()[2].tb_frame.f_back
    print('%s -- %s -- %d -- %s ' % (str(datetime.now()), os.path.basename(f.f_code.co_filename), f.f_lineno, f.f_code.co_name), end='')
    print(o)

# 例子
def test1():
    print("test1")
    print_debug_info('-->pass')

# test1()