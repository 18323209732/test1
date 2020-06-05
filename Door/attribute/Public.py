
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

def list_id():
    url = 'https://2004105022-site.pool5.yun300.cn/manager/gwforward/manager-webapi/product/productAttribute/list?viewType=1&tenantId=188078&appId=2&ec_p=1&ec_crd=15&startDate=&endDate=&sortField=&sortType='
    headers = {'Content-Type': 'application/json;charset=UTF-8', 'Cookie': 'GWSESSION=OTU3YzNmYzUtNmIwNS00MWQyLWI4MTYtNDg2OWMyNWFiZGQy'}
    r = requests.get(url, headers=headers, stream=True, verify=False)
    result = r.json()
    list_num = []
    for i in result['data']['list']:
        id = i['id']
        if id != 1:
            list_num.append(id)
    return list_num

list_num = list_id()