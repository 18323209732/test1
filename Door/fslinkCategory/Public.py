
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
        r = requests.get(url, headers=self.headers, stream=True, verify=False)
        result = r.json()
        id_list = []
        if result['status'] == 200:
            if result.get('data').get('list') != []:
                for list in result.get('data').get('list'):
                    id_list.append(list.get('id'))
                return id_list
            else:
                id_list.append(self.add_classify())
                return id_list


class EnvData_Category:
    pass


get_classify = Classify()
if __name__ == '__main__':
    print(random.choice(get_classify.get_classify_list()))