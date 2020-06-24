# coding=utf-8
import unittest
import traceback
import requests
from Common.FontColor import outcome
from Common.MyUnit import MyTest
from Common.ReadYaml import ConfigYaml
from Common.DataHandle import ReRun
import urllib3, time
from Door.listShowcase.Public import readyaml,writeyaml,GetAll,readconfig_ini,readyaml_case


class manage_listShowcase(MyTest):

    condition = True
    type_condition = True
    # 橱窗管理
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test01_add_listShowcase(self):
        # 添加/编辑橱窗
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            for i, y in [('1', 'w'), ('2', 'a')]:
                self.data['showcaseName'] = '橱窗%s号' %i
                self.data['showcaseId'] = ''
                r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
                self.result = r.json()
                # print(self.result)
                writeyaml(w_key=self.result['data']['showcaseName'], w_value=self.result['data']['id'], n=y)
                self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test02_listShowcase(self):

        # 橱窗列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url+'&ec_crd=15&ec_p=1&appId=2'
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    #@unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test03_keywords_listShowcase(self):
        # 筛选橱窗
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url+\
                  '&ec_crd=15&ec_p=1&appId=2&keywords=01&startDate=2020-06-17+00:00&endDate=%s+23:59' % time.strftime("%Y-%m-%d", time.localtime())
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            return self.url
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    #@unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test04_saveProductShowcaseRelation(self):
        # 橱窗选择产品
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            proIds = GetAll().get_product_attribute()
            caseId = readyaml(file='listShowcase', key='橱窗1号')
            url = ConfigYaml(self.projectName).base_url + self.url + '&appId=2&proIds=%s&caseId=%s' % (proIds,caseId)
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()
            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    #@unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test05_ShowcaseRelation(self):
        # 选择/批量选择橱窗
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            proIds = GetAll().get_product_list()
            caseId = readyaml(file='listShowcase', key='橱窗1号')
            url = ConfigYaml(self.projectName).base_url + self.url +'&appId=2&proids=%s&caseids=%s' % (proIds,caseId)
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()
            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test06_delProduct(self):
        # 橱窗批量/移除产品
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            proIds = GetAll().get_product_list()
            caseId = readyaml(file='listShowcase', key='橱窗1号')
            url = ConfigYaml(self.projectName).base_url + self.url
            self.data['ids'] = proIds
            self.data['showcaseId'] = caseId
            headers = readconfig_ini(v=False)
            r = requests.post(url, headers=headers, data=self.data, stream=True, verify=False)
            self.result = r.json()
            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    #@unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test07_Productlist(self):
        # 筛选并搜索橱窗里显示的产品列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            self.data["showCaseId"] = readyaml(file='listShowcase', key='橱窗1号')
            url = ConfigYaml(self.projectName).base_url + self.url
            headers = readconfig_ini()
            r = requests.post(url, headers=headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test08_delete(self):
        # 筛选并搜索橱窗里显示的产品列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            # 获取橱窗列表所有数据，找出没有产品的橱窗，并删除
            url = ConfigYaml(self.projectName).base_url + readyaml_case() + '?ec_crd=15&ec_p=1&appId=2'
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()
            productNum = self.result['data']['list']
            for i in productNum:
                if i['productNum'] == 0:
                    idd = i['id']
                    # 删除没有产品的橱窗
                    self.data['id'] = idd
                    url = ConfigYaml(self.projectName).base_url + self.url
                    r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
                    self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        