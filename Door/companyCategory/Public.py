
# coding=utf-8
import configparser
import urllib3
import traceback
import requests, os
import requests.packages.urllib3
from Common.FontColor import outcome
import yaml
from ruamel.yaml import RoundTripDumper
from Common.Route import Any_Path
from Common.ReadYaml import ReadPublic, ConfigYaml
from urllib3 import encode_multipart_formdata


projectName = ConfigYaml("projectName").base_config
Url = ConfigYaml(projectName).base_url


def readyaml(file=None, key=None):
    """
    1. 获取文件当前路劲+文件名称
    2. 打开yaml文件
    3. 转译文件内容获取对应key的值
    """
    path = Any_Path(file, "Public.yaml")

    try:
        with open(path, 'r', encoding='utf-8') as f:
            value = yaml.load(f.read(), Loader=yaml.Loader)[key]
        return value
    except:
        pass


def readyaml_case(key=None):
    """
    1. 获取case.yaml的橱窗列表
    2. 转译文件内容获取对应test03_keywords_listShowcase的URL值
    """
    path = Any_Path("Door", "Case.yaml")

    try:
        with open(path, 'r', encoding='utf-8') as f:
            # value = yaml.load(f.read(), Loader=yaml.Loader)[key]
            value = yaml.load(f.read())['Door']['listShowcase'][0]['funName'][0]['test03_keywords_listShowcase']['url']

        return value
    except:
        pass


def writeyaml(w_key=None, w_value=None, n=None, file=None):
    """
    1. 打开当前文件下的yaml文件，n传入写入方法（a 为追加方式写入，w 为清空后重写）
    2. 传入要写入的key：value
    3. 转译文件，传入参数，去重｛｝，方便yaml直接读取数据
    """
    path = Any_Path(file, "Public.yaml")
    with open(path, n, encoding="utf-8") as yaml_file:
        data = {w_key: w_value}
        yaml.dump(data, yaml_file, Dumper=RoundTripDumper, allow_unicode=True)


def readconfig_yaml(basekey='base_url', key='Door'):
    path = Any_Path("Config", "Config.yaml")
    # print(path)
    with open(path, 'r', encoding='utf-8') as f:
        value = yaml.load(f.read(), Loader=yaml.Loader)[basekey][key]
    return value


def readconfig_ini(v=True):
    path = Any_Path("Door", "Config.ini")
    config = configparser.ConfigParser()
    config.read(path)
    cookies_value = config.get("session", "cookies")
    headers1 = {'Content-Type': 'application/json;charset=UTF-8'}
    headers2 = {'Content-Type': 'application/x-www-form-urlencoded'}
    headers3 = {'Content-Type': 'multipart/form-data'}
    headers4 = {}
    if v==True:
        headers1.update({'Cookie': cookies_value})
        return headers1
    elif v==3:
        headers3 = {'Cookie': cookies_value}
        return headers3
    elif v==4:
        headers4 = {'Cookie': cookies_value}
        return headers4
    else:
        headers2.update({'Cookie': cookies_value})
        return headers2

