# coding=utf-8
import unittest
import traceback
import requests
from Common.FontColor import outcome
from Common.MyUnit import MyTest
from Common.ReadYaml import ConfigYaml
from Common.DataHandle import ReRun
import random
import urllib3


class add_attribute(MyTest):
    condition = True
    # 添加属性

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_add_attribute(self):
        # 添加属性类型
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            num = random.randint(0, 1000)
            self.data['templateName'] = '自动%d' % num
            r = requests.post(url, headers=self.headers, json=self.data, stream=True,verify = False)
            self.result = r.json()
            print("templateId:::",self.result['data']['templateId'])

            self.time=r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular


    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_attribute_list(self):
        # 属性类型列表
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify = False)
            print("jieguo:",r)
            self.result = r.json()
            global list_num
            list_num = []
            for i in self.result['data']['list']:
                id = i['id']
                list_num.append(id)

            self.time=r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular


    # # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_edit_attribute(self):
        # 编辑属性类型
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify = False)
            self.result = r.json()

            self.time=r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_edit_attribute_pre(self):
        # 编辑属性类型后保存
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            num = random.randint(0,10000)
            self.data['templateName'] = '默认属性类型%d'%num
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify = False)
            self.result = r.json()

            self.time=r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_attribute_copy(self):
        # 复制属性类型
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time=r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_attribute_delete(self):
        # 删除属性类型
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time=r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular
        