
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

    def add_class(self):
        '''
        添加分类
        :return:
        '''
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='picture', key="add_class")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url

        data = self.public_data.public_value("bar")
        data['className'] = random_str("自动化测试分类")
        data['classInfo'] = random_str("自动化测试分类描述内容数据")

        r = requests.post(url, headers=self.headers, data=data, stream=True, verify=False)


    def file_upload(self):
        '''
        上传文件
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        file_path = Any_Path("File", "picture.jpg")
        del self.headers[self.type]
        f = open(file_path, "rb")
        file = {"file": f}
        self.public_data = ReadPublic(catalog='picture', key="file_upload")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, data=data, files=file, stream=True, verify=False)

    @ReExecution(add_class, status='200', swich=False, isuse=1, key='used')
    def get_news_used(self):
        '''
        获取新闻资讯列表数据
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='picture', key="get_picture")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, data=data, stream=True, verify=False)
        result = r.json()

        return result

    @ReExecution(add_class, status='200')
    def get_news(self):
        '''
        获取新闻资讯列表数据
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='picture', key="get_picture")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, data=data, stream=True, verify=False)
        result = r.json()

        return result


    @ReExecution(file_upload, status='200')   #imgUrl
    def picture_name(self):
        '''
        获取新闻资讯列表数据
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='picture', key="picture_url")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}&pageSize=15&currentPage=1&queryStatus=&startDate=&endDate=&name=&classId="
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.get(url, headers=self.headers, json=data, stream=True, verify=False)
        result = r.json()

        return result


    @ReExecution(add_class, status='200', response_list='')
    def get_class(self):
        '''
        获取新闻资讯列表数据
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='picture', key="get_class")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.get(url, headers=self.headers, data=data, stream=True, verify=False)
        result = r.json()

        return result


# if __name__ == "__main__":
#     print(next(Public_Data().get_news(value='id')))
#     # Public_Data().add_class()
#     pass

