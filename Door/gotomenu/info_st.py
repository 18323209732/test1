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
from Common.RWyaml import RWyaml as RWYaml
from Common.Route import Any_Path
import urllib3


class info_gotomenu(MyTest):

    condition = True
    type_condition = False
    Public_path = Any_Path('Door\\gotomenu', 'Public.yaml')
    # 一键菜单
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_all_gotomenu(self):
        # 全部一键菜单列表页
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.type_condition = True
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            # print(r.json())
            RWYaml(self.Public_path).write_yaml('gotomenu', 'number', r.json()['data']['page']['total'])    # 存入菜单总数
            if r.json()['data']['list'] != []:
                n = 1
                for i in r.json()['data']['list']:
                    RWYaml(self.Public_path).write_yaml('gotomenu', 'id'+str(n), i['id'])   # 存入id值
                    n += 1
            else:
                print('列表为空，请先新增!')
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_add_gotomenu(self):
        # 添加一键菜单
        for i in range(1):
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            self.data['name'] = '接口新增' + str(time.time())[:10]
            # 拼接最新的按钮参数
            dict1 = RWYaml(self.Public_path).read_yaml_all()['button']
            value = dict1.values()
            list1 = []
            for i in value:
                list1.append({'moBtnId': i, "showFlag": 'true'})
            self.data['btnRelations'] = list1
            try:
                if self.type_condition:
                    self.headers[self.type] = self.form_type

                url = ConfigYaml(self.projectName).base_url + self.url
                r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
                # print(r.json())
                self.result = r.json()

                self.time = r.elapsed.total_seconds()
                print_debug_info('--->pass')
            except:
                self.singular = str(traceback.format_exc())
                outcome('red', self.singular)
                return self.singular
        
    @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_zdelete_gotomenu(self):
        # 删除一键菜单
        for i in range(1,2):
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            self.data['ids'] = RWYaml(self.Public_path).read_yaml_value('gotomenu', 'id'+str(i))
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
    def test_edit_gotomenu(self):
        # 编辑一键菜单
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['id'] = RWYaml(self.Public_path).read_yaml_value('gotomenu', 'id1')
        self.data['name'] = '接口编辑' + str(time.time())[:10]
        # 拼接最新的按钮参数
        dict1 = RWYaml(self.Public_path).read_yaml_all()['button']
        value = dict1.values()
        list1 = []
        for i in value:
            list1.append({'moBtnId': i, "showFlag": 'true'})
        self.data['btnRelations'] = list1
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
    def test_hide_gotomenu(self):
        # 隐藏一键菜单
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['ids'] = RWYaml(self.Public_path).read_yaml_value('gotomenu', 'id1')
        self.type_condition = True
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            # print(r.json())
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_show_gotomenu(self):
        # 显示一键菜单
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['ids'] = RWYaml(self.Public_path).read_yaml_value('gotomenu', 'id1')
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
    def test_find_gotomenu(self):
        # 筛选一键菜单列表页
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['startDate'] = str(datetime.datetime.now())[:10]  # 筛选开始时间
        self.data['endDate'] = str(datetime.datetime.now())[:10]    #筛选结束时间
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            # print(r.json()['data']['list'])
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_flip_over_gotomenu(self):
        # 翻页
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        number = RWYaml(self.Public_path).read_yaml_value('gotomenu', 'number')
        if int(number) > 15:
            self.data['currentPage'] = 2
        self.type_condition = True
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            # print(r.json()['data']['list'][0]['id'])
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_aadd_button_gotomenu(self):
        # 添加按钮
        for i in range(2):
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            self.data['alias'] = '添加按钮' + str(time.time())[:10]
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
    def test_aall_button_gotomenu(self):
        # 全部按钮列表页
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.type_condition = True
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            RWYaml(self.Public_path).write_yaml('button_number', 'number', r.json()['data']['page']['total'])
            n = 1
            for i in r.json()['data']['list']:
                RWYaml(self.Public_path).write_yaml('button', 'button_id'+str(n), i['id'])
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
    def test_edit_button_gotomenu(self):
        # 编辑按钮
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['id'] = RWYaml(self.Public_path).read_yaml_value('button', 'button_id1')
        self.data['alias'] = '编辑按钮' + str(time.time())[:10]
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
    def test_zdelete_button_gotomenu(self):
        # 删除按钮
        for i in range(2):
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            self.data['ids'] = RWYaml(self.Public_path).read_yaml_value('button', 'button_id'+str(i+1))
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
    def test_drag_button_gotomenu(self):
        # 拖拽按钮排序
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['sectionIds'] = RWYaml(self.Public_path).read_yaml_value('button', 'button_id1')
        self.data['targetId'] = RWYaml(self.Public_path).read_yaml_value('button', 'button_id2')
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
    def test_flip_over_button_gotomenu(self):
        # 翻页
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        number = RWYaml(self.Public_path).read_yaml_value('button_number', 'number')
        if int(number) > 15:
            self.data['currentPage'] = 2
        self.type_condition = True
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
        