
# coding=utf-8
import requests
from random import randint,choice
import random,os,re
import json
import requests
import time
import urllib3
from random import randint
from datetime import date,timedelta
from Common.ReadYaml import ReadPublic, ConfigYaml
from Common.ReadWriteIni import ReadWrite
projectName = ConfigYaml("projectName").base_config
Url = ConfigYaml(projectName).base_url

class Customer:

    def __init__(self):
        self.url = ConfigYaml(projectName).base_url
        self.cookies_value = ReadWrite(sign='session', option='cookies').read_ini_cookies()
        self.headers = {ConfigYaml('cookies').base_config:self.cookies_value}
        self.tenant_value = '?tenantId={}'.format(ConfigYaml('tenant_value').base_config)

    def get_group_list(self):
        '''
        根据添加的客户分组名称，获取分组id
        :return: 分组id
        '''
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        public_data = ReadPublic(catalog='customer_manage', key="get_group_list")
        url = self.url + public_data.public_value('url') + self.tenant_value
        data = public_data.public_value('bar')
        name = self.add_customergroup()
        self.headers['Content-Type'] = "application/x-www-form-urlencoded"
        r = requests.post(url, headers=self.headers, stream=True, verify=False)
        result = r.json()
        if result['status'] == 200:
            for data in result['data']['list']:
                if data['name'] == name:
                    return data['id']

    def add_customergroup(self):
        '''
        添加客户分组
        :return: 分组名称
        '''
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        public_data = ReadPublic(catalog='customer_manage', key="add_customergroup")
        url = self.url + public_data.public_value('url') + self.tenant_value
        data = public_data.public_value('bar')
        data['name'] = 'wode客户分组{}'.format(time.time())
        self.headers['Content-Type'] = "application/x-www-form-urlencoded"
        r = requests.post(url, headers=self.headers, data=data, stream=True, verify=False)
        result = r.json()
        if result['status'] == 200:
            return data['name']
