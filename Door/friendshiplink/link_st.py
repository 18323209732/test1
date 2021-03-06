# coding=utf-8
import unittest
import traceback
import requests
import random
from Common.FontColor import outcome
from Common.MyUnit import MyTest
from Common.ReadYaml import ConfigYaml
from Common.DataHandle import ReRun
import urllib3
import time
from Door.friendshiplink.Public import get_link,get_classify,EnvData

class link_friendshiplink(MyTest):

    condition = True
    type_condition = False
    # 友情链接
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_01_add_friendshiplink(self):
        # 添加链接
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            self.data['friendLink']['name'] = 'FK接口添加{}'.format(time.time())
            self.data['categoryIds'] = [random.choice(get_classify.get_classify_list())]
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_friendshiplink_list(self):
        # 链接列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url + '&categoryId=&state=2&mobileState=2&endDate=&startDate=&keywords=&ec_s_categorys=&ec_s_createDate=&ec_s_showFlag=&ec_s_mobileShowFlag=&ec_s_name=&currentPage=1&pageSize=15'
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_list_Search(self):
        # 列表搜索
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.type_condition = True
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            url = ConfigYaml(self.projectName).base_url + self.url + '&keywords={}'.format(1)
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_list_sort(self):
        # 列表排序
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.type_condition = True
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            self.data['targetId'] = random.choice(get_link.get_list_id())
            self.data['sectionIds'] = get_link.add_friendshiplink_id()
            r = requests.post(url, headers=self.headers,data=self.data, stream=True,verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_edit_link(self):
        # 编辑
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            self.data['friendLink']['name'] = 'FK接口编辑{}'.format(time.time())
            self.data['friendLink']['id'] = random.choice(get_link.get_list_id())
            self.data['categoryIds'] = [random.choice(get_classify.get_classify_list())]
            print(self.data)
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()
            print(self.result)

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_transfer_link(self):
        # 转移
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.type_condition = True
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            self.data['ids'] = random.choice(get_link.get_list_id())
            self.data['categoryIds'] = random.choice(get_classify.get_classify_list())
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_01_updateShowState(self):
        # 隐藏电脑版
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.type_condition = True
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            self.data['ids'] = random.choice(get_link.get_list_id())
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()
            setattr(EnvData,"hide_id",self.data['ids'])

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_display_updateShowState(self):
        # 显示电脑版
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.type_condition = True
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            self.data['ids'] = EnvData.hide_id
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_delete_friendshiplink(self):
        # 删除友情链接
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.type_condition = True
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            self.data['ids'] = random.choice(get_link.get_list_id())
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_batchdelete_friendshiplink(self):
        # 批量删除
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.type_condition = True
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            try:
                ids = random.sample(get_link.get_list_id(), 2)
            except ValueError:
                get_link.add_friendshiplink()
                ids = random.sample(get_link.get_list_id(), 2)
            self.data['ids'] = ids
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()
            print(self.result)

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_batch_updateShowState(self):
        # 批量隐藏电脑版
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.type_condition = True
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            try:
                ids = random.sample(get_link.get_list_id(), 3)
            except ValueError:
                get_link.add_friendshiplink()
                get_link.add_friendshiplink()
                ids = random.sample(get_link.get_list_id(), 3)
            self.data['ids'] = ids
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()
            setattr(EnvData,'ids',self.data['ids'])

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_batchdisplay_updateShowState(self):
        # 批量显示电脑版
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.type_condition = True
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            self.data['ids'] = EnvData.ids
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_batch_transfer(self):
        # 批量转移
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.type_condition = True
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            try:
                ids = random.sample(get_link.get_list_id(), 3)
            except ValueError:
                get_link.add_friendshiplink()
                get_link.add_friendshiplink()
                ids = random.sample(get_link.get_list_id(), 3)
            self.data['ids'] = ids
            self.data['categoryIds'] = get_classify.add_classify()
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_Turn_the_page(self):
        # 翻页
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.type_condition = True
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url + '&categoryId=&state=2&mobileState=2&endDate=&startDate=&keywords=&ec_s_categorys=&ec_s_createDate=&ec_s_showFlag=&ec_s_mobileShowFlag=&ec_s_name=&currentPage=2&pageSize=15'
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        