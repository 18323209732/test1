# coding=utf-8
import unittest,os
import traceback
import requests
from Common.FontColor import outcome
from Common.MyUnit import MyTest
from Common.ReadYaml import ConfigYaml
from Common.DataHandle import ReRun
import urllib3
from Door.tab.Public import Public_path, print_debug_info
from Common.RWyaml import RWyaml
import time

class info_tab(MyTest):

    condition = True
    type_condition = False
    # 标记管理
    
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_all_tablist(self):
        # 全部标记列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            # for i in r.json()["data"]:
            #     if "接口新增标记" in i['markName']:
            #         RWyaml(Public_path()).write_yaml('tab', 'id', i['id'])  # 标记id存入public.yaml文件
            i = r.json()['data'][-1]
            RWyaml(Public_path()).write_yaml('tab', 'id', i['id'])  # 标记id存入public.yaml文件

            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular
        
    
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_add_tab_product(self):
        # 新增标记
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.type_condition = True
        self.data['markName'] = ("接口新增标记" + str(time.time())[:10])   # 拼接产品名称
        self.data['imageId'] = RWyaml(Public_path()).read_yaml_value('img', 'imageId')  # 读取yaml文件imageId
        self.data['imageurl'] = RWyaml(Public_path()).read_yaml_value('img', 'imageurl')  # 读取yaml文件imageurl
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
            outcome('red',self.singular)
            return self.singular
        
    
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_edit_tab(self):
        # 编辑标记
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['id'] = RWyaml(Public_path()).read_yaml_value('tab', 'id')  # 读取yaml文件id
        self.data["markName"] = ("接口编辑标记" + str(time.time())[:10])   # 拼接产品名称
        self.data['imageId'] = RWyaml(Public_path()).read_yaml_value('img', 'imageId')  # 读取yaml文件imageId
        self.data['imageurl'] = RWyaml(Public_path()).read_yaml_value('img', 'imageurl')  # 读取yaml文件imageurl
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
            outcome('red',self.singular)
            return self.singular
        
    
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_delete_tab(self):
        # 删除标记
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['id'] = RWyaml(Public_path()).read_yaml_value('tab', 'id')    # 读取yaml文件id
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
    def test_add_img_tab(self):
        # 上传照片
        # file_path = os.path.realpath('图片.jpg')
        file_path = "D:\Program Files\PycharmProjects\Portal_interface\Door\tab\图片.jpg"
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        file = {"file": ("图片.jpg", open(file_path, "rb"), "image/jpeg")}
        del self.headers['Content-Type']
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False, files=file)
            # print(r.json())
            RWyaml(Public_path()).write_yaml('img', 'imageId', r.json()['data']['fileID'])  # fileID存入public.yaml文件
            RWyaml(Public_path()).write_yaml('img', 'imageurl', r.json()['data']['imgUrl'])  # fileID存入public.yaml文件
            if r.json():
                self.result = {"status": 200}

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular
        