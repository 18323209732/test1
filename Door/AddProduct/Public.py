
# coding=utf-8
import configparser
from Common.ReadWriteIni import ReadWrite
import requests
import traceback
import random,os,re
import json
import requests
from Common.MyUnit import MyTest
from Common.FontColor import outcome
from Common.ReadYaml import ConfigYaml
import yaml
from ruamel.yaml import RoundTripDumper


def readyaml(file=None, key=None):
    """
    1. 获取文件当前路劲+文件名称
    2. 打开yaml文件
    3. 转译文件内容获取对应key的值
    """
    path = os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\%s\Public.yaml" % file
    with open(path, 'r', encoding='utf-8') as f:
        value = yaml.load(f.read(), Loader=yaml.Loader)[key]
    return value


def writeyaml(w_key=None, w_value=None, n=None):
    """
    1. 打开当前文件下的yaml文件，传入写入方法（a 为追加方式写入，w 为清空后重写）
    2. 传入要写入的key：value
    3. 转译文件，传入参数，去重｛｝，方便yaml直接读取数据
    """
    with open("Public.yaml", n, encoding="utf-8") as yaml_file:
        data = {w_key: w_value}
        yaml.dump(data, yaml_file, Dumper=RoundTripDumper, allow_unicode=True)


def readconfig_yaml(key='Door'):
    path = os.path.abspath(os.path.join(os.getcwd(), "../.."))+r'\Config\Config.yaml'
    with open(path, 'r', encoding='utf-8') as f:
        value = yaml.load(f.read(), Loader=yaml.Loader)[key]
    return value


def readconfig_ini():

    cookies_value = ReadWrite(sign='session', option='cookies').read_ini_cookies()
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    headers.update({'cookies': cookies_value})
    return headers
print(readconfig_ini)




class GetAll:

    def get_product_attribute(self):
        """
        1. 获取属性列表及规格、规格值
        """
        try:
            headers = 1
            data = {}
            url = readconfig_yaml()+r'/manager/gwforward/manager-webapi/product/productAttribute/list?appId=2'
            r = requests.get(url, headers=headers, json=data, stream=True, verify=False)
        except:
            singular = str(traceback.format_exc())
            outcome('red', singular)
            return singular