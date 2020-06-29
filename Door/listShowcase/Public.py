# coding=utf-8
import configparser
import urllib3
from Common.ReadWriteIni import ReadWrite
from Common.ReadYaml import ConfigYaml
import traceback
import os,requests
import requests.packages.urllib3
from Common.FontColor import outcome
import yaml
from ruamel.yaml import RoundTripDumper


def readyaml(file=None, key=None):
    """
    1. 获取文件当前路劲+文件名称
    2. 打开yaml文件
    3. 转译文件内容获取对应key的值
    """
    path = os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\%s\Public.yaml" % file
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
    path = os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\Case.yaml"
    try:
        with open(path, 'r', encoding='utf-8') as f:
            # value = yaml.load(f.read(), Loader=yaml.Loader)[key]
            value = yaml.load(f.read())['Door']['listShowcase'][0]['funName'][0]['test03_keywords_listShowcase']['url']

        return value
    except:
        pass


def writeyaml(w_key=None, w_value=None, n=None):
    """
    1. 打开当前文件下的yaml文件，n传入写入方法（a 为追加方式写入，w 为清空后重写）
    2. 传入要写入的key：value
    3. 转译文件，传入参数，去重｛｝，方便yaml直接读取数据
    """
    with open("Public.yaml", n, encoding="utf-8") as yaml_file:
        data = {w_key: w_value}
        yaml.dump(data, yaml_file, Dumper=RoundTripDumper, allow_unicode=True)


def readconfig_yaml(basekey='base_url', key='Door'):
    path = os.path.abspath(os.path.join(os.getcwd(), "../.."))+r'\Config\Config.yaml'
    with open(path, 'r', encoding='utf-8') as f:
        value = yaml.load(f.read(), Loader=yaml.Loader)[basekey][key]
    return value


def readconfig_ini(v=True):
    path = os.path.abspath(os.path.join(os.getcwd(), "../.."))+r'\Door\Config.ini'
    config = configparser.ConfigParser()
    config.read(path)
    cookies_value = config.get("session", "cookies")
    headers1 = {'Content-Type': 'application/json;charset=UTF-8'}
    headers2 = {'Content-Type': 'application/x-www-form-urlencoded'}
    headers3 = {'Content-Type': 'multipart/form-data'}
    if v==True:
        headers1.update({'Cookie': cookies_value})
        return headers1
    elif v==3:
        headers3 = {'Cookie': cookies_value}
        return headers3
    else:
        headers2.update({'Cookie': cookies_value})
        return headers2


class GetAll:
    def __init__(self):
        self.tenant_value = readconfig_yaml(basekey='base_config', key='tenant_value')
        self.headers = readconfig_ini()

    def get_product_attribute(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        """
        1. 获取适合当前橱窗产品列表，并返回id
        """
        try:
            data = {"appId":2,"cateId":0,"showCaseId":readyaml(file='listShowcase', key='橱窗1号'),"attributeId":0,"pageSize":15,"pageNumber":1}
            url = readconfig_yaml() + r'/manager/gwforward/manager-webapi/product/productShowcase/listProduct?tenantId=%s' % (self.tenant_value)
            r = requests.post(url, headers=readconfig_ini(), json=data, stream=True, verify=False)
            result = r.json()
            id = result['data']['list'][0]['id']
            # print(result['data']['list'])
            return id
        except:
            singular = str(traceback.format_exc())
            outcome('red', singular)
            return singular

    def get_product_list(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        """
        1. 获取当前橱窗产品列表，并返回id
        """
        try:
            data = {"appId":2,"cateId":0,"showCaseId":readyaml(file='listShowcase', key='橱窗1号'),"attributeId":0,"pcStatus":"null","moStatus":"null","startDate":"","endDate":"","keyword":"","pageSize":15,"pageNumber":1,"orderColumn":"","order_productName":"","order_productCode":"","order_cateName":"","order_retailPrice":"","order_publishTime":"","order_pcStatus":"","order_moStatus":"","order_shortUrl":""}
            url = readconfig_yaml() + r'/manager/gwforward/manager-webapi/product/productInformation/list?tenantId=%s' % (self.tenant_value)
            r = requests.post(url, headers=readconfig_ini(), json=data, stream=True, verify=False)

            result = r.json()
            try:
                for i in result['data']['list']:
                    id = i['id']
                    #print(result['data']['list'])
                    return id

            except:
                writeyaml(w_key="删除", w_value="成功", n='a')


        except:
            singular = str(traceback.format_exc())
            outcome('red', singular)
            return singular



if __name__ == '__main__':
    GetAll().get_product_list()