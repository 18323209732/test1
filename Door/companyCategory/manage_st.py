# coding=utf-8
import unittest
import traceback
import requests
from Common.FontColor import outcome
from Common.MyUnit import MyTest
from Common.ReadYaml import ConfigYaml
from Common.DataHandle import ReRun
import urllib3
from Door.companyCategory import Public
from ddt import ddt, data, unpack


@ddt  # 装饰测试类
class manage_companyCategory(MyTest):
    condition = True
    type_condition = False

    # 企业分类
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test01_add_companyCategory(self):
        # 添加“普通”企业下载分类，并从图片库选择图片，推广优化，html描述
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            Public.put_img()
            self.headers = Public.readconfig_ini(v=2)
            url = ConfigYaml(self.projectName).base_url + self.url
            imgurl = Public.readyaml(file=r'Door/companyCategory', key='p_url')
            imgId = Public.readyaml(file=r'Door/companyCategory', key='p_id')
            data = "id=0&type=1&parentId=&imgUrl=" + str(imgurl) + "&imgId=" + str(
                imgId) + "&newOpen=1&mobileNewOpen=1&showFlag=1&mobileShowFlag=1&linkUrl=&mobileLinkUrl=&iconUrl=&appId=24&name=%E4%BC%81%E4%B8%9A%E4%B8%8B%E8%BD%BD%E5%88%86%E7%B1%BB01&summaryCheck=&linkPath=&linkPathMobile=&des=123456789&mobileDes=&message=&keywords=&summary=&seoState=true&hidTitle=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22categoryName%22%7D%2C%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E4%B8%80%E7%BA%A7%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22oneCategoryName%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%5D&hidKeywords=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%85%B3%E9%94%AE%E8%AF%8D%22%2C%22id%22%3A%22categoryKeyword%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%5D&hidDescription=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22categoryName%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%2C%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E6%8F%8F%E8%BF%B0%22%2C%22id%22%3A%22categoryDescription%22%7D%5D&hidTitleSign=_&hidKeywordsSign=%2C&hidDescriptionSign=-&hidAddDescription=&seoTitleSign=_&seoKeywordsSign=%2C&seoDescriptionSign=-&seoTitle=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22categoryName%22%7D%2C%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E4%B8%80%E7%BA%A7%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22oneCategoryName%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%5D&seoKeywords=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%85%B3%E9%94%AE%E8%AF%8D%22%2C%22id%22%3A%22categoryKeyword%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%5D&seoDescription=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22categoryName%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%2C%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E6%8F%8F%E8%BF%B0%22%2C%22id%22%3A%22categoryDescription%22%7D%5D&seoAddDescription=&authData=%5B%7B%22authType%22%3A1%2C%22authStr%22%3A%22GW_%3A24%3Acategory%3Aview%3A%22%2C%22roleIds%22%3A%22%22%7D%5D&authStr=GW_%3A24%3Acategory%3Aview%3A&authType=1&roleIds=&"
            r = requests.post(url, headers=self.headers, data=data, stream=True, verify=False)
            self.result = r.json()
            # 把添加的企业下载分类id写入companyCategory的Public.yaml
            # print(self.result['data']['id'])
            Public.writeyaml(w_key='C_id', w_value=self.result['data']['id'], n='w', file=r'Door/companyCategory')
            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test02_add_Category(self):
        # 添加链接分类，并从图片库选择图片，推广优化，链接目标
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            self.headers = Public.readconfig_ini(v=2)
            url = ConfigYaml(self.projectName).base_url + self.url
            data ="id=0&type=2&parentId=&imgUrl=&imgId=&newOpen=1&mobileNewOpen=1&showFlag=1&mobileShowFlag=1&linkUrl=http%3A%2F%2Fwww.baidu.com&mobileLinkUrl=%7B%22text%22%3A%22%22%7D&iconUrl=&appId=24&name=%E9%93%BE%E6%8E%A5%E5%88%86%E7%B1%BB1&summaryCheck=&linkPath=&linkPathMobile=&des=&mobileDes=&message=&keywords=&summary=&seoState=true&hidTitle=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22categoryName%22%7D%2C%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E4%B8%80%E7%BA%A7%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22oneCategoryName%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%5D&hidKeywords=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%85%B3%E9%94%AE%E8%AF%8D%22%2C%22id%22%3A%22categoryKeyword%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%5D&hidDescription=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22categoryName%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%2C%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E6%8F%8F%E8%BF%B0%22%2C%22id%22%3A%22categoryDescription%22%7D%5D&hidTitleSign=_&hidKeywordsSign=%2C&hidDescriptionSign=-&hidAddDescription=&seoTitleSign=_&seoKeywordsSign=%2C&seoDescriptionSign=-&seoTitle=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22categoryName%22%7D%2C%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E4%B8%80%E7%BA%A7%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22oneCategoryName%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%5D&seoKeywords=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%85%B3%E9%94%AE%E8%AF%8D%22%2C%22id%22%3A%22categoryKeyword%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%5D&seoDescription=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22categoryName%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%2C%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E6%8F%8F%E8%BF%B0%22%2C%22id%22%3A%22categoryDescription%22%7D%5D&seoAddDescription=&authData=%5B%7B%22authType%22%3A1%2C%22authStr%22%3A%22GW_%3A24%3Acategory%3Aview%3A%22%2C%22roleIds%22%3A%22%22%7D%5D&authStr=GW_%3A24%3Acategory%3Aview%3A&authType=1&roleIds=&TOKEN=677e5175691c341942bee72da9e2e3dd67323b7081c847f1c4b442077c30332bacf101ca863f70f89644bcd86b7b99db6c2a03730ff5b1994ec925507b94e6647382579eb0bd853bb183a146932d58d07a42fd909ee8622cc0209e53fd2176b9a48f995ec268380a8c2743a6d993d34a5d251c4dc6ba9c5a330f2af294094032&"
            r = requests.post(url, headers=self.headers, data=data, stream=True, verify=False)
            self.result = r.json()
            # 把添加的企业下载分类id写入companyCategory的Public.yaml
            Public.writeyaml(w_key='L_id', w_value=self.result['data']['id'], n='a', file='Door/companyCategory')
            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test03_edit_companyCategory(self):
        # 编辑链接分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            self.headers = Public.readconfig_ini(v=2)
            url = ConfigYaml(self.projectName).base_url + self.url
            id = Public.readyaml(file=r'Door\companyCategory', key='C_id')
            data = "id="+str(id)+"&type=2&parentId=&imgUrl=&imgId=&newOpen=1&mobileNewOpen=1&showFlag=1&mobileShowFlag=1&linkUrl=http%3A%2F%2Fwww.baidu.com&mobileLinkUrl=%7B%22text%22%3A%22%22%7D&iconUrl=&appId=24&name=%E9%93%BE%E6%8E%A5%E5%88%86%E7%B1%BB1&summaryCheck=&linkPath=&linkPathMobile=&des=&mobileDes=&message=&keywords=&summary=&seoState=true&hidTitle=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22categoryName%22%7D%2C%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E4%B8%80%E7%BA%A7%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22oneCategoryName%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%5D&hidKeywords=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%85%B3%E9%94%AE%E8%AF%8D%22%2C%22id%22%3A%22categoryKeyword%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%5D&hidDescription=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22categoryName%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%2C%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E6%8F%8F%E8%BF%B0%22%2C%22id%22%3A%22categoryDescription%22%7D%5D&hidTitleSign=_&hidKeywordsSign=%2C&hidDescriptionSign=-&hidAddDescription=&seoTitleSign=_&seoKeywordsSign=%2C&seoDescriptionSign=-&seoTitle=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22categoryName%22%7D%2C%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E4%B8%80%E7%BA%A7%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22oneCategoryName%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%5D&seoKeywords=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%85%B3%E9%94%AE%E8%AF%8D%22%2C%22id%22%3A%22categoryKeyword%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%5D&seoDescription=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22categoryName%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%2C%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E6%8F%8F%E8%BF%B0%22%2C%22id%22%3A%22categoryDescription%22%7D%5D&seoAddDescription=&authData=%5B%7B%22authType%22%3A1%2C%22authStr%22%3A%22GW_%3A24%3Acategory%3Aview%3A%22%2C%22roleIds%22%3A%22%22%7D%5D&authStr=GW_%3A24%3Acategory%3Aview%3A&authType=1&roleIds=&TOKEN=677e5175691c341942bee72da9e2e3dd67323b7081c847f1c4b442077c30332bacf101ca863f70f89644bcd86b7b99db6c2a03730ff5b1994ec925507b94e6647382579eb0bd853bb183a146932d58d07a42fd909ee8622cc0209e53fd2176b9a48f995ec268380a8c2743a6d993d34a5d251c4dc6ba9c5a330f2af294094032&"
            r = requests.post(url, headers=self.headers, data=data, stream=True, verify=False)
            self.result = r.json()
            self.time = r.elapsed.total_seconds()

        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test04_update_CateStatus(self):
        # 隐藏/显示电脑版链接分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            self.headers = Public.readconfig_ini(v=2)
            self.data['cateId'] = Public.readyaml(file=r'Door\companyCategory', key='L_id')
            for i in [0, 1]:
                self.data['status'] = i
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
    def test05_checkout_CateStatus(self):
        # 查看链接分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            self.headers = Public.readconfig_ini(v=2)
            url = ConfigYaml(self.projectName).base_url + self.url
            id = Public.readyaml(file=r'Door\companyCategory', key='C_id')
            data = "appId=24&cateId=" + str(
                id) + "&pcStatus=-1&mobileStatus=-1&startDate=&endDate=&wd=&pageSize=15&currentPage=1&ec_s_title=&ec_s_categorys=&ec_s_pubDate=&ec_s_showFlag=&ec_s_showMobileFlag=&ec_s_viewcount=&orderColumn=&orderType=&"
            r = requests.post(url, headers=self.headers, data=data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test06_Cate_Tree(self):
        # 全部分类列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            self.headers = Public.readconfig_ini(v=2)
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()
            id1 = self.result['data'][0]['id']
            id2 = self.result['data'][1]['id']
            Public.writeyaml(w_key='id1', w_value=id1, n="a", file='Door/companyCategory')
            Public.writeyaml(w_key='id2', w_value=id2, n="a", file='Door/companyCategory')
            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test07_order_Cate(self):
        # 分类拖拽排序
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            self.headers = Public.readconfig_ini(v=2)
            url = ConfigYaml(self.projectName).base_url + self.url
            id1 = Public.readyaml(file=r'Door\companyCategory', key='id1')
            id2 = Public.readyaml(file=r'Door\companyCategory', key='id2')
            data = "cateId=" + str(id2) + "&targetId=" + str(id1) + "&targetPos=below&"
            r = requests.post(url, headers=self.headers, data=data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过"
    @ReRun(MyTest.setUp)
    def test08_move_Cate(self):
        # 转移分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            self.headers = Public.readconfig_ini(v=2)
            url = ConfigYaml(self.projectName).base_url + self.url
            id1 = Public.readyaml(file=r'Door\companyCategory', key='id1')
            id2 = Public.readyaml(file=r'Door\companyCategory', key='id2')
            data = "toCateId=" + str(id1) + "&cateId=" + str(id2)
            r = requests.post(url, headers=self.headers, data=data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test09_update_CateStatus(self):
        # 隐藏/显示电脑版分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            self.headers = Public.readconfig_ini(v=2)
            self.data['cateId'] = Public.readyaml(file=r'Door\companyCategory', key='C_id')
            for i in [0, 1]:
                self.data['status'] = i
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
    def test10_delete_Cate(self):
        # 删除分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            self.headers = Public.readconfig_ini(v=2)
            id1 = Public.readyaml(file=r'Door\companyCategory', key='id2')
            url = ConfigYaml(self.projectName).base_url + self.url+'&cateId=%s' % id1
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test11_update_CateStatus(self):
        # 隐藏/显示移动版分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            self.headers = Public.readconfig_ini(v=2)
            self.data['cateId'] = Public.readyaml(file=r'Door\companyCategory', key='C_id')
            for i in [0, 1]:
                self.data['status'] = i
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
    def test12_update_CateStatus(self):
        # 隐藏电脑版链接分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            self.data['cateId'] = Public.readyaml(file=r'Door\companyCategory', key='C_id')
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
