# coding=utf-8
import unittest
import traceback
import requests
from Common.FontColor import outcome
from Common.MyUnit import MyTest
from Common.ReadYaml import ConfigYaml
from Common.DataHandle import ReRun
import urllib3
from Door.companyFile import Public
from ddt import ddt,data,unpack


@ddt  # 装饰测试类
class manage_companyFile(MyTest):

    condition = True
    type_condition = False

    # 企业下载
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test01_add_companyFile(self):
        # 添加链接文件
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            C_id = str(Public.GetAll().add_Cate())
            self.data['cateGoryIds'] = C_id
            self.data['imgUrl'] = str(Public.readyaml(file=r'Door\AddProduct', key='p_url'))
            self.data['imgId'] = str(Public.readyaml(file=r'Door\AddProduct', key='p_id'))
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test02_more_companyFile(self):
        # 添加多个分类链接文件
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            url1 = ConfigYaml(self.projectName).base_url+"/manager/gwforward/manager-webapi/content/companyFileCategory/companyfileCategoryTree"
            r1 = requests.get(url=url1, headers=self.headers,data={},stream=True, verify=False)
            self.result = r1.json()
            a = self.result['data'][0]['id']
            b = self.result['data'][1]['id']
            self.data['cateGoryIds'] = "%s,%s" % (a, b)
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
    def test03_selectApp(self):
        # 获取相关内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url + "&detailAppId=24"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test04_getSeoList(self):
        # 获取SEO列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url + "&appId=24&type=1&detailId="
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test05_getUsedAndTotalCapacity(self):
        # 获取全部分类和用户分类
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
    def test06_getKs3Config(self):
        # 获取金山文件接口
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
    def test07_findByPagination(self):
        # 获取文件接口列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            Public.GetAll().put_file()
            url = ConfigYaml(self.projectName).base_url + self.url + "&currentPage=1&pageSize=15&startDate=&endDate=&queryStatus=&type=0&orderColumn=&orderType=&keywords="
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()
            id1 = self.result['data']['list'][0]['id']
            path1 = self.result['data']['list'][0]['path']
            id2 = self.result['data']['list'][1]['id']
            path2 = self.result['data']['list'][1]['path']
            Public.writeyaml(w_key='file_id1', w_value=id1, n="w", file='Door\companyFile')
            Public.writeyaml(w_key='path1', w_value=path1, n="a", file='Door\companyFile')
            Public.writeyaml(w_key='file_id2', w_value=id2, n="a", file='Door\companyFile')
            Public.writeyaml(w_key='path2', w_value=path2, n="a", file='Door\companyFile')
            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test08_add_File(self):
        # 添加普通单图文件
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            C_id = str(Public.GetAll().add_Cate())
            self.data['cateGoryIds'] = C_id
            self.data['imgUrl'] = str(Public.readyaml(file=r'Door\AddProduct', key='p_url'))
            self.data['imgId'] = str(Public.readyaml(file=r'Door\AddProduct', key='p_id'))
            self.data['comFiles'][0]['id'] = Public.readyaml(file=r'Door\companyFile', key='file_id1')
            self.data['comFiles'][0]['path'] = Public.readyaml(file=r'Door\companyFile', key='path1')
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test09_add_moreCate(self):
        # 添加多选文件
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            C_id = str(Public.GetAll().add_Cate())
            self.data['cateGoryIds'] = C_id
            self.data['imgUrl'] = str(Public.readyaml(file=r'Door\AddProduct', key='p_url'))
            self.data['imgId'] = str(Public.readyaml(file=r'Door\AddProduct', key='p_id'))
            self.data['comFiles'][0]['id'] = Public.readyaml(file=r'Door\companyFile', key='file_id1')
            self.data['comFiles'][0]['path'] = Public.readyaml(file=r'Door\companyFile', key='path1')
            self.data['comFiles'][1]['id'] = Public.readyaml(file=r'Door\companyFile', key='file_id2')
            self.data['comFiles'][1]['path'] = Public.readyaml(file=r'Door\companyFile', key='path2')
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test10_add_content(self):
        # 添加电脑版、移动版描述，关键词文件
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            C_id = str(Public.GetAll().add_Cate())
            self.data['cateGoryIds'] = C_id
            self.data['comFiles'][0]['id'] = Public.readyaml(file=r'Door\companyFile', key='file_id1')
            self.data['comFiles'][0]['path'] = Public.readyaml(file=r'Door\companyFile', key='path1')
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test11_add_relevantInfoList(self):
        # 获取企业下载列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            headers = Public.readconfig_ini(v=2)
            url = ConfigYaml(self.projectName).base_url + self.url
            self.data = "keyword=&pcStatus=-1&moStatus=-1&ids=&notSelectIds=&categoryId=0&pageNumber=1&pageSize=15&appId=24&"
            r = requests.post(url, headers=headers, json=self.data, stream=True, verify=False)
            self.result = r.json()
            id = self.result['data']['relatedContentList'][0]['id']
            Public.writeyaml(w_key='list_id', w_value=id, n='a', file='Door\companyFile')
            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test12_RelevantContent(self):
        # 有相关内容文件
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            C_id = str(Public.GetAll().add_Cate())
            self.data['cateGoryIds'] = C_id
            self.data['comFiles'][0]['id'] = Public.readyaml(file=r'Door\companyFile', key='file_id1')
            self.data['comFiles'][0]['path'] = Public.readyaml(file=r'Door\companyFile', key='path1')
            self.data['RelevantContent'][0]['contentList'] = [Public.readyaml(file=r'Door\companyFile', key='list_id')]
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test13_getAppAuthority(self):
        # 获取高级选项
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url1 = ConfigYaml(self.projectName).base_url + self.url + "&appId=24&type=1&detailId="
            url2 = ConfigYaml(self.projectName).base_url + self.url + "&appId=24&type=3&detailId="
            for url in [url1, url2]:
                r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
                self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test14_authData(self):
        # 高级选项文件
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            C_id = str(Public.GetAll().add_Cate())
            self.data['cateGoryIds'] = C_id
            self.data['imgUrl'] = str(Public.readyaml(file=r'Door\AddProduct', key='p_url'))
            self.data['imgId'] = str(Public.readyaml(file=r'Door\AddProduct', key='p_id'))
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test15_sort_list(self):
        # 企业下载列表排序
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            Public.GetAll().get_sortlist()
            headers = Public.readconfig_ini(v=2)
            url = ConfigYaml(self.projectName).base_url + self.url
            orderMode = ['TITLE_ASC', 'TITLE_DESC', 'PUB_DATE_ASC', 'PUB_DATE_DESC', 'default']
            for i in orderMode:
                self.data = 'viewType=1&tenantId=196566&_d=1594276214675&orderMode=' + i
                r = requests.post(url, headers=headers, data=self.data, stream=True, verify=False)
                self.result = r.json()

                self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test16_get_info(self):
        # 获取电脑、移动端域名
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
    def test17_get_list(self):
        # 企业下载列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            self.data = "appId=24&cateId=-1&pcStatus=-1&mobileStatus=-1&startDate=&endDate=&wd=&pageSize=15&currentPage=1&ec_s_title=&ec_s_categorys=&ec_s_pubDate=&ec_s_showFlag=&ec_s_showMobileFlag=&ec_s_viewcount=&orderColumn=&orderType=&"
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()
            id1 = self.result['data']['list'][0]['id']
            id2 = self.result['data']['list'][1]['id']
            Public.writeyaml(w_key='id1', w_value=id1, n="a", file='Door\companyFile')
            Public.writeyaml(w_key='id2', w_value=id2, n="a", file='Door\companyFile')
            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test18_get_updatelist(self):
        # 企业拖拽排序
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            headers = Public.readconfig_ini(v=2)
            url = ConfigYaml(self.projectName).base_url + self.url
            id2 = Public.readyaml(file=r'Door\companyFile', key='id2')
            id1 = Public.readyaml(file=r'Door\companyFile', key='id1')
            self.data = "sectionIds="+str(id2)+"&targetId="+str(id1)+"&minOrder="+str(id1)+"&maxOrder="+str(id2)+"&direction=0&"
            r = requests.post(url, headers=headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test19_choice_list(self):
        # 筛选列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            headers = Public.readconfig_ini(v=2)
            url = ConfigYaml(self.projectName).base_url + self.url
            C_id = str(Public.GetAll().add_Cate())
            self.data = "appId=24&cateId="+C_id+"&pcStatus=1&mobileStatus=-1&startDate=2020-07-08%2000%3A00&endDate=2020-07-08%2023%3A59&wd=&pageSize=15&currentPage=1&ec_s_title=&ec_s_categorys=&ec_s_pubDate=&ec_s_showFlag=&ec_s_showMobileFlag=&ec_s_viewcount=&orderColumn=&orderType=&"
            r = requests.post(url, headers=headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test20_search_list(self):
        # 搜索列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            headers = Public.readconfig_ini(v=2)
            C_id = str(Public.GetAll().add_Cate())
            cateId = C_id
            self.data = "appId=24&cateId="+cateId+"&pcStatus=1&mobileStatus=-1&startDate=&endDate=&wd=%E5%85%B3%E9%94%AE&pageSize=15&currentPage=1&ec_s_title=&ec_s_categorys=&ec_s_pubDate=&ec_s_showFlag=&ec_s_showMobileFlag=&ec_s_viewcount=&orderColumn=&orderType=&"

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test21_next_list(self):
        # 翻页
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            headers = Public.readconfig_ini(v=2)
            C_id = str(Public.GetAll().add_Cate())
            cateId = C_id
            self.data = "appId=24&cateId=" + cateId + "&pcStatus=1&mobileStatus=-1&startDate=&endDate=&wd=&pageSize=15&currentPage=2&ec_s_title=&ec_s_categorys=&ec_s_pubDate=&ec_s_showFlag=&ec_s_showMobileFlag=&ec_s_viewcount=&orderColumn=&orderType=&"

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test22_editor(self):
        # 编辑企业下载
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            self.data['id'] = str(Public.readyaml(file=r'Door\companyFile', key='id1'))
            C_id = str(Public.GetAll().add_Cate())
            self.data['cateGoryIds'] = C_id
            self.data['imgUrl'] = str(Public.readyaml(file=r'Door\AddProduct', key='p_url'))
            self.data['imgId'] = str(Public.readyaml(file=r'Door\AddProduct', key='p_id'))
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test23_goto(self):
        # 批量转移
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            headers = Public.readconfig_ini(v=2)
            id1 = str(Public.readyaml(file=r'Door\companyFile', key='id1'))
            id2 = str(Public.readyaml(file=r'Door\companyFile', key='id2'))
            C_id = str(Public.GetAll().add_Cate())
            data1 = "appId=24&id="+id1+',' + id2+"&cateId=" + C_id
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=headers, data=data1, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test24_updateState_PC(self):
        # 批量显示/隐藏电脑版
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            headers = Public.readconfig_ini(v=2)
            id1 = str(Public.readyaml(file=r'Door\companyFile', key='id1'))
            id2 = str(Public.readyaml(file=r'Door\companyFile', key='id2'))
            url1 = ConfigYaml(
                self.projectName).base_url + self.url + "appId=24&id=" + id1 + "," + id2 + "&view=pc&state=true"
            url2 = ConfigYaml(self.projectName).base_url + self.url + "appId=24&id="+id1+","+id2+"&view=pc&state=false"
            for url in [url1, url2]:
                r = requests.get(url, headers=headers, data=self.data, stream=True, verify=False)
                self.result = r.json()

                self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test25_updateState_MO(self):
        # 批量显示/隐藏移动版
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            headers = Public.readconfig_ini(v=2)
            id1 = str(Public.readyaml(file=r'Door\companyFile', key='id1'))
            id2 = str(Public.readyaml(file=r'Door\companyFile', key='id2'))
            url1 = ConfigYaml(
                self.projectName).base_url + self.url + "appId=24&id=" + id1 + "," + id2 + "&view=mo&state=true"
            url2 = ConfigYaml(
                self.projectName).base_url + self.url + "appId=24&id=" + id1 + "," + id2 + "&view=mo&state=false"
            for url in [url1, url2]:
                r = requests.get(url, headers=headers, data=self.data, stream=True, verify=False)
                self.result = r.json()

                self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test26_delete(self):
        # 批量删除
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            headers = Public.readconfig_ini(v=2)
            id1 = str(Public.readyaml(file=r'Door\companyFile', key='id1'))
            id2 = str(Public.readyaml(file=r'Door\companyFile', key='id2'))
            self.data = "ppId=24&id=" + id1 + ',' + id2
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        