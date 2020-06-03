# coding=utf-8
import unittest
import traceback
import requests
from Common.FontColor import outcome
from Common.MyUnit import MyTest
from Common.ReadYaml import ConfigYaml
from Common.DataHandle import ReRun
import urllib3
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class manage_productCategory(MyTest):

    condition = True
    # 添加产品分类,然后获取分类列表，验证创建分类是否存在

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_add_category(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        # 添加产品分类
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            self.data['category']['categoryName'] = '分类%s' %time.time()  # 获取随机分类名称
            print(self.data['category']['categoryName'])
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time=r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_category_list(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        # 获取产品分类列表
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time=r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular
        