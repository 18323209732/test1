
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
        self.tenant_value = ConfigYaml('tenant_value').base_config

    def add_classify(self):
        '''
        新建分类
        :return: 分类id
        '''
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
                if id is None:
                    return self.add_classify()
                else:
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
        self.tenant_value = ConfigYaml('tenant_value').base_config



    def hide_classify(self):
        '''
        隐藏分类
        :return: 隐藏分类的id
        '''
        id = Public_Data().add_classify() #新建分类id
        self.public_data = ReadPublic(catalog='classification', key="hide_classify")
        url = self.public_data.public_value("url")
        url = self.url + url + "?viewType=1&authPermission=classify_update&appId=2&id={}&status=1".format(id) + "&tenantId={}".format(self.tenant_value)
        data = self.public_data.public_value("bar")

        r = requests.get(url, headers=self.headers, data=data, stream=True, verify=False)
        result = r.json()

        return id

if __name__ == '__main__':
    # p = Public_Data()
    # ret = p.get_classification(swich=False)
    # print(ret)
    addd = Classify()
    id = addd.hide_classify()
    print(id)
    # print(id)