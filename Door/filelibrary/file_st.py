# coding=utf-8
import unittest
import traceback
from random import choice

import requests

from Common.CusMethod import random_str
from Common.FontColor import outcome
from Common.MyUnit import MyTest
from Common.ReadYaml import ConfigYaml
from Common.DataHandle import ReRun
import urllib3
from ddt import ddt, data,file_data
from Common.ReExecution import Get_Cls_Fun
from Common.Route import Any_Path
from Door.filelibrary.Public import Public_Data as pd
my_data = pd()
try:
    class_ids = my_data.get_class_list()
except:
    class_ids = []
try:
    file_ids = my_data.get_file_list()
except:
    file_ids = []


pb_data = type("pb_data", (object,), {})
setattr(pb_data, "class_ids", class_ids)
setattr(pb_data, "file_ids", file_ids)


@ddt
class file_filelibrary(MyTest):

    condition = True
    type_condition = True
    # 文件库

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_list_file(self):
        # 文件列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_search_file(self):
        # 搜索
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if not pb_data.file_ids:
                pb_data.file_ids = my_data.get_file_list()
                name = choice(pb_data.file_ids).get("fileName")
            else:
                name = choice(pb_data.file_ids).get("fileName")

            url = ConfigYaml(self.projectName).base_url + self.url + f"keywords={name}"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_shaixuan_file(self):
        # 筛选
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if not pb_data.file_ids:
                pb_data.file_ids = my_data.get_file_list()
                name = choice(pb_data.file_ids).get("fileName")
            else:
                name = choice(pb_data.file_ids).get("fileName")

            self.data['keywords'] = name

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_headsort_file(self):
        # 表头排序
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_upload_file(self):
        # 表头排序
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            del self.headers[self.type]

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_edit_file(self):
        # 编辑
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if not pb_data.file_ids:
                pb_data.file_ids = my_data.get_file_list()
                id = choice(pb_data.file_ids).get("id")
            else:
                id = choice(pb_data.file_ids).get("id")
            name = random_str("自动化测试")

            url = ConfigYaml(self.projectName).base_url + self.url + f"&authPermission=file_update&id={id}&name={name}"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_down_file(self):
        # 下载
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            file_name = my_data.get_key()[0]

            url = self.url.rsplit("?", 1)[0] + file_name

            r = requests.get(url, headers=self.headers,  stream=True, verify=False)
            self.result = r.content
            if self.result:
                self.result = {"status":200}
            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_delete_file(self):
        # 删除
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.file_ids:
                pb_data.file_ids = my_data.get_file_list()
                file_name = pb_data.file_ids.pop(0).get("fileKey")
            else:
                file_name = pb_data.file_ids.pop(0).get("fileKey")

            url = self.url.rsplit("?", 1)[0] + f"{file_name}"
            r = requests.get(url, headers=self.headers,stream=True, verify=False)
            self.result = r.content

            if self.result:
                self.result = {"status": 200}

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_pidelete_file(self):
        # 批量删除
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if len(pb_data.file_ids) > 2:
                file_name = pb_data.file_ids.pop(0).get("fileKey")
                file_name_ = pb_data.file_ids.pop(1).get("fileKey")
            else:
                my_data.file_add()
                my_data.file_add()
                pb_data.file_ids = my_data.get_file_list()
                file_name = pb_data.file_ids.pop(0).get("fileKey")
                file_name_ = pb_data.file_ids.pop(1).get("fileKey")


            url = ConfigYaml(self.projectName).base_url + self.url +f"&fileKeys={file_name},{file_name_}"

            r = requests.post(url, headers=self.headers, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_page_file(self):
        # 翻页
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
    def test_add_fileclass(self):
        # 添加分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            self.data['className'] = random_str("自动化测试")
            self.data['classInfo'] = random_str("自动化测试描述")

            url = ConfigYaml(self.projectName).base_url + self.url +"&authPermission=file_type_add"

            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_edit_fileclass(self):
        # 编辑分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class_list()
                id = choice(pb_data.class_ids).get("id")
            else:
                id = choice(pb_data.class_ids).get("id")

            self.data['id'] = id
            self.data['className'] = random_str("编辑自动化测试")
            self.data['classInfo'] = random_str("编辑自动化测试描述")

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
    def test_deleteclass_fileclass(self):
        # 删除分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class_list()
                id = pb_data.class_ids.pop(0).get("id")
            else:
                id = pb_data.class_ids.pop(0).get("id")

            self.data['ids'] = id

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
    def test_deletepi_fileclass(self):
        # 批量删除
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if len(pb_data.class_ids) > 2:
                id = pb_data.class_ids.pop(0).get("id")
                id_ = pb_data.class_ids.pop(1).get("id")
            else:
                my_data.class_add()
                my_data.class_add()
                pb_data.class_ids = my_data.get_class_list()
                id = pb_data.class_ids.pop(0).get("id")
                id_ = pb_data.class_ids.pop(1).get("id")

            self.data['ids'] = f"{id},{id_}"

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
    def test_search_fileclass(self):
        # 查找
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class_list()
                name = choice(pb_data.class_ids).get("className")
            else:
                name = choice(pb_data.class_ids).get("className")

            url = ConfigYaml(self.projectName).base_url + self.url + f"className={name}"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        