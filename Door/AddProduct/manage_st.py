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
from Door.AddProduct.Public import readyaml, writeyaml,GetAll


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
            value = readyaml(file='AddCategory', key='id')
            self.data['categoryIds'] = [value]
            # print(self.data)
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()
            # print(self.result)
            # 把添加成功的产品名称写入Public.yaml
            writeyaml(w_key='productName', w_value=self.data['productInformation']['productName'], n="w")
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
            value = readyaml(file='AddCategory', key='id')
            self.data['categoryIds'] = [value]
            # 获取属性列表及规格、规格值、启用货品,货品sku编码固定为110
            attribute_id,s_id,specName,value_id,specValueName = GetAll().get_attribute()
            self.data['skuList'] = [{"id":"","code":"110","price":0,"retailPrice":0,"stock":0,"moq":1,"deliveryTime":"","weight":0,"chargedWeight":0,"status":1,"isDefault":1,"name":"","productId":"","templateId":8,"productSkuSpecs":[{"productId":"","specId":s_id,"specValueId":value_id,"name":specValueName,"specName":specName,"skuId":""}]}]
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

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
            value = readyaml(file='AddCategory', key='id')
            self.data['categoryIds'] = [value]


            # 获取素材库图片，上传本地图片，从素材库选择本地图片，并设置成封面第一张
            GetAll().put_img()
            imgId = readyaml(file='AddProduct', key='p_id')
            url1 = readyaml(file='AddProduct', key='p_url')
            imageName = readyaml(file='AddProduct', key='p_name')
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
    def test03_product_list(self):
        # 产品列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
# 获取橱窗列表、选择橱窗

# 获取标记列表、选择标记

# 禁用货品生成产品后，查看货品信息；批量启用、禁用货品

# 相关内容，添加选择新闻资讯应用

# 获取高级设置里的getSeoList

# 打开权限设置
# 删除产品、批量删除

# 拖拽排序、批量拖拽

# 批量编辑价格

# 批量编辑库存

# 关闭规格列表验证返回值
# current_path= 'E:\Automate\Portal_interface\Door\AddProduct'

# runner = unittest.TextTestRunner(verbosity=1)
# for i in range(0):
#     discover = unittest.defaultTestLoader.discover(
#         current_path, pattern='*_st.py', top_level_dir=None
#     )
#     runner = unittest.TextTestRunner(verbosity=1)
#     runner.run(discover)