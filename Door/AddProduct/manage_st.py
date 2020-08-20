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
from Door.AddProduct.Public import readyaml, writeyaml, GetAll
from Door.news.Public import Public_Data
import warnings

warnings.simplefilter("ignore", ResourceWarning)


class manage_AddProduct(MyTest):
    condition = True
    # 保存产品
    type_condition = False

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test01_add_product(self):
        # 添加产品
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            # 自定义产品名称
            self.data['productInformation']['productName'] = '我的产品%s' % time.time()
            # 设置上传时间为当前时间
            self.data['productInformation']['publishTime'] = time.strftime("%Y-%m-%d %H:%M", time.localtime())
            # 读取产品分类里的id，把获取到的分类id，自定义的产品名称 传参。
            value = readyaml(file='Door\AddCategory', key='id')
            self.data['categoryIds'] = [value]
            # print(self.data)
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()
            # print(self.result)

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test02_choice_skuList(self):
        # 添加规格值货品信息
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            # 自定义产品名称
            self.data['productInformation']['productName'] = '我的产品%s' % time.time()
            # 设置上传时间为当前时间
            self.data['productInformation']['publishTime'] = time.strftime("%Y-%m-%d %H:%M", time.localtime())
            # 读取产品分类里的id，把获取到的分类id，自定义的产品名称 传参。
            value = readyaml(file='Door\AddCategory', key='id')
            self.data['categoryIds'] = [value]
            # 获取属性列表及规格、规格值、启用货品,货品sku编码固定为110
            attribute_id, s_id, specName, value_id, specValueName = GetAll().get_attribute()
            self.data['skuList'] = [
                {"id": "", "code": "110", "price": 0, "retailPrice": 0, "stock": 0, "moq": 1, "deliveryTime": "",
                 "weight": 0, "chargedWeight": 0, "status": 1, "isDefault": 1, "name": "", "productId": "",
                 "templateId": 8, "productSkuSpecs": [
                    {"productId": "", "specId": s_id, "specValueId": value_id, "name": specValueName,
                     "specName": specName, "skuId": ""}]}]
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()
            writeyaml(file="Door\AddProduct", w_key="productName",
                      w_value=self.data['productInformation']['productName'], n="w")

            self.time = r.elapsed.total_seconds()

        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test03_put_img(self):
        # 添加图片
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            # 自定义产品名称
            self.data['productInformation']['productName'] = '我的产品%s' % time.time()
            # 设置上传时间为当前时间
            self.data['productInformation']['publishTime'] = time.strftime("%Y-%m-%d %H:%M", time.localtime())
            # 读取产品分类里的id，把获取到的分类id，自定义的产品名称 传参。
            value = readyaml(file='Door\AddCategory', key='id')
            self.data['categoryIds'] = [value]

            # 获取素材库图片，上传本地图片，从素材库选择本地图片，并设置成封面第一张
            GetAll().put_img()
            imgId = readyaml(file='Door\AddProduct', key='p_id')
            url1 = readyaml(file='Door\AddProduct', key='p_url')
            imageName = readyaml(file='Door\AddProduct', key='p_name')
            self.data['productImageList'] = [
                {"imgId": imgId, "url": url1, "thumbId": imgId, "thumbUrl": url1, "imageName": imageName, "iscover": 1,
                 "sequence": "", "height": "", "wide": ""}]
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test04_product_list(self):
        # 产品列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()
            list = self.result['data']['list']
            id1 = list[0]['id']
            writeyaml(file='Door/AddProduct', w_key='product_id', w_value=id1, n="a")


            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test05_news_list(self):
        # 相关内容获取新闻资讯
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            # 自定义产品名称
            self.data['productInformation']['productName'] = '我的产品%s' % time.time()
            # 设置上传时间为当前时间
            self.data['productInformation']['publishTime'] = time.strftime("%Y-%m-%d %H:%M", time.localtime())
            # 读取产品分类里的id，把获取到的分类id，自定义的产品名称 传参。
            value = readyaml(file='Door\AddCategory', key='id')
            self.data['categoryIds'] = [value]

            # 获取新闻资讯id
            news_id = Public_Data().get_news_id(value='id')
            self.data['relecontentList'][1]['contentList'] = [next(news_id)]
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()

        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test06_getSeoList(self):
        # 优化推广
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url + '&appId=2'
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test07_choiceshow(self):
        # 选择橱窗
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            # 自定义产品名称
            self.data['productInformation']['productName'] = '我的产品%s' % time.time()
            # 设置上传时间为当前时间
            self.data['productInformation']['publishTime'] = time.strftime("%Y-%m-%d %H:%M", time.localtime())
            # 读取产品分类里的id，把获取到的分类id，自定义的产品名称 传参。
            value = readyaml(file='Door\AddCategory', key='id')
            self.data['categoryIds'] = [value]
            # 获取橱窗id
            self.data['showcaseIds'] = GetAll().showlist()
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test08_choicemark(self):
        # 选择标记
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            # 自定义产品名称
            self.data['productInformation']['productName'] = '我的产品%s' % time.time()
            # 设置上传时间为当前时间
            self.data['productInformation']['publishTime'] = time.strftime("%Y-%m-%d %H:%M", time.localtime())
            # 读取产品分类里的id，把获取到的分类id，自定义的产品名称 传参。
            value = readyaml(file='Door\AddCategory', key='id')
            self.data['categoryIds'] = [value]
            # 获取标记id
            self.data['markIds'] = [GetAll().get_mark()]
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()
            # print(self.result)

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test09_editor(self):
        # 编辑库存和价格
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            self.data['productInformation']['publishTime'] = time.strftime("%Y-%m-%d %H:%M", time.localtime())
            self.data['productInformation']['id'] = readyaml(file="Door\AddProduct", key='product_id')
            self.data['productBigField']['productId'] = readyaml(file="Door\AddProduct", key='product_id')
            self.data['productBigField']['productName'] = readyaml(file="Door\AddProduct", key='productName')
            self.data['categoryList'][0]['id'] = readyaml(file='Door\AddCategory', key='id')
            self.data['categoryList'][0]['categoryName'] = readyaml(file="Door\AddCategory", key='productName')
            self.data['productInformation']['price'] = 8000
            self.data['productInformation']['retailPrice'] = 7000
            self.data['productInformation']['stock'] = 50
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test10_close_sku(self):
        # 批量/隐藏货品
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            self.data['productInformation']['publishTime'] = time.strftime("%Y-%m-%d %H:%M", time.localtime())
            self.data['productInformation']['id'] = readyaml(file="Door\AddProduct", key='product_id')
            self.data['productBigField']['productId'] = readyaml(file="Door\AddProduct", key='product_id')
            self.data['productBigField']['productName'] = readyaml(file="Door\AddProduct", key='productName')
            self.data['categoryList'][0]['id'] = readyaml(file='Door\AddCategory', key='id')
            self.data['categoryList'][0]['categoryName'] = readyaml(file="Door\AddCategory", key='productName')

            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test11_order_Product(self):
        # 拖拽产品排序
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            # 颠倒前两个产品id顺序
            id1, id2 = GetAll().get_list()
            self.data['scopeIDs'] = id2, id1
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test12_delete_Product(self):
        # 删除编辑过的产品
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url + '&authPermission=product_del&appId=2&ids=%s' % (
                readyaml(file="Door\AddProduct", key='product_id'))
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()
            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
