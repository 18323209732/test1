
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

        self.type = ConfigYaml('type_key').base_config
        self.form_type = ConfigYaml('form_type').base_config
        self.cookies_key = ConfigYaml('cookies').base_config
        self.cookies_value = ReadWrite(sign='session', option='cookies').read_ini_cookies()
        self.headers = {self.type: self.form_type}
        self.headers.update({self.cookies_key: self.cookies_value})
        self.projectName = ConfigYaml("projectName").base_config
        self.url = ConfigYaml(projectName).base_url
        self.tenant_value = ConfigYaml('tenant_value').base_config

    def add_attribute(self):
        '''
        添加属性类型
        :return: 属性类型id
        '''
        self.public_data = ReadPublic(catalog='attribute', key="add_attribute")
        url = self.public_data.public_value("url")
        url = self.url + url + "?tenantId={}".format(self.tenant_value) + '&authPermission=attribute_add'
        data = self.public_data.public_value("bar")
        data['templateName'] = 'FK自动{}'.format(time.time())
        self.headers['Content-Type'] = 'application/json'
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
        result = r.json()
        if result.get('status') == 200:
            return result['data']['templateId']

    def get_attribute(self, swich=False):
        '''
        获取属性管理列表数据
        :return:
        '''
        self.public_data = ReadPublic(catalog='attribute', key="get_attribute")
        url = self.public_data.public_value("url")
        url = self.url + url + "?tenantId={}".format(self.tenant_value) +'&appId=2&ec_p=1&ec_crd=15&startDate=&endDate=&sortField=&sortType='
        data = self.public_data.public_value("bar")
        r = requests.get(url, headers=self.headers, json=data, stream=True, verify=False)
        result = r.json()
        name = []
        id = []
        if result.get('status')==200:
            if swich:
                for value in result.get('data').get('list'):
                    if value.get('id') != 1:
                        name.append(value.get('templateName'))
                return name
            else:
                for value in result.get('data').get('list'):
                    if value.get('id') != 1:
                        id.append(value.get('id'))
                if id is None:
                    return self.add_attribute()
                else:
                    return id



if __name__ == '__main__':
    p =  Public_Data()

    # print(p.get_attribute())
