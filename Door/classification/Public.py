
# coding=utf-8
import requests
import time
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



    def get_classification(self, swich=True):
        '''
        获取分类管理列表数据
        :return:
        '''
        self.public_data = ReadPublic(catalog='classification', key="get_classification")
        url = self.public_data.public_value("url")
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.get(url, headers=self.headers, json=data, stream=True, verify=False)
        result = r.json()
        name = []
        id = []
        if result.get('status')==200:
            if swich:
                for value in result.get('data'):
                    name.append(value.get('categoryName'))
                return name
            else:
                for value in result.get('data'):
                    id.append(value.get('id'))

                return id

class Classify:

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

    def add_classify(self):
        self.public_data = ReadPublic(catalog='classification', key="add_classify")
        url = self.public_data.public_value("url")
        url = self.url + url
        data = self.public_data.public_value("bar")
        data['category']['categoryName'] = '接口分类{}'.format(time.time())

        self.headers['Content-Type'] = 'application/json;charset=UTF-8'
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
        result = r.json()
        if result.get('status')==200:
            id = result.get('data').get('id')

        return id

if __name__ == '__main__':
    # p = Public_Data()
    # ret = p.get_classification(swich=False)
    # print(ret)
    addd = Classify()
    id = addd.add_classify()
    print(id)