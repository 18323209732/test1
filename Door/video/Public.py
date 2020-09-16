# coding=utf-8
import requests
from random import randint,choice
import random,os,re
import json
import requests
import time
from random import randint
from datetime import date,timedelta
import urllib3
from Common.CusMethod import random_str
from Common.ReExecution import ReExecution
from Common.ReadWriteIni import ReadWrite
from Common.ReadYaml import ReadPublic, ConfigYaml
from Common.Route import Any_Path

projectName = ConfigYaml("projectName").base_config


class Public_Data:

    def __init__(self):
        '''
        '''
        self.type = ConfigYaml('type_key').base_config
        self.form_type = ConfigYaml('form_type').base_config
        self.cookies_key = ConfigYaml('cookies').base_config
        self.json_type = ConfigYaml('json_type').base_config
        self.cookies_value = ReadWrite(sign='session', option='cookies').read_ini_cookies()
        self.headers = {self.type: self.form_type}
        self.headers.update({self.cookies_key: self.cookies_value})
        self.projectName = ConfigYaml("projectName").base_config
        self.url = ConfigYaml(projectName).base_url
        self.tenant_key = ConfigYaml('tenant_key').base_config
        self.tenant_value = ConfigYaml('tenant_value').base_config

    def get_signature(self):
        '''

        :return:
        '''
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.headers[self.type] = self.json_type
        self.public_data = ReadPublic(catalog='video', key="get_signature")
        url = self.public_data.public_value("url")
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, json=data,  stream=True, verify=False)
        if r.json().get("status"):
            return r.json().get("data").get("authData")

    def get_uploads(self):
        '''

        :return:
        '''
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        headers = {"Authorization": self.get_signature(),"Content-Type": "video/mp4"}
        url = "https://cetest02.cn-bj.ufileos.com/100001_2008145027/55.mp4?uploads"
        r = requests.post(url, headers=headers,   stream=True, verify=False)
        return r.json().get("UploadId")

    def get_signature_(self):
        '''

        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.headers[self.type] = self.json_type
        self.public_data = ReadPublic(catalog='video', key="get_signature_")
        url = self.public_data.public_value("url")
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
        if r.json().get("status") == 200:
            return r.json().get("data").get("authData")


    def upload(self):

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        headers = {"Authorization": self.get_signature_(), "Content-Type": "video/mp4","Content-Length": "3798643",
                   "Referer":"https://2008145027-site.pool202.yun300.cn/managePanel/videoLibrary/list?appId=167&initPanel=true&homeLocation=https://web-site.yun300.cn/manageHome/insideHome?instanceCode=NEW2020081410384609161&tenantId=207799&templateCode=global_site&currentPage=1&pageSize=15"}
        file_path = Any_Path("File", "55.mp4")
        file = {"file": open(file_path)}
        self.up_id = self.get_uploads()
        url = f"https://cetest02.cn-bj.ufileos.com/100001_2008145027/55.mp4?uploadId={ self.up_id}&partNumber=0"
        r = requests.put(url, headers=headers, files=file,stream=True, verify=False)


    def get_signature_one(self):
        '''

        :return:
        '''
        self.upload()
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.headers[self.type] = self.json_type
        self.public_data = ReadPublic(catalog='video', key="get_signature_one")
        url = self.public_data.public_value("url")
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
        if r.json().get("status") == 200:
            return r.json().get("data").get("authData")

    def get_size(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        headers = {"Authorization": self.get_signature_one(), "Content-Type": "video/mp4"}
        url = f"https://cetest02.cn-bj.ufileos.com/100001_2008145027/55.mp4?uploadId={ self.up_id}"
        r = requests.post(url, headers=headers, stream=True, verify=False)

    def save_file(self):
        '''

        :return:
        '''
        self.get_size()
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.headers[self.type] = self.form_type
        self.public_data = ReadPublic(catalog='video', key="save")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"+"&authPermission=video_add"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, data=data, stream=True, verify=False)

    def get_video_data(self):
        '''
        获取新闻id
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='video', key="get_video_data")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
        result = r.json()
        if result.get("status", []) == '200':
            if result.get("data").get("list"):
                return result.get("data").get("list")
            else:
                self.save_file()
                r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
                result = r.json()
                if result.get("status", []) == '200':
                    if result.get("data").get("list"):
                        return result.get("data").get("list")
                else:
                    return False

        else:
            return False



if __name__ == "__main__":
    Public_Data().save_file()
    pass
#

