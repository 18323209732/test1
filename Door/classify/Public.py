
# coding=utf-8
import requests
from random import randint,choice
import random,os,re
import json
import requests
import time
from random import randint
from datetime import date,timedelta
from Common.ReadWriteIni import ReadWrite
from Common.ReadYaml import ReadPublic, ConfigYaml
projectName = ConfigYaml("projectName").base_config
url = ConfigYaml(projectName).base_url

class Classify:

    def __init__(self):
        self.type = ConfigYaml('type_key').base_config
        self.json_type = ConfigYaml('json_type').base_config
        self.cookies_key = ConfigYaml('cookies').base_config
        self.cookies_value = ReadWrite(sign='session', option='cookies').read_ini_cookies()
        self.headers = {self.type: self.json_type}
        self.headers.update({self.cookies_key: self.cookies_value})
        self.projectName = ConfigYaml("projectName").base_config
        self.url = ConfigYaml(projectName).base_url
        self.tenant_value = ConfigYaml('tenant_value').base_config



    def add_classify(self):
        '''
        添加分类
        :return: 分类id
        '''
        self.public_data = ReadPublic(catalog='classify', key="add_classify")
        url = self.public_data.public_value("url")
        url = self.url + url + "?tenantId={}".format(self.tenant_value)
        data = self.public_data.public_value("bar")
        data['introductionCategory']['name'] = '接口分类{}'.format(time.time())

        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
        result = r.json()

        return result['data']['id']

    def add_hide_classify(self):
        '''
        添加隐藏电脑版分类
        :return: 隐藏电脑版分类的id
        '''
        id = self.add_classify()
        self.public_data = ReadPublic(catalog='classify', key="add_hide_classify")
        url = self.public_data.public_value("url")
        url = self.url + url + "?tenantId={}".format(self.tenant_value)
        data = self.public_data.public_value("bar")
        data['id'] = id
        self.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        r = requests.post(url, headers=self.headers, data=data, stream=True, verify=False)
        result = r.json()

        return id
    def get_picture_id(self):
        '''
        获取分类图片列表id
        :return: 随机返回一个id
        '''
        self.public_data = ReadPublic(catalog='classify', key="get_picture_id")
        url = self.public_data.public_value("url")
        url = self.url + url + "&tenantId={}".format(self.tenant_value)
        self.headers['Content-Type'] = 'applicaton/x-www-form-urlencoded'
        r = requests.get(url, headers=self.headers, stream=True, verify=False)
        result = r.json()
        id = []
        for value in result.get('data').get('list'):
            # print(value)
            id.append(value.get('id'))

        id = random.choice(id)
        return id


if __name__ == '__main__':
    add = Classify()
    print(add.get_picture_id())