
# coding=utf-8
import requests
from random import randint,choice
import random,os,re
import json
import requests
import time
from random import randint
from datetime import date,timedelta
from Common.ReadYaml import ReadPublic, ConfigYaml
projectName = ConfigYaml("projectName").base_config
Url = ConfigYaml(projectName).base_url

def Public_path():
    """当前路径"""
    return os.path.realpath('产品导入.zip')

"""

file_path = "D:/项目/门户接口自动化/Portal_interface/Door/product/产品导入.zip"
url = "http://2004105022.pool5-site.make.yun300.cn/manager/gwforward/manager-webapi/product/productStream/importZip"
headers = {"Cookie": "GWSESSION=ZDYzNGE5NWEtNWQxNC00MTc1LTg5N2EtMDJlYjM5YTVkYmEx"}
datas = {"isOverwrite": "false", "appId": "2"}
file = {"file": ("产品导入.zip", open(file_path, "rb"), "application/zip")}
r = requests.post(url, headers=headers, data=datas, stream=True, verify=False, files=file)
print(r.json())

"""