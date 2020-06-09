
# coding=utf-8
import requests
from random import randint,choice
import random,os,re
import json
import requests
import time
from random import randint
from datetime import date,timedelta
from Common.ReadYaml import ConfigYaml
from Common.MyUnit import MyTest
from Common.ReadYaml import CaseYaml
import yaml




# 获取当前项目根目录
curpath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# 获取yaml文件路径
config_yamlpath = os.path.join(os.path.join(curpath, "config"),'config.yaml')
case_yamlpath = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'Case.yaml')
# open方法打开文件直接读出来
with open(config_yamlpath, 'r', encoding='utf-8') as f:
    ret = f.read()
with open(case_yamlpath, 'r', encoding='utf-8') as f:
    ret1 = f.read()
d = yaml.load(ret)
d2 = yaml.load(ret1)
url = None
for i in d2['Door']['attribute']:
    for n in i['funName']:
        url = d['base_url']['Door'] + n['test_attribute_list']['url']


def list_id(url):
    '''
    获取属性管理列表数据ID
    :return:list_num-列表数据id
    '''
    print(url)
    url = url
    headers = {'Content-Type': 'application/json;charset=UTF-8', 'Cookie': 'GWSESSION=OTU3YzNmYzUtNmIwNS00MWQyLWI4MTYtNDg2OWMyNWFiZGQy'}
    data = {'appId':2,'viewType':1,'tenantId':'188078','ec_p':'1','ec_crd':'15','startDate':'','endDate':'','sortField':''}
    r = requests.get(url, headers=headers, params=data,stream=True, verify=False)
    result = r.json()
    print(result)
    list_num = []
    for i in result['data']['list']:
        id = i['id']
        if id != 1:
            list_num.append(id)
    return list_num

list_num = list_id()







