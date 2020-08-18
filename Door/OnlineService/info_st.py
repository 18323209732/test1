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


class info_OnlineService(MyTest):

    condition = True
    type_condition = False
    Public_path = Any_Path('Door\\OnlineService', 'Public.yaml')
    # 在线客服
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_all_group_onlineservice(self):
        # 基本设置页获取列表组
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            if r.json()['data']['list'] != []:
                RWYaml(self.Public_path).write_yaml('data', 'list', r.json()['data']['list'])
                n = 1
                for i in r.json()['data']['list']:
                    RWYaml(self.Public_path).write_yaml('group', 'id'+str(n), i['id'])      # 写入组id
                    # n += 1
                    l = []
                    if i['staff'] != []:
                        for e in i['staff']:
                            l.append(e['id'])
                            RWYaml(self.Public_path).write_yaml('service', 'id' + str(n), l)  # 写入每组人员id
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
    def test_azll_service_onlineservice(self):
        # 基本设置页获取列表每组客服
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            if r.json()['data']['list'] != []:
                RWYaml(self.Public_path).write_yaml('data', 'list', r.json()['data']['list'])
                n = 1
                for i in r.json()['data']['list']:
                    RWYaml(self.Public_path).write_yaml('group', 'id'+str(n), i['id'])      # 写入组id
                    # n += 1
                    l = []
                    if i['staff'] != []:
                        for e in i['staff']:
                            l.append(e['id'])
                            RWYaml(self.Public_path).write_yaml('service', 'id' + str(n), l)  # 写入每组人员id
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
    def test_add_agroup_onlineservice(self):
        # 添加客服组
        for i in range(2):
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            self.data['name'] = '新增组' + str(time.time())[7:10]
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
    def test_azdd_service_onlineservice(self):
        # 添加客服人员
        for i in range(1):
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            self.data['name'] = '客服' + str(time.time())[7:10]
            self.data['ccount'] = str(time.time())[:10]
            self.data['groupId'] = RWYaml(self.Public_path).read_yaml_value('group', 'id1')
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
    def test_edit_agroup_onlineservice(self):
        # 编辑客服组
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['id'] = RWYaml(self.Public_path).read_yaml_value('group', 'id1')
        self.data['name'] = '编辑组' + str(time.time())[7:10]
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
    def test_edit_service_onlineservice(self):
        # 编辑客服人员
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['name'] = '编辑客服' + str(time.time())[7:10]
        self.data['groupId'] = RWYaml(self.Public_path).read_yaml_value('group', 'id1')
        self.data['id'] = RWYaml(self.Public_path).read_yaml_value('service', 'id1')[0]
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
    def test_off_service_onlineservice(self):
        # 停用客服人员
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['id'] = RWYaml(self.Public_path).read_yaml_value('service', 'id1')[0]
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
    def test_open_service_onlineservice(self):
        # 启用客服人员
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['id'] = RWYaml(self.Public_path).read_yaml_value('service', 'id1')[0]
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
    def test_zdelet_agroup_onlineservice(self):
        # 删除客服组
        for i in range(1, 3):
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            self.data['id'] = RWYaml(self.Public_path).read_yaml_value('group', 'id' + str(i))
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
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_ydelet_service_onlineservice(self):
        # 删除客服人员
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['id'] = RWYaml(self.Public_path).read_yaml_value('service', 'id1')
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

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_hotline_service_onlineservice(self):
        # 客服热线页
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
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
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_save_hotline_service_onlineservice(self):
        # 保存客服热线配置
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['telephone'] = '400-' + str(time.time())[2:10]
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
    def test_aydrag_service_onlineservice(self):
        # 拖拽客服组排序
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        data = RWYaml(self.Public_path).read_yaml_value('data', 'list')     # 读取列表数据
        # print(data)
        d1 = data[0]
        data[0] = data[1]
        data[1] = d1
        # print(data)
        self.type_condition = True
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            self.data['jsonData'] = str({"groups": data})
            # print(self.data)
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
