# coding=utf-8
import unittest
import traceback
import requests
from Common.FontColor import outcome
from Common.MyUnit import MyTest
from Common.ReadYaml import ConfigYaml
from Common.DataHandle import ReRun
import urllib3
import time, yaml, os
from ruamel.yaml import RoundTripDumper


class manage_AddProduct(MyTest):

    condition = True
    # 保存产品

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_add_product(self):
        # 添加产品
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            self.data['productInformation']['productName'] = '我的产品%s' % time.time()
            # 读取产品分类里的id，添加商品选择此分类。
            path = os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\productCategory\Public.yaml"
            with open(path, 'r', encoding='utf-8') as f:  # 读取productCategory\Public.yaml中'id'的值
                id = yaml.load(f.read(), Loader=yaml.Loader)['id']
            self.data['categoryIds'] = [id]

            # 把获取到的分类id，自定义的产品名称 传参
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()
            # 把添加成功的产品名称写入Public.yaml
            with open("Public.yaml", "a", encoding="utf-8") as yaml_file:
                data = {'productName': self.data['productInformation']['productName']}
                yaml.dump(data, yaml_file, Dumper=RoundTripDumper, allow_unicode=True)

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_product_list(self):
        # 产品列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()
            print(self.result)
            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        