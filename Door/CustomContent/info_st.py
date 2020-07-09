# coding=utf-8
import unittest
import traceback
import requests
import time,datetime
from Common.FontColor import outcome
from Common.MyUnit import MyTest
from Common.ReadYaml import ConfigYaml
from Common.DataHandle import ReRun
from Common.PrintDebug import print_debug_info
from Common.RWYaml import RWYaml
from Common.Route import Any_Path
import urllib3


class info_CustomContent(MyTest):

    condition = True
    type_condition = False
    Public_path = Any_Path('Door\\CustomContent', 'Public.yaml')
    # 自定义内容
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_all_CustomContent(self):
        # 全部自定义内容列表页
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            number = r.json()['data']['totalCount']
            RWYaml(self.Public_path).write_yaml('CustomContent', 'number', number)  # 存入列表总数
            if r.json()['data']['pres'] != []:
                n = 1
                for i in r.json()['data']['pres']:
                    RWYaml(self.Public_path).write_yaml('CustomContent', 'id' + str(n), i['id'])  # 存入id值
                    n += 1
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_add_CustomContent(self):
        # 新增自定义内容
        for i in range(1):
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            self.data['complaintPageContent']['title'] = '新增' + str(time.time())[:10]
            try:
                if self.type_condition:
                    self.headers[self.type] = self.form_type

                url = ConfigYaml(self.projectName).base_url + self.url
                r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
                self.result = r.json()

                self.time = r.elapsed.total_seconds()
                print_debug_info('--->pass')
            except:
                self.singular = str(traceback.format_exc())
                outcome('red', self.singular)
                return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_edit_CustomContent(self):
        # 编辑自定义内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['complaintPageContent']['id'] = RWYaml(self.Public_path).read_yaml_value('CustomContent', 'id1')
        self.data['complaintPageContent']['title'] = '编辑' + str(time.time())[:10]
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_zdelete_CustomContent(self):
        # 删除自定义内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['ids'] = RWYaml(self.Public_path).read_yaml_value('CustomContent', 'id1')
        try:
            if self.type_condition:

                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_hide_CustomContent(self):
        # 隐藏自定义内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['id'] = RWYaml(self.Public_path).read_yaml_value('CustomContent', 'id1')
        self.type_condition = True
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_show_CustomContent(self):
        # 显示自定义内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['id'] = RWYaml(self.Public_path).read_yaml_value('CustomContent', 'id1')
        self.type_condition = True
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_flip_over_CustomContent(self):
        # 翻页
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        number = RWYaml(self.Public_path).read_yaml_value('CustomContent', 'number')
        if int(number) > 15:
            self.data['currentPage'] = 2    # 列表数量大于15就翻页
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_time_find_CustomContent(self):
        # 日期搜索
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['beginDate'] = str(datetime.datetime.now())[:10]   # 当前日期
        self.data['endDate'] = str(datetime.datetime.now())[:10]     # 当前日期
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_title_find_CustomContent(self):
        # 标题搜索
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['keywords'] = '新增'
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_pull_find_CustomContent(self):
        # 电脑版下拉搜索
        import random
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['isdisplay'] = str(random.sample([-1, 0, 1], 1))   # 随机取值

        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        