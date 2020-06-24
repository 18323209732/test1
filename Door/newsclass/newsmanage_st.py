# coding=utf-8
import unittest
import traceback
import requests
from random import choice
from Common.CusMethod import random_str
from Common.FontColor import outcome
from Common.MyUnit import MyTest
from Common.ReadYaml import ConfigYaml
from Common.DataHandle import ReRun
import urllib3
from Door.news.Public import Public_Data as pub_news
from Door.newsclass.Public import Public_Data as pd


class newsmanage_newsclass(MyTest):

    condition = True
    type_condition = True
    # 新闻分类管理
    # @unittest.skipIf(condition, "暂时跳过")

    @ReRun(MyTest.setUp)
    def test_list_news(self):
        # “分类管理”页面列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
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
    def test_edit_newsclass(self):
        # 编辑分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            self.data['id'] = next(pd().get_classnews_id(value='id'))
            self.data['name'] = random_str("自动化新增分类...")
            self.data['des'] = random_str("<p>自动化新增分类描述数据...</p>\n")

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
    def test_add_newsclass(self):
        # 添加分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            img_url = next(pub_news().get_pictures(value='id'))
            self.data['name'] = random_str("自动化新增分类...")
            self.data['des'] = random_str("<p>自动化新增分类描述数据...</p>\n")
            self.data['imgUrl'] = img_url
            self.data['imgThumbUrl'] = img_url
            self.data['summary'] = random_str("自动化新增分类来源数据...")
            self.data['keywords'] = random_str("关键词...")

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
    def test_cat_newsclass(self):
        # 查看分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_info_newsclass(self):
        # 查看关联资讯数据
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

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
    def test_info_page_newsclass(self):
        # 查看关联列表
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
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_tocustomsort_newsclass(self):
        # 查看关联列表
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
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_move_newsclass(self):
        # 转移分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            toCateId = next(pd().get_classnews_id(value='id'))
            cateId = next(pd().get_classnews_id(value='id'))

            url = ConfigYaml(self.projectName).base_url + self.url + f"&toCateId={toCateId}&cateId={cateId}"
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_pcstatus_newsclass(self):
        # 显示电脑版
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            cateId = next(pd().get_classnews_id(value='id'))

            url = ConfigYaml(self.projectName).base_url + self.url + f"&cateId={cateId}&status=1"
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_hidepcstatus_newsclass(self):
        # 显示电脑版
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            cateId = next(pd().get_classnews_id(value='id'))

            url = ConfigYaml(self.projectName).base_url + self.url + f"&cateId={cateId}&status=0"
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_delete_newsclass(self):
        # 删除
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            cateId = next(pd().get_classnews_id(value='id'))

            url = ConfigYaml(self.projectName).base_url + self.url + f"&cateId={cateId}"
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_sort_newsclass(self):
        # 添加分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            cateId = next(pd().get_classnews_id(value='id'))
            targetId = next(pd().get_classnews_id(value='id'))
            targetPos = choice(['before', 'below'])

            url = ConfigYaml(self.projectName).base_url + self.url + f"&cateId={cateId}&targetId={targetId}&targetPos={targetPos}"
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_addordinary_newsclass(self):
        # 添加普通分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            img_url = next(pub_news().get_pictures(value='imgUrl'))
            self.data['name'] = random_str("自动化新增普通分类...")
            self.data['des'] = random_str("<p>自动化新增普通分类描述数据...</p>\n")
            self.data['imgUrl'] = img_url
            self.data['imgThumbUrl'] = img_url
            self.data['summary'] = random_str("自动化新增普通分类来源数据...")
            self.data['keywords'] = random_str("关键词...")
                
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
    def test_addconnect_newsclass(self):
        # 添加普通分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            img_url = next(pub_news().get_pictures(value='imgUrl'))
            self.data['name'] = random_str("自动化新增连接分类...")
            self.data['des'] = random_str("<p>自动化新增连接分类描述数据...</p>\n")
            self.data['imgUrl'] = img_url
            self.data['imgThumbUrl'] = img_url
            self.data['summary'] = random_str("自动化新增连接分类来源数据...")
            self.data['keywords'] = random_str("关键词...")
                
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
    def test_picture_newsclass(self):
        # 获取分类图片
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url + "&currentPage=1&pageSize=15"
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_keyword_newsclass(self):
        # 自动获取关键词
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
                
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
    def test_getseolist_newsclass(self):
        # 推广优化
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
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
    def test_selectlink_newsclass(self):
        # 获取链接
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_savecontinue_newsclass(self):
        # 获取链接
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            img_url = next(pub_news().get_pictures(value='imgUrl'))
            self.data['name'] = random_str("自动化新增保存继续分类...")
            self.data['des'] = random_str("<p>自动化新增保存继续分类描述数据...</p>\n")
            self.data['imgUrl'] = img_url
            self.data['imgThumbUrl'] = img_url
            self.data['summary'] = random_str("自动化新增保存继续分类来源数据...")
            self.data['keywords'] = random_str("关键词...")
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        