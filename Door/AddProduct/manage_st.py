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
from Door.AddProduct.Public import readyaml, writeyaml


class manage_AddProduct(MyTest):

    condition = True
    # 保存产品

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test01_add_product(self):
        # 获取所属分类，添加产品
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            self.data['productInformation']['productName'] = '我的产品%s' % time.time()
            value = readyaml(file='AddCategory', key='id')  # 读取产品分类里的id，添加商品选择此分类。
            self.data['categoryIds'] = [value]  # 把获取到的分类id，自定义的产品名称 传参
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()
            # 把添加成功的产品名称写入Public.yaml
            writeyaml(w_key='productName', w_value=self.data['productInformation']['productName'], n="a")

            # 获取属性列表及规格、规格值

            # 获取素材库图片，上传本地图片，从素材库选择本地图片，并设置成封面第一张

            # 获取橱窗列表、选择橱窗

            # 获取标记列表、选择标记

            # 启用货品、禁用货品生成产品后，查看货品信息；批量启用、禁用货品

            # 相关内容，添加选择新闻资讯应用

            # 获取高级设置里的getSeoList

            # 打开权限设置


            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test02_attribute_list(self):
        # ?????????
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular





    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test03_product_list(self):
        # 产品列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()
            print(self.result)
            self.time = r.elapsed.total_seconds()
            # 删除产品、批量删除

            # 拖拽排序、批量拖拽

            # 批量编辑价格

            # 批量编辑库存

            # 关闭规格列表验证返回值


        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        


        


        


