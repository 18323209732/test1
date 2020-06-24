
# coding=utf-8
import requests
from random import randint,choice
import random,os,re
import json
import requests
import time
from random import randint
from datetime import date,timedelta
from Common.GetToken import Get_Cookies
from Common.ReadWriteIni import ReadWrite
from Common.ReadYaml import ReadPublic, ConfigYaml
projectName = ConfigYaml("projectName").base_config
url = ConfigYaml(projectName).base_url


class Public_Data:
    def __init__(self):
        '''
        '''
        self.type = ConfigYaml('type_key').base_config
        self.form_type = ConfigYaml('form_type').base_config
        self.cookies_key = ConfigYaml('cookies').base_config
        self.cookies_value = ReadWrite(sign='session', option='cookies').read_ini_cookies()
        self.headers = {self.type: self.form_type}
        self.headers.update({self.cookies_key: self.cookies_value})
        self.projectName = ConfigYaml("projectName").base_config
        self.url = ConfigYaml(projectName).base_url



    def get_news(self, swich=True):
        '''
        获取新闻资讯列表数据
        :return:
        '''
        self.public_data = ReadPublic(catalog='news', key="get_news")
        url = self.public_data.public_value("url")
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
        result = r.json()
        title = []
        news_id = []
        if result.get('status')==200:
            if swich:
                for value in result.get('data').get('pres'):
                    title.append(value.get('title'))

                return title
            else:
                for value in result.get('data').get('pres'):
                    news_id.append(value.get('id'))

                return news_id

    @property
    def get_news_class(self):
        '''
        获取新闻资讯分类数据
        :return:
        '''
        self.public_data = ReadPublic(catalog='news', key="get_news_class")
        url = self.public_data.public_value("url")
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
        result = r.json()
        class_id = []
        if result.get('status') == 200:
            for value in result.get('data').get('data'):
                class_id.append(value.get('id'))

        return class_id


