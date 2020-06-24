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
from Door.news.Public import Public_Data as pub_news
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
        self.pub_news_data = pub_news()
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
        img_url = next(pub_news().get_pictures(value='id'))
        data['name'] = random_str("自动化新增分类...")
        data['des'] = random_str("<p>自动化新增分类描述数据...</p>\n")
        data['imgUrl'] = img_url
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

    @ReExecution(add_classnews, response_list='data') #value='name'
    def get_classnews_name(self):
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

if __name__ == "__main__":
    # print(next(Public_Data().get_classnews_name()))
    pass
