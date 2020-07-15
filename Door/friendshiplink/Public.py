
# coding=utf-8
import requests
from random import randint,choice
import random,os,re
import json
import requests
import time
from random import randint
from datetime import date,timedelta
from Common.ReadYaml import ReadPublic, ConfigYaml
projectName = ConfigYaml("projectName").base_config
from Common.ReadWriteIni import ReadWrite

class Link:

    def __init__(self):
        self.url = ConfigYaml(projectName).base_url
        self.cookies_value = ReadWrite(sign='session', option='cookies').read_ini_cookies()
        self.headers = {ConfigYaml('cookies').base_config:self.cookies_value}
        self.tenant_value = '?tenantId={}'.format(ConfigYaml('tenant_value').base_config)


    def add_friendshiplink(self):
        public_data = ReadPublic(catalog='friendshiplink', key="add_friendshiplink")
        url = self.url + public_data.public_value('url') + self.tenant_value
        data = public_data.public_value('bar')
        data['friendLink']['name'] = 'FK接口添加{}'.format(time.time())
        r = requests.post(url,headers=self.headers,json=data, stream=True, verify=False)
        result = r.json()
        if result['status'] == 200:
            return data['friendLink']['name']

    def get_list_id(self,values=True):
        public_data = ReadPublic(catalog='friendshiplink', key="get_list_id")
        url = self.url + public_data.public_value('url') + self.tenant_value + '&categoryId=&state=2&mobileState=2&endDate=&startDate=&keywords=&ec_s_categorys=&ec_s_createDate=&ec_s_showFlag=&ec_s_mobileShowFlag=&ec_s_name=&currentPage=1&pageSize=15'
        data = public_data.public_value('bar')
        r = requests.get(url, headers=self.headers,data=data,stream=True,verify=False)
        result = r.json()
        dic = {}
        if result['status'] == 200:
            for i in result.get('data').get('list'):
                dic[i.get('name')] = i.get('id')
            if values:
                li = []
                for id in dic.values():
                    li.append(id)
                return li
            else:
                return dic

    def add_friendshiplink_id(self):
        key_name = self.add_friendshiplink()
        dic = self.get_list_id(values=False)
        return dic.get(key_name)

class Classify:

    def __init__(self):
        self.url = ConfigYaml(projectName).base_url
        self.cookies_value = ReadWrite(sign='session', option='cookies').read_ini_cookies()
        self.headers = {ConfigYaml('cookies').base_config:self.cookies_value}
        self.tenant_value = '?tenantId={}'.format(ConfigYaml('tenant_value').base_config)

    def add_classify(self):
        '''
        添加分类
        :return: 分类id
        '''
        public_data = ReadPublic(catalog='friendshiplink', key="add_classify")
        url = self.url + public_data.public_value('url') + self.tenant_value
        data = public_data.public_value('bar')
        data['name'] = '接口新增{}'.format(time.time())
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
        result = r.json()
        if result['status'] == 200:
            return result['data']['id']
    def get_classify_list(self):
        public_data = ReadPublic(catalog='friendshiplink', key="get_classify_list")
        url = self.url + public_data.public_value('url') + self.tenant_value + '&currentPage=1&pageSize=15'
        data = public_data.public_value('bar')
        r = requests.get(url, headers=self.headers, stream=True, verify=False)
        result = r.json()
        id_list = []
        if result['status'] == 200:
            if result.get('data').get('list') != []:
                for list in result.get('data').get('list'):
                    id_list.append(list.get('id'))
                return id_list
            else:
                print('-----N')
                id_list.append(self.add_classify())
                return id_list

get_link = Link()
get_classify = Classify()
if __name__ == '__main__':
    print(get_classify.add_classify())