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

    def add_department(self):
        '''
        获取新闻资讯分类数据
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='position', key="add_department")
        self.headers[self.type] = self.json_type
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        id_imgurl = choice(self.get_picture_ids())

        data['department']['name'] = random_str("自动化新增部门")
        data['department']['des'] = random_str("<p>自动化部门详情信息....</p>")
        data['department']['summary'] = random_str("<p>自动化部门描述信息....</p>")
        data['department']['keywords'] = random_str("<p>自动化部门关键词....</p>")
        data['department']['imgUrl'] = id_imgurl.get("imgUrl")
        data['department']['keywords'] = id_imgurl.get("id")

        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)

    def add_position(self):
        '''
        获取新闻资讯分类数据
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='position', key="add_position")
        self.headers[self.type] = self.json_type
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")

        id = choice(self.get_department_ids()).get("id")
        data["job"]['departmentId'] = id
        data['departmentId'] = id
        data["job"]['age'] = 24
        data["job"]['name'] = random_str("自动化测试职位发布名称")
        data["job"]['des'] = random_str("<p>自动化测试职位发布数据</p>")
        data["job"]['district'] = "四川省||成都市||锦江区"

        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)


    def get_picture_ids(self):
        '''
        获取新闻id
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='position', key="get_picture")
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
        self.public_data = ReadPublic(catalog='position', key="file_upload")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, data=data, files=file, stream=True, verify=False)

    def get_department_ids(self):
        '''
        获取新闻id
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='position', key="get_department")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.get(url, headers=self.headers, json=data, stream=True, verify=False)
        result = r.json()
        if result.get("data").get("pres"):
            return result.get("data").get("pres")
        else:
            self.add_department()
            r = requests.get(url, headers=self.headers, json=data, stream=True, verify=False)
            result = r.json()
            if result.get("data").get("pres"):
                return result.get("data").get("pres")
            else:
                return False

    def get_position_ids(self):
        '''
        获取新闻id
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='position', key="list_position")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.get(url, headers=self.headers, json=data, stream=True, verify=False)
        result = r.json()
        if result.get("data").get("pres"):
            return result.get("data").get("pres")
        else:
            self.add_position()
            r = requests.get(url, headers=self.headers, json=data, stream=True, verify=False)
            result = r.json()
            if result.get("data").get("pres"):
                return result.get("data").get("pres")
            else:
                return False

if __name__=="__main__":
    print(Public_Data().add_position())