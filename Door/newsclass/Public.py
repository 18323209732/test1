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
    def __init__(self, value='id', status=200, response_key='data', response_list='list'):
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
        self.value = value
        self.status = status
        self.response_key = response_key
        self.response_list = response_list

    def add_classnews(self):
        '''
        获取新闻资讯列表数据
        :return:
        '''
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self.public_data = ReadPublic(catalog='newsclass', key="add_classnews")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        self.headers[self.type] = self.json_type

        data = self.public_data.public_value("bar")
        img_url = choice(self.get_picture_ids()).get("id")
        data['name'] = random_str("自动化新增分类...")
        data['des'] = random_str("<p>自动化新增分类描述数据...</p>\n")
        data['imgUrl'] = img_url
        data['imgThumbUrl'] = img_url
        data['summary'] = random_str("自动化新增分类来源数据...")
        data['keywords'] = random_str("关键词...")
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)

    def add_link_class(self):
        '''
        获取新闻资讯列表数据
        :return:
        '''
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self.public_data = ReadPublic(catalog='newsclass', key="add_link_class")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        self.headers[self.type] = self.json_type

        data = self.public_data.public_value("bar")
        value = choice(self.get_picture_ids())
        img_url = value.get("imgUrl")
        img_id = value.get("id")
        data['name'] = random_str("自动化新增连接分类...")
        data['des'] = random_str("<p>自动化新增分类描述数据...</p>\n")
        data['imgUrl'] = img_url
        data['imgId'] = img_id
        data['imgThumbUrl'] = img_url
        data['summary'] = random_str("自动化新增分类来源数据...")
        data['keywords'] = random_str("关键词...")
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)

    @ReExecution(add_classnews, response_list='data')
    def get_classnews_id(self):
        '''
        获取新闻资讯列表数据
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self.public_data = ReadPublic(catalog='newsclass', key="list_classnews")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url

        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, data=data, stream=True, verify=False)
        result = r.json()

        return result

    def file_upload(self):
        '''
        添加新闻资讯
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        file_path = Any_Path("File", "picture.jpg")
        del self.headers[self.type]
        f = open(file_path, "rb")
        file = {"file": f}
        self.public_data = ReadPublic(catalog='newsclass', key="file_upload")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, data=data, files=file, stream=True, verify=False)

    @ReExecution(file_upload, status='200', response_list='list')
    def get_pictures(self):
        '''
        获取新闻资讯分类数据
        :return:
        '''
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='newsclass', key="get_picture")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.get(url, headers=self.headers, data=data, stream=True, verify=False)
        result = r.json()

        return result

    def get_class_ids(self):
        '''
        获取新闻id
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='newsclass', key="list_classnews")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
        result = r.json()
        if result.get("data").get("data"):
            return result.get("data").get("data")
        else:
            self.add_classnews()
            r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
            result = r.json()
            if result.get("data").get("data"):
                return result.get("data").get("data")
            else:
                return False

    def get_move_ids(self,swich=True):
        '''
        获取新闻id
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='newsclass', key="list_classnews")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
        result = r.json()
        ordinary_id = []
        link_id = []
        if result.get("data").get("data"):
            if swich:
                for or_id in result.get("data").get("data"):
                    if or_id.get("type") == 1:
                        ordinary_id.append(or_id.get("id"))
                if not ordinary_id:
                    self.add_classnews()
                    r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
                    result = r.json()
                    for or_id in result.get("data").get("data"):
                        if or_id.get("type") == 1:
                            ordinary_id.append(or_id.get("id"))
                return ordinary_id
            else:
                for l_id in result.get("data").get("data"):
                    if l_id.get("type") == 2:
                        link_id.append(l_id.get("id"))
                if not link_id:
                    self.add_link_class()
                    r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
                    result = r.json()
                    for l_id in result.get("data").get("data"):
                        if l_id.get("type") == 2:
                            link_id.append(l_id.get("id"))
                return link_id

    def get_picture_ids(self):
        '''
        获取新闻id
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='newsclass', key="get_picture")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
        result = r.json()
        if result.get("data").get("list"):
            return result.get("data").get("list")
        else:
            self.file_upload()
            r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
            result = r.json()
            if result.get("data").get("list"):
                return result.get("data").get("list")
            else:
                return False

if __name__ == "__main__":
    # print(Public_Data().get_move_ids(swich=False))
    pass
