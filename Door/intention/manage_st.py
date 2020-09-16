# coding=utf-8
import unittest
import traceback
import requests
from Common.FontColor import outcome
from Common.MyUnit import MyTest
from Common.ReadYaml import ConfigYaml
from Common.DataHandle import ReRun
import urllib3
from ddt import ddt, data, file_data
from Common.ReExecution import Get_Cls_Fun
from Common.Design import Design
from Door.intention import Public


@ddt
class manage_intention(MyTest):
    condition = True
    type_condition = False

    # 互动表单-意向信息

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test01_intention_list(self):
        # 意向信息列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            Design().add_intention()
            url = ConfigYaml(self.projectName).base_url + self.url + "&categoryId=-1&status=-1&equipmentType=-1" \
                                                                     "&startDate=&endDate=&name=&dateType=0&ec_p=1" \
                                                                     "&ec_crd=15"

            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()
            id = self.result['data']['pagination']['list'][0]['id']
            Public.writeyaml(w_key='list_id', w_value=id, n='w', file=r'Door\intention')

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test02_intention_list(self):
        # 意向筛选已删除列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url + "&categoryId=0&status=-1" \
                                                                     "&equipmentType=-1&dateType=0" \
                                                                     "&ec_p=1&ec_crd=15"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test03_intention_list(self):
        # 搜索意向列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url + "&categoryId=0&status=-1&equipmentType=-1" \
                                                                     "&startDate=&endDate=" \
                                                                     "&name=达达&dateType=0&ec_p=1&ec_crd=15"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test04_intention_list(self):
        # 排序意向列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url +"&categoryId=0&status=-1&equipmentType=-1" \
                                                                     "&startDate=&endDate=&name=达达&dateType=0" \
                                                                    "&ec_p=1&ec_crd=15&" \
                                                                    "ec_s_POST_DATE=&ec_s_SERIAL_NUMBER=desc" \
                                                                    "&ec_s_UPDATE_DATE="
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test05_intention_list(self):
        # 翻页意向列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url + "&categoryId=0&status=-1&equipmentType=-1" \
                                                                     "&startDate=&endDate=&name=达达&dateType=0" \
                                                                     "&ec_p=2&ec_crd=15&" \
                                                                     "ec_s_POST_DATE=&ec_s_SERIAL_NUMBER=desc" \
                                                                     "&ec_s_UPDATE_DATE="
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test06_send_sms_intention(self):
        # 意向转发短信
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
    def test07_send_sendMail_intention(self):
        # 意向转发邮件
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
    def test08_intention_intention(self):
        # 处理未删除意向
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            id = str(Public.readyaml(file=r'Door\intention', key='list_id'))
            url = ConfigYaml(self.projectName).base_url + self.url + "&intentionIds="+id+"&operationType=0"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test09_intention_subhandle(self):
        # 意向备注
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            id = str(Public.readyaml(file=r'Door\intention', key='list_id'))
            url = ConfigYaml(self.projectName).base_url + self.url
            data="intentionId="+id+"&followupContent=565"
            self.data['intentionId'] = id
            r = requests.post(url, headers=Public.readconfig_ini(v=2), data=data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test10_getAllChannel_sms_intention(self):
        # 意向客户发短信
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
    def test11_change_status_intention(self):
        # 有效意向
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            id = str(Public.readyaml(file=r'Door\intention', key='list_id'))
            url = ConfigYaml(self.projectName).base_url + self.url + "&status=2&id="+id
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test12_change_status_intention(self):
        # 无效意向
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            id = str(Public.readyaml(file=r'Door\intention', key='list_id'))
            url = ConfigYaml(self.projectName).base_url + self.url + "&status=3&id="+id
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test13_change_list_intention(self):
        # 意向操作记录
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            id = str(Public.readyaml(file=r'Door\intention', key='list_id'))
            url = ConfigYaml(self.projectName).base_url + self.url + "&operationType=0&intentionIds="+id
            r = requests.get(url, headers=Public.readconfig_ini(v=2), data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test14_delete_intention(self):
        # 删除意向列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            id = str(Public.readyaml(file=r'Door\intention', key='list_id'))
            url = ConfigYaml(self.projectName).base_url + self.url
            data = "id="+id
            r = requests.post(url, headers=Public.readconfig_ini(v=2), data=data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test15_intention_dellist(self):
        # 搜索和筛选已删除意向列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url +"&urlType=deletedEnquiry&status=-1&source=-1&startDate=2020-09-05&endDate=2020-09-11&keyword=&dateType=4&ec_p=1&ec_crd=15"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test16_intention_nodellist(self):
        # 意向还原
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            id = str(Public.readyaml(file=r'Door\intention', key='list_id'))
            data = "intentionIds="+id+"&flag=0"
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=Public.readconfig_ini(v=2), data=data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test17_see_del_intention(self):
        # 查看已删除意向
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            Public.GetAll().delete_enquiry()
            id = str(Public.readyaml(file=r'Door\intention', key='list_id'))
            url = ConfigYaml(self.projectName).base_url + self.url + "&intentionIds="+id+"&operationType=0"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test18_intention_isdelete(self):
        # 彻底删除意向
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            id = str(Public.readyaml(file=r'Door\intention', key='list_id'))
            url = ConfigYaml(self.projectName).base_url + self.url
            data = "id="+id
            r = requests.post(url, headers=Public.readconfig_ini(v=2), data=data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

        


        


        


        


        


        


        


        