
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
from Common.GetToken import Get_Cookies
from Common.ReadWriteIni import ReadWrite
from Common.ReadYaml import ReadPublic, ConfigYaml
from Common.Route import Any_Path

projectName = ConfigYaml("projectName").base_config
from Common.ReExecution import ReExecution
from Door.picture.Public import Public_Data as picture
from Door.news.Public import Public_Data as pub_news


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

    def file_add(self):
        '''
        添加分类
        :return:
        '''
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='filelibrary', key="file_add")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")

        self.headers[self.type] = self.json_type
        del self.headers[self.type]

        r = requests.post(url, headers=self.headers, data=data, stream=True, verify=False)

    def class_add(self):
        '''
        添加分类
        :return:
        '''
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='filelibrary', key="class_add")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")

        data['className'] = random_str("自动化测试")
        data['classInfo'] = random_str("自动化测试描述")

        self.headers[self.type] = self.form_type
        r = requests.post(url, headers=self.headers, data=data, stream=True, verify=False)

    @ReExecution(file_add, status='200')
    def file_list(self):
        '''
        获取新闻资讯列表数据
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='filelibrary', key="file_list")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        self.headers[self.type] = self.form_type
        data = self.public_data.public_value("bar")
        r = requests.get(url, headers=self.headers, data=data, stream=True, verify=False)

        result = r.json()

        return result

    def get_key(self):
        '''
        获取新闻资讯列表数据
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='filelibrary', key="get_key")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        self.headers[self.type] = self.json_type
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)

        result = r.json()

        if result["status"] == 200:
            return result['data']['key'], result['data']['signature']['signature'],\
                   result['data']['signature']['kssAccessKeyId'],result['data']['signature']['policy']

    @ReExecution(class_add, response_list='', status='200')
    def class_list(self):
        '''
        获取新闻资讯列表数据
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='filelibrary', key="class_list")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url

        r = requests.get(url, headers=self.headers, stream=True, verify=False)
        result = r.json()

        return result

    def get_class_list(self):
        '''
        获取新闻id
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='filelibrary', key="class_list")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.get(url, headers=self.headers, stream=True, verify=False)
        result = r.json()

        if result.get("data"):
            return result.get("data")
        else:
            self.class_add()
            r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
            result = r.json()
            if result.get("data"):
                return result.get("data")
            else:
                return False

    def get_file_list(self):
        '''
        获取新闻id
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='filelibrary', key="file_list")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.get(url, headers=self.headers, stream=True, verify=False)
        result = r.json()
        if result.get("data").get("list"):
            return result.get("data").get("list")
        else:
            self.file_add()
            r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
            result = r.json()
            if result.get("data").get("list"):
                return result.get("data").get("list")
            else:
                return False


if __name__=="__main__":
    print(Public_Data().get_file_list())
    # pass