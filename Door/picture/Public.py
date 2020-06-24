
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

    def get_news(self, swich=True, use=False):
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
        if result.get('status') == '200':
            if swich:
                try:
                    value = choice(result.get('data').get('list'))
                    yield value.get('name')
                except StopIteration:
                    pass

            else:
                if use:
                    try:
                        value = choice(result.get('data').get('list'))
                        if value.get('used') == 1:
                            yield value.get('id')
                    except StopIteration:
                        pass
                else:
                    try:
                        value = choice(result.get('data').get('list'))
                        yield value.get('id')
                    except StopIteration:
                        pass


    @property
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
        if result.get('status') == '200':
            value = choice(result.get('data').get('list'))
            yield value.get('imgUrl')

    def get_class(self, swich=True):
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
        if result.get('status') == '200':
            if swich:
                try:
                    value = choice(result.get('data'))
                    yield value.get('className')
                except StopIteration:
                    pass

            else:
                try:
                    value = choice(result.get('data'))
                    yield value.get('id')
                except StopIteration:
                    pass

if __name__ == "__main__":
    # print(next(Public_Data().get_class(swich=False)))
    pass

