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
from Door.attribute.Public import list_num
import datetime

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
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

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
            self.headers['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8'
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify = False)
            self.result = r.json()

            self.time=r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular


    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_edit_attribute_pre(self):
        # 编辑属性类型
        try:
            id = random.choice(list_num)
            url = ConfigYaml(self.projectName).base_url + self.url
            num = random.randint(0,10000)
            self.data['templateName'] = '自动%d'%num
            self.data['id'] = id
            print('id--===：',self.data)
            print('url:::',url)
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify = False)
            self.result = r.json()
            print('rrrr-=:',self.result)

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
            id = random.choice(list_num)
            url = ConfigYaml(self.projectName).base_url + self.url.format(id)
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
            id = random.choice(list_num)
            url = ConfigYaml(self.projectName).base_url + self.url.format(id)
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time=r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular


    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_list_screen(self):
        # 列表筛选
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            start_today = datetime.date.today()  # 获取当前年月日
            offset = datetime.timedelta(days=-5)
            end_date = (start_today + offset).strftime('%Y-%m-%d')  # 获取当前日期前5天年月日

            url = ConfigYaml(self.projectName).base_url + self.url.format(end_date,start_today)
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time=r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular
        