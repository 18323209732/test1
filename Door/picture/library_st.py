# coding=utf-8
import unittest
import traceback
import requests

from Common.CusMethod import get_hour_second, random_str
from Common.FontColor import outcome
from Common.MyUnit import MyTest
from Common.ReadYaml import ConfigYaml
from Common.DataHandle import ReRun
import urllib3
from random import choice
from Door.picture.Public import Public_Data as pd
from Door.news.infoes_st import picture_ids
from Common.Route import Any_Path
my_data = pd()
try:
    class_ids = my_data.get_class_ids()
except:
    class_ids = []

pb_data = type("pb_data", (object,), {})
setattr(pb_data, "picture_ids", picture_ids)
setattr(pb_data, "class_ids", class_ids)

class library_picture(MyTest):

    condition = True
    type_condition = True


    # 新闻分类管理
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_list_picture(self):
        # 全部图片列表数据
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
    def test_search_picture(self):
        # 筛选图片
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            self.data['queryStatus'] = choice([0, 1, ''])
            self.data['startDate'] = get_hour_second(-7)
            self.data['endDate'] = get_hour_second(0)
            self.data['classId'] = choice([0, 1, ''])

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
    def test_screen_picture(self):
        # 搜索图片
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_picture_ids()
                name = choice(pb_data.picture_ids).get("name")
            else:
                name = choice(pb_data.picture_ids).get("name")
            self.data['name'] = name

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
    def test_edit_picture(self):
        # 编辑图片
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_picture_ids()
                id = choice(pb_data.picture_ids).get("id")
            else:
                id = choice(pb_data.picture_ids).get("id")
            self.data['id'] = id
            self.data['name'] = random_str("自动化编辑图片名称...")

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
    def test_upload_picture(self):
        # 上传图片
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            file_path = Any_Path("File", "picture.jpg")
            del self.headers[self.type]
            f = open(file_path, "rb")
            file = {"file": f}

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, files=file, stream=True, verify=False)
            f.close()
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_cat_picture(self):
        # 预览图片
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            del self.headers[self.type]
            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_picture_ids()
                img_url = choice(pb_data.picture_ids).get("imgUrl")
            else:
                img_url = choice(pb_data.picture_ids).get("imgUrl")

            url = ConfigYaml(self.projectName).base_url + img_url
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            if r.content:
                self.result = {'status': '200'}

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_move_picture(self):
        # 转移图片
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_picture_ids()
                id = choice(pb_data.picture_ids).get("id")
            else:
                id = choice(pb_data.picture_ids).get("id")
            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class_ids()
                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")
            self.data['ids'] = id
            self.data['classId'] = class_id

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
    def test_moves_pictures(self):
        # 批量转移图片
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if len(pb_data.picture_ids) > 2:
                id_one = pb_data.picture_ids[0].get("id")
                id_two = pb_data.picture_ids[1].get("id")
            else:
                my_data.file_upload()
                my_data.file_upload()
                pb_data.picture_ids = my_data.get_picture_ids()
                id_one = pb_data.picture_ids[0].get("id")
                id_two = pb_data.picture_ids[1].get("id")

            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class_ids()
                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")

            self.data['classId'] = class_id
            self.data['ids'] = [id_one, id_two]

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
    def test_addwater_pictures(self):
        # 添加水印
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_picture_ids()
                id = choice(pb_data.picture_ids).get("id")
            else:
                id = choice(pb_data.picture_ids).get("id")
            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class_ids()
                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")
            self.data['ids'] = id
            self.data['classId'] = class_id

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
    def test_addwateres_pictures(self):
        # 批量添加水印
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if len(pb_data.picture_ids) > 2:
                id_one = pb_data.picture_ids[0].get("id")
                id_two = pb_data.picture_ids[1].get("id")
            else:
                my_data.file_upload()
                my_data.file_upload()
                pb_data.picture_ids = my_data.get_picture_ids()
                id_one = pb_data.picture_ids[0].get("id")
                id_two = pb_data.picture_ids[1].get("id")

            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class_ids()
                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")

            self.data['classId'] = class_id
            self.data['ids'] = [id_one, id_two]

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
    def test_acancelwateres_pictures(self):
        # 批量取消水印
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if len(pb_data.picture_ids) > 2:
                id_one = pb_data.picture_ids[0].get("id")
                id_two = pb_data.picture_ids[1].get("id")
            else:
                my_data.file_upload()
                my_data.file_upload()
                pb_data.picture_ids = my_data.get_picture_ids()
                id_one = pb_data.picture_ids[0].get("id")
                id_two = pb_data.picture_ids[1].get("id")

            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class_ids()
                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")

            self.data['classId'] = class_id
            self.data['ids'] = [id_one, id_two]

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
    def test_acancelwater_pictures(self):
        # 取消水印
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_picture_ids()
                id = choice(pb_data.picture_ids).get("id")
            else:
                id = choice(pb_data.picture_ids).get("id")
            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class_ids()

                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")

            self.data['ids'] = id
            self.data['classId'] = class_id

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
    def test_delete_pictur(self):
        # 删除水印
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_picture_ids()
                id = choice(pb_data.picture_ids).get("id")
            else:
                id = choice(pb_data.picture_ids).get("id")

            url = ConfigYaml(self.projectName).base_url + self.url + f"&ids={id}"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_delete_pictures(self):
        # 批量删除水印
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if len(pb_data.picture_ids) > 2:
                id_one = pb_data.picture_ids[0].get("id")
                id_two = pb_data.picture_ids[1].get("id")
            else:
                my_data.file_upload()
                my_data.file_upload()
                pb_data.picture_ids = my_data.get_picture_ids()
                id_one = pb_data.picture_ids[0].get("id")
                id_two = pb_data.picture_ids[1].get("id")

            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class_ids()
                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")
            self.data['classId'] = class_id

            url = ConfigYaml(self.projectName).base_url + self.url + f"&ids={id_one},{id_two}"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_pages_pictures(self):
        # 翻页
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            page = choice([1, 2, 3, 4])

            url = ConfigYaml(self.projectName).base_url + self.url + f"&pageSize=15&currentPage={page}"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular


    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_editwindow_pictures(self):
        # 编辑上传图片
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            file_path = Any_Path("File", "edit.jpg")
            del self.headers[self.type]
            f = open(file_path, "rb")
            file = {"file": f}
            url = ConfigYaml(self.projectName).base_url + self.url

            r = requests.post(url, headers=self.headers, data=self.data, files=file, stream=True, verify=False)
            f.close()
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    #
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_wicket_pictures(self):
        # 编辑图片窗口
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_picture_ids()
                img_url = choice(pb_data.picture_ids).get("imgUrl")
            else:
                img_url = choice(pb_data.picture_ids).get("imgUrl")

            url = ConfigYaml(self.projectName).base_url + img_url
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            if r.content:
                self.result = {'status': '200'}

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_edetwicket_pictures(self):
        # 编辑图片确认
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_picture_ids()
                id = choice(pb_data.picture_ids).get("id")
            else:
                id = choice(pb_data.picture_ids).get("id")
            self.data['id'] = id
            self.data['name'] = random_str("自动化图片编辑后的数据")

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
    def test_waterset_pictures(self):
        # 水印设置
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
    def test_saveandgetwater_pictures(self):
        # 生成水印waterbak.png
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.type_condition = False
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            if r.content:
                self.result = {"status": '200'}

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_waterupload_pictures(self):
        # 水印设置保存
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_picture_ids()
                value = choice(pb_data.picture_ids)
            else:
                value = choice(pb_data.picture_ids)

            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class_ids()
                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")
            self.data['classId'] = class_id
            self.data['imageUrl'] = value.get("imgUrl")
            self.data['word'] = random_str("自动化测试")
            self.data['url'] = "http://www.baidu.com"
            self.data['imageId'] = value.get("id")
                
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
    def test_water_pictures(self):
        # 水印设置页面
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            if r.content:
                self.result = {"status": '200'}

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_water1_pictures(self):
        # 水印设置页面1
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            if r.content:
                self.result = {"status": '200'}

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_water2_pictures(self):
        # 水印设置页面2
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            if r.content:
                self.result = {"status": '200'}

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_reset_pictures(self):
        # 重置
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
    def test_batchsearch_pictures(self):
        # id批量查询
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if len(pb_data.picture_ids) > 2:
                id_one = pb_data.picture_ids[0].get("id")
                id_two = pb_data.picture_ids[1].get("id")
            else:
                my_data.file_upload()
                my_data.file_upload()
                pb_data.picture_ids = my_data.get_picture_ids()
                id_one = pb_data.picture_ids[0].get("id")
                id_two = pb_data.picture_ids[1].get("id")

            url = ConfigYaml(self.projectName).base_url + self.url + f"&ids={id_one},{id_two}"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            if r.json():
                self.result = {"status": 200}

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_addclass_pictures(self):
        # 添加分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            self.data['className'] = random_str("自动化测试")
            self.data['classInfo'] = random_str("自动化测试描述")

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
    def test_deleteclass_pictures(self):
        # 删除分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class_ids()
                class_id = pb_data.class_ids.pop(0).get("id")
            else:
                class_id = pb_data.class_ids.pop(0).get("id")
            self.data['ids'] = class_id

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
    def test_editclass_pictures(self):
        # 编辑分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class_ids()
                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")

            self.data['id'] = class_id
            self.data['className'] = random_str("编辑后的自动化测试")
            self.data['classInfo'] = random_str("编辑后的自动化测试描述")

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
    def test_listclass_pictures(self):
        # 获取分类列表
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
        