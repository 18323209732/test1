# coding=utf-8
import unittest
import traceback
import requests
from Common.FontColor import outcome
from Common.MyUnit import MyTest
from Common.ReadYaml import ConfigYaml
from Common.DataHandle import ReRun
import urllib3
from Door.classes.Public import Public_path, print_debug_info
from Common.RWyaml import RWyaml
import time

class info_classes(MyTest):

    condition = True
    type_condition = False
    # 分类管理
    
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_all_classlist(self):
        # 全部分类列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            # print(r.json())
            i = r.json()['data'][-1]
            RWyaml(Public_path()).write_yaml('class', 'id', i['id'])  # 标记id存入public.yaml文件

            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular
        
    
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_delete_class(self):
        # 删除分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data["id"] = RWyaml(Public_path()).read_yaml_value('class', 'id')  # 读取yaml文件id
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
            outcome('red',self.singular)
            return self.singular
        
    
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_add_class(self):
        # 新增分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['category']['categoryName'] = ("接口新增分类" + str(time.time())[:10])  # 拼接产品名称
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
            outcome('red',self.singular)
            return self.singular
        