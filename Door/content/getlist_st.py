# coding=utf-8
import unittest
import traceback, sys
import requests, time
from Common.FontColor import outcome
from Common.MyUnit import MyTest
from Common.ReadYaml import ConfigYaml
from Common.DataHandle import ReRun
import urllib3
from Common.generator import random_name, random_address
from Common.RWyaml import RWyaml
from Door.content.Public import print_debug_info
from Common.Route import Any_Path

class getlist_content(MyTest):
    condition = True
    Public_path = Any_Path('Door\\content', 'Public.yaml')
    # 介绍内容


    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_all_class_content(self):
        # 全部分类内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            title = r.json()['data']['list'][0]['title']  # 获取首个内容title
            RWyaml(self.Public_path).write_yaml('content', 'title', title)  # 内容title存入public.yaml文件
            n = 1
            for i in r.json()['data']['list']:
                # print(i['id'])
                RWyaml(self.Public_path).write_yaml('content', 'id'+str(n), i['id'])  # 内容id存入public.yaml文件
                n += 1
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_no_class_content(self):
        # 无分类内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_showpc_content(self):
        # 显示电脑版
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['id'] = RWyaml(self.Public_path).read_yaml_value('content', 'id1')  # 读取yaml文件内容id
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            # print(r.json())
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_hidepc_content(self):
        # 隐藏电脑版
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['id'] = RWyaml(self.Public_path).read_yaml_value('content', 'id1')  # 读取yaml文件内容id
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_add_content(self):
        # 新增分类内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data["introductionContent"]['title'] = ("接口新增内容" + str(time.time())[:10])  # 随机生成内容标题
        self.data["content"] = "接口新增内容"  # 随机生成详细介绍
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            # print(r.json())
            id = r.json()['data']
            RWyaml(self.Public_path).write_yaml('content', 'addid2', id[8:])  # 新增内容id存入public.yaml文件
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_ydel_content(self):
        # 删除分类内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.headers["Content-Type"] = "application/x-www-form-urlencoded;charset=UTF-8"  # 修改头部请求方式
        self.data["id"] = RWyaml(self.Public_path).read_yaml_value('content', 'id3')  # yaml文件读取删除id
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_search_content(self):
        # 搜索分类内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['keywords'] = RWyaml(self.Public_path).read_yaml_value('content', 'title')  # 读取yaml文件标题名
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_filter_content(self):
        # 筛选分类内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_page_content(self):
        # 翻页分类内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_drag_content(self):
        # 拖拽排序分类内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.headers["Content-Type"] = "application/x-www-form-urlencoded;charset=UTF-8"
        self.data['id'] = RWyaml(self.Public_path).read_yaml_value('content', 'id1')  # 拖拽内容id
        self.data['orderid'] = RWyaml(self.Public_path).read_yaml_value('content', 'id2')  # 拖拽到id
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_updata_content(self):
        # 编辑第一个分类内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['introductionContent']['title'] = ('接口编辑内容' + str(time.time())[:8])
        self.data['introductionContent']['id'] = RWyaml(self.Public_path).read_yaml_value('content', 'id1')
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            # print(r.json())
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_preview_content(self):
        # 预览分类内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.headers["Content-Type"] = "application/x-www-form-urlencoded;charset=UTF-8"  # 更新头部请求类型
        self.data['id'] = RWyaml(self.Public_path).read_yaml_value('content', 'id1')  # 读取yaml文件内容id
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_move_content(self):
        # 转移分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['id'] = RWyaml(self.Public_path).read_yaml_value('content', 'id1')  # 读取yaml文件内容id
        self.data['cateid'] = 2  # 转移分类的id
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_copy_content(self):
        # 复制分类内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['id'] = RWyaml(self.Public_path).read_yaml_value('content', 'id1')  # 读取yaml文件内容id
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_batch_move_content(self):
        # 批量转移分类内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        id1 = RWyaml(self.Public_path).read_yaml_value('content', 'id1')  # 读取yaml文件内容id
        id2 = RWyaml(self.Public_path).read_yaml_value('content', 'id2')  # 读取yaml文件内容id
        self.data['ids'] = [id1, id2]
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_batch_hidepc_content(self):
        # 批量隐藏电脑版
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_batch_showpc_content(self):
        # 批量显示电脑版
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_zbatch_delete_content(self):
        # 批量删除
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.headers["Content-Type"] = "application/x-www-form-urlencoded;charset=UTF-8"
        id1 = RWyaml(self.Public_path).read_yaml_value('content', 'addid1')  # 读取yaml文件内容id
        id2 = RWyaml(self.Public_path).read_yaml_value('content', 'addid2')  # 读取yaml文件内容id
        self.data['id'] = [id1, id2]
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            # print(r.json())
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_quick_addclass_content(self):
        # 快速添加分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['introductionCategory']['name'] = random_name()
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            # print(r.json())
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_autokey_content(self):
        # 自动获取关键词
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['content'] = random_address()
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            # print(r.json())
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_get_relevant_content(self):
        # 获取相关内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.headers["Content-Type"] = "application/x-www-form-urlencoded;charset=UTF-8"
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_jump_class_content(self):
        # 跳转分类管理页
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            # print(r.json())
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_add_link_content(self):
        # 新增链接分类内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data["introductionContent"]['title'] = ("接口新增链接分类" + str(time.time())[:10])  # 随机生成内容标题
        self.data["introductionContent"]["linkurl"] = "www.baidu.com"  # 链接url
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            id = r.json()['data']
            RWyaml(self.Public_path).write_yaml('content', 'addid1', id[8:])  # 新增内容id存入public.yaml文件

            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
