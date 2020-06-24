
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