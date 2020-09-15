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
from Door.news.infoes_st import picture_ids
from Door.position.Public import Public_Data as pd
my_data = pd()
try:
    department_ids = my_data.get_department_ids()
except:
    department_ids = []
try:
    position_ids = my_data.get_position_ids()
except:
    position_ids = []

pb_data = type("pb_data", (object,), {})
setattr(pb_data, "department_ids", department_ids)
setattr(pb_data, "position_ids", position_ids)
setattr(pb_data, "picture_ids", picture_ids)


@ddt
class release_position(MyTest):

    condition = True
    type_condition = True
    # 职位发布

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_add_position(self):
        # 添加职位
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if not pb_data.department_ids:
                pb_data.department_ids = my_data.get_department_ids()
                id = choice(pb_data.department_ids).get("id")
            else:
                id = choice(pb_data.department_ids).get("id")
            url = ConfigYaml(self.projectName).base_url + self.url
            self.data["job"]['departmentId'] = id
            self.data['departmentId'] = id
            self.data["job"]['age'] = 24
            self.data["job"]['name'] = random_str("自动化测试职位发布名称")
            self.data["job"]['des'] = random_str("<p>自动化测试职位发布数据</p>")
            self.data["job"]['district'] = "四川省||成都市||锦江区"
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular


    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_add_department(self):
        # 添加部门
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_picture_ids()
                id_imgurl = choice(pb_data.picture_ids)
            else:
                id_imgurl = choice(pb_data.picture_ids)

            self.data['department']['name'] = random_str("自动化新增部门")
            self.data['department']['des'] = random_str("<p>自动化部门详情信息....</p>")
            self.data['department']['summary'] = random_str("<p>自动化部门描述信息....</p>")
            self.data['department']['keywords'] = random_str("<p>自动化部门关键词....</p>")
            self.data['department']['imgUrl'] = id_imgurl.get("imgUrl")
            self.data['department']['keywords'] = id_imgurl.get("id")
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
    def test_list_position(self):
        # 职位列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

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
    def test_sort_position(self):
        # 职位发布--拖拽排序
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if len(pb_data.position_ids) > 2:
                id_one = pb_data.position_ids[0].get("id")
                id_two = pb_data.position_ids[1].get("id")
            else:
                my_data.add_position()
                my_data.add_position()
                pb_data.position_ids = my_data.get_position_ids()
                id_one = pb_data.position_ids[0].get("id")
                id_two = pb_data.position_ids[1].get("id")

            self.data['sectionIds'] = id_two
            self.data['targetId'] = id_one
            self.data['minOrder'] = id_one
            self.data['maxOrder'] = id_two
            self.data['direction'] = 0

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
    def test_theader_position(self):
        # 职位发布--表头排序
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            url = ConfigYaml(self.projectName).base_url + self.url + "&categoryId=&state=2&mobileState=2&timeType=4&ec_p=1&ec_crd=15&draftBox=false&ec_s_visitCounts=desc"
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular


    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_search_position(self):
        # 职位发布--搜索
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if not pb_data.position_ids:
                pb_data.position_ids = my_data.get_position_ids()
                name = choice(pb_data.position_ids).get("name")
            else:
                name = choice(pb_data.position_ids).get("name")

            url = ConfigYaml(self.projectName).base_url + self.url + f"categoryId=10&state=2&mobileState=2&timeType=4&keywords={name}&ec_p=1&ec_crd=15&draftBox=false&category=10"
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular


    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_screen_position(self):
        # 职位发布--搜索
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            url = ConfigYaml(self.projectName).base_url + self.url + "&categoryId=&state=1&mobileState=2&timeType=4&endDate=2020-10-09&startDate=2020-09-07&ec_p=1&ec_crd=15&draftBox=false&ec_s_showFlag=&category=10"
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular


    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_edit_position(self):
        # 职位发布--编辑
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            if not pb_data.position_ids:
                pb_data.position_ids = my_data.get_position_ids()
                id = choice(pb_data.position_ids).get('id')
            else:
                id = choice(pb_data.position_ids).get('id')

            self.data['job']['name'] = random_str("自动化编辑后的部门名称")
            self.data['job']['id'] = id

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
    def test_updatePubTime_position(self):
        # 职位发布--更新
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.position_ids:
                pb_data.position_ids = my_data.get_position_ids()
                id = choice(pb_data.position_ids).get('id')
            else:
                id = choice(pb_data.position_ids).get('id')
            self.headers[self.type] = self.form_type
            self.data['id'] = id

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
    def test_getSitePage_position(self):
        # 职位发布--浏览
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if not pb_data.position_ids:
                pb_data.position_ids = my_data.get_position_ids()
                id = choice(pb_data.position_ids).get('id')
            else:
                id = choice(pb_data.position_ids).get('id')

            self.data['id'] = id

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
    def test_transfer_position(self):
        # 职位发布--转移
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.position_ids:
                pb_data.position_ids = my_data.get_position_ids()
                id = choice(pb_data.position_ids).get('id')
            else:
                id = choice(pb_data.position_ids).get('id')

            if not pb_data.department_ids:
                pb_data.department_ids = my_data.get_department_ids()
                de_id = choice(pb_data.department_ids).get("id")
            else:
                de_id = choice(pb_data.department_ids).get("id")
            self.data['ids'] = id
            self.data['departmentIds'] = de_id

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
    def test_pitransfer_position(self):
        # 职位发布--批量转移
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if len(pb_data.position_ids) > 2:
                id_one = pb_data.position_ids[0].get("id")
                id_two = pb_data.position_ids[1].get("id")
            else:
                my_data.add_position()
                my_data.add_position()
                pb_data.position_ids = my_data.get_position_ids()
                id_one = pb_data.position_ids[0].get("id")
                id_two = pb_data.position_ids[1].get("id")

            if not pb_data.department_ids:
                pb_data.department_ids = my_data.get_department_ids()
                de_id = choice(pb_data.department_ids).get("id")
            else:
                de_id = choice(pb_data.department_ids).get("id")

            self.data['ids'] = [id_one, id_two]
            self.data['departmentIds'] = de_id

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
    def test_show_position(self):
        # 职位发布--显示
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if not pb_data.position_ids:
                pb_data.position_ids = my_data.get_position_ids()
                id = choice(pb_data.position_ids).get('id')
            else:
                id = choice(pb_data.position_ids).get('id')

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
    def test_hiden_position(self):
        # 职位发布--隐藏
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.position_ids:
                pb_data.position_ids = my_data.get_position_ids()
                id = choice(pb_data.position_ids).get('id')
            else:
                id = choice(pb_data.position_ids).get('id')

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
    def test_pishow_position(self):
        # 职位发布--批量显示
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if len(pb_data.position_ids) > 2:
                id = pb_data.position_ids[0].get("id")
                id_ = pb_data.position_ids[1].get("id")
            else:
                my_data.add_position()
                my_data.add_position()
                pb_data.position_ids = my_data.get_position_ids()
                id = pb_data.position_ids[0].get("id")
                id_= pb_data.position_ids[1].get("id")

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
    def test_pihiden_position(self):
        # 职位发布--批量隐藏
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if len(pb_data.position_ids) > 2:
                id = pb_data.position_ids[0].get("id")
                id_ = pb_data.position_ids[1].get("id")
            else:
                my_data.add_position()
                my_data.add_position()
                pb_data.position_ids = my_data.get_position_ids()
                id = pb_data.position_ids[0].get("id")
                id_ = pb_data.position_ids[1].get("id")

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
    def test_delete_position(self):
        # 职位发布--删除
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            if not pb_data.position_ids:
                pb_data.position_ids = my_data.get_position_ids()
                id = pb_data.position_ids.pop(0).get('id')
            else:
                id = pb_data.position_ids.pop(0).get('id')

            url = ConfigYaml(self.projectName).base_url + self.url + f"&ids={id}"
            r = requests.get(url, headers=self.headers, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular


    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_pidelete_position(self):
        # 职位发布--批量删除
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if len(pb_data.position_ids) > 2:
                id = pb_data.position_ids.pop(0).get("id")
                id_ = pb_data.position_ids.pop(1).get("id")
            else:
                my_data.add_position()
                my_data.add_position()
                pb_data.position_ids = my_data.get_position_ids()
                id = pb_data.position_ids.pop(0).get("id")
                id_ = pb_data.position_ids.pop(1).get("id")

            url = ConfigYaml(self.projectName).base_url + self.url + f"&ids={id},{id_}"
            r = requests.get(url, headers=self.headers, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular


    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_turnpage_position(self):
        # 职位发布--翻页
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            url = ConfigYaml(self.projectName).base_url + self.url + "categoryId=&state=2&mobileState=2&timeType=4&ec_p=2&ec_crd=15&draftBox=false"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular


    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_getSeoList_position(self):
        # 职位发布--添加职能部门页面接口
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            url = ConfigYaml(self.projectName).base_url + self.url + "&pageType=2"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular


    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_list_department(self):
        # 职位发布--添加职能部门页面接口
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

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
    def test_edit_department(self):
        # 职位发布--职能部门编辑
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if not pb_data.department_ids:
                pb_data.department_ids = my_data.get_department_ids()
                id_ = choice(pb_data.department_ids).get("id")
            else:
                id_ = choice(pb_data.department_ids).get("id")

            self.data["department"]['name'] = random_str("编辑后的职能部门名称")
            self.data["department"]['id'] = id_

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
    def test_cat_department(self):
        # 职位发布--职能部门查看
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            if not pb_data.department_ids:
                pb_data.department_ids = my_data.get_department_ids()
                id_ = choice(pb_data.department_ids).get("id")
            else:
                id_ = choice(pb_data.department_ids).get("id")
            url = ConfigYaml(self.projectName).base_url + self.url + f"category={id_}"
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular


    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_sort_department(self):
        # 职位发布--职能部门拖拽排序
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if len(pb_data.department_ids) > 2:
                id_one = pb_data.department_ids[0].get("id")
                id_two = pb_data.department_ids[1].get("id")
            else:
                my_data.add_department()
                my_data.add_department()
                pb_data.department_ids = my_data.get_department_ids()
                id_one = pb_data.department_ids[0].get("id")
                id_two = pb_data.department_ids[1].get("id")

            url = ConfigYaml(self.projectName).base_url + self.url + f"&sectionIds={id_two}&targetId={id_one}&minOrder={id_one}&maxOrder={id_two}&direction=0"
            r = requests.get(url, headers=self.headers, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular


    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_show_department(self):
        # 职位发布--职能部门显示
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.department_ids:
                pb_data.department_ids = my_data.get_department_ids()
                id = choice(pb_data.department_ids).get("id")
            else:
                id = choice(pb_data.department_ids).get("id")

            self.data['id'] = id

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
    def test_hideen_department(self):
        # 职位发布--职能部门隐藏
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if not pb_data.department_ids:
                pb_data.department_ids = my_data.get_department_ids()
                id = choice(pb_data.department_ids).get("id")
            else:
                id = choice(pb_data.department_ids).get("id")

            self.data['id'] = id

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
    def test_delete_department(self):
        # 职位发布--职能部门删除
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if not pb_data.department_ids:
                pb_data.department_ids = my_data.get_department_ids()
                id = pb_data.department_ids.pop(0).get("id")
            else:
                id = pb_data.department_ids.pop(0).get("id")
                
            url = ConfigYaml(self.projectName).base_url + self.url + f"&id={id}"
            r = requests.get(url, headers=self.headers, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        