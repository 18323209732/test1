
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
    return os.path.realpath('img.img')

"""
file_path = os.path.realpath('图片.jpg')
url = "https://2004105022-site.pool5.yun300.cn/manager/gwforward/dssresources/imageRepository/imageFileUpload?viewType=1"
headers = {"Cookie": "GWSESSION=M2RiOWNmY2YtZTIyYy00OGUwLTg0MzQtNWE5ODU1MzQwNzll"}
datas = {"appId": ""}
file = {"file": ("图片.jpg", open(file_path, "rb"), "image/jpeg")}
r = requests.post(url, headers=headers, data=datas, stream=True, verify=False, files=file)
print(r.json()['data']['imgUrl'])
print(r.json()['data']['fileID'])
"""

# 下载

from lxml import etree

headers = {"Cookie": "WSESSION=NWNiY2M5NTUtZTVlMi00NjlhLWE4OGMtN2FmYTdkMzFhNjFl"}

#引用 requests文件
import requests
#下载地址
url = "https://2004105022-site.pool5.yun300.cn/manager/gwforward/manager-webapi/content/info/download?downloadType=1"
Download_addres='https://2004105022-site.pool5.yun300.cn/manager/gwforward/manager-webapi/content/info/export?cateId=-1&beginDate=undefined&endDate=undefined&queryType=4&cateName=%E5%85%A8%E9%83%A8%E5%88%86%E7%B1%BB&export_begin_date=undefined&export_end_date=undefined'
#把下载地址发送给requests模块
f=requests.get(url, headers=headers, verify=False)
#下载文件
with open(r"c:\导出.zip","wb") as code:
     code.write(f.content)