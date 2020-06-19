
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

    def get_news(self, swich=True):
        '''
        获取新闻资讯列表数据
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='news', key="get_news")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
        result = r.json()
        if result.get('status') == 200:
            if swich:
                if not result.get('data').get('pres'):
                    self.add_news()
                try:
                    value = choice(result.get('data').get('pres'))
                    yield value.get('title')
                except StopIteration:
                    pass

            else:
                if not result.get('data').get('pres'):
                    self.add_news()
                try:
                    value = choice(result.get('data').get('pres'))
                    yield value.get('id')
                except StopIteration:
                    pass

    @property
    def get_news_class(self):
        '''
        获取新闻资讯分类数据
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='news', key="get_news_class")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
        result = r.json()
        if result.get('status') == 200:
            try:
                value = choice(result.get('data').get('data'))
                yield value.get('id')
            except StopIteration:
                pass

    def add_news(self):
        '''
        获取新闻资讯分类数据
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='news', key="add_news")
        self.headers[self.type] = self.json_type
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")

        data['title'] = random_str("自动化新增新闻资讯")
        data['content'] = random_str("<p>自动化新增新闻资讯内容....</p>\n")
        data['infotype'] = str(next(self.get_news_class))
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)

    @property
    def get_pictures(self):
        '''
        获取新闻资讯分类数据
        :return:
        '''
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='news', key="get_picture")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.get(url, headers=self.headers, data=data, stream=True, verify=False)
        result = r.json()
        if result.get('data'):
            try:
                value = choice(result.get('data').get('list'))
                yield value.get('imgUrl')
            except StopIteration:
                pass

    @property
    def get_application(self):
        '''
        获取新闻资讯分类数据
        :return:
        '''
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='news', key="get_application")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"

        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, data=data, stream=True, verify=False)
        result = r.json()
        if result.get("status"):
            try:
                value = choice(result.get('data').get("relatedContentList"))
                yield value.get('id')
            except StopIteration:
                pass

if __name__ == "__main__":
    # print(next(Public_Data().get_application))
    pass

