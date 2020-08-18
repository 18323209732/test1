
# coding=utf-8
import unittest
import traceback
import requests
import time,datetime
from Common.FontColor import outcome
from Common.MyUnit import MyTest
from Common.ReadYaml import ConfigYaml
from Common.DataHandle import ReRun
from Common.PrintDebug import print_debug_info
from Common.RWyaml import RWyaml as RWYaml
from Common.Route import Any_Path
import urllib3


class info_banner(MyTest):

    condition = True
    type_condition = False
    Public_path = Any_Path('Door\\banner', 'Public.yaml')
    img_path = Any_Path('Img', '图片.jpg')
    # 属性管理
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_add_banner(self):
        # 新增banner
        for i in range(1):
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            self.data['name'] = '接口新增' + str(time.time())[:10]
            self.type_condition = True
            try:
                if self.type_condition:
                    self.headers[self.type] = self.form_type

                url = ConfigYaml(self.projectName).base_url + self.url
                r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
                # print(r.json())
                addid = r.json()['data']['positionId']
                RWYaml(self.Public_path).write_yaml('banner', 'addid', addid)

                self.result = r.json()

                self.time = r.elapsed.total_seconds()
                print_debug_info('--->pass')
            except:
                self.singular = str(traceback.format_exc())
                outcome('red', self.singular)
                return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_zdelete_banner(self):
        # 删除banner
        # for i in range(1):
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            self.data['id'] = RWYaml(self.Public_path).read_yaml_value('banner', 'addid')
            try:
                if self.type_condition:
                    self.headers[self.type] = self.form_type

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
    def test_bgetlist_banner(self):
        # 获取全部列表banner
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            name = r.json()['data']['list'][0]['name']
            RWYaml(self.Public_path).write_yaml('banner', 'name', name)     # 写入name
            number = r.json()['data']['totalCount']
            RWYaml(self.Public_path).write_yaml('banner', 'banner_number', number)     # 写入banner总数
            id = r.json()['data']['list']
            n = 1
            for i in id:
                RWYaml(self.Public_path).write_yaml('banner', 'id'+str(n), i['id'])
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
    def test_time_screen_banner(self):
        # 筛选banner
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        day = str(datetime.datetime.now())[:10]
        self.data['startDate'] = day
        self.data['endDate'] = day
        self.data['positionId'] = RWYaml(self.Public_path).read_yaml_value('banner', 'addid')
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            # print(r.json()['data']['list'])
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_name_screen_banner(self):
        # 搜索banner
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['keywords'] = RWYaml(self.Public_path).read_yaml_value('banner', 'name')
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            # print(r.json()['data']['list'])
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_add_img_banner(self):
        # 添加图片内容
        for i in range(2):
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            self.data[0]['apId'] = RWYaml(self.Public_path).read_yaml_value('banner', 'addid')
            self.data[0]['resUrl'] = RWYaml(self.Public_path).read_yaml_value('img', 'imageurl')
            self.data[0]['resId'] = RWYaml(self.Public_path).read_yaml_value('img', 'imageId')
            self.data[0]['title'] = '添加图片' + str(time.time())[:10]
            self.data[0]['beginTime'] = str(datetime.datetime.now())[:19]  # 发布开始时间
            try:
                if self.type_condition:
                    self.headers[self.type] = self.form_type

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
    def test_edit_banner(self):
        # 编辑banner
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['id'] = RWYaml(self.Public_path).read_yaml_value('banner', 'addid')
        self.data['name'] = '接口编辑' + str(time.time())[:10]
        self.type_condition = True
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
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
    def test_aaupload_img_banner(self):
        # 上传照片
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        with open(self.img_path, 'rb')as f:    # 使用with打开图片后自动关闭，直接用open后面会报未关闭图片错误
            file = {"file": ("图片.jpg", f.read(), "image/jpeg")}
        del self.headers['Content-Type']
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False, files=file)
            # print(r.json())
            RWYaml(self.Public_path).write_yaml('img', 'imageId', r.json()['data']['fileID'])  # fileID存入public.yaml文件
            RWYaml(self.Public_path).write_yaml('img', 'imageurl', r.json()['data']['imgUrl'])  # fileID存入public.yaml文件
            if r.json():
                self.result = {"status": 200}

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_title_sort_banner(self):
        # 表头排序
        import random
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['ec_s_name'] = random.sample(['asc', 'desc'], 1)  # random.sample()方法随机获取列表一个值
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
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
    def test_flip_over_banner(self):
        # 翻页
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        number = RWYaml(self.Public_path).read_yaml_value('banner', 'banner_number')
        if int(number) > 15:       # 15表示单页最多显示15条，大于15表示有翻页
            self.data['currentPage'] = 2    # 修改翻页数，默认是1
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            # print(r.json()['data']['list'][0]['id'])
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_maintain_banner(self):
        # 维护跳转
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['positionId'] = RWYaml(self.Public_path).read_yaml_value('banner', 'addid')
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
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
    def test_add_code_banner(self):
        # 添加代码内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data[0]['title'] = '添加代码' + str(time.time())[:10]
        self.data[0]['apId'] = RWYaml(self.Public_path).read_yaml_value('banner', 'addid')
        self.data[0]['beginTime'] = str(datetime.datetime.now())[:19]  # 发布开始时间
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
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
    def test_bmaintain_list_banner(self):
        # 维护内容列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['positionId'] = RWYaml(self.Public_path).read_yaml_value('banner', 'addid')
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            id = r.json()['data']['list'][0]['id']
            RWYaml(self.Public_path).write_yaml('banner', 'content_id', id)  # 写入维护列表id
            content_number = r.json()['data']['totalCount']
            RWYaml(self.Public_path).write_yaml('banner', 'content_number', content_number)  # 写入维护列表id
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_hide_banner(self):
        # 隐藏电脑版
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['id'] = RWYaml(self.Public_path).read_yaml_value('banner', 'content_id')
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
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
    def test_show_banner(self):
        # 显示电脑版
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['id'] = RWYaml(self.Public_path).read_yaml_value('banner', 'content_id')
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
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
    def test_edit_content_banner(self):
        # 编辑banner内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['id'] = RWYaml(self.Public_path).read_yaml_value('banner', 'content_id')
        self.data['title'] = '编辑' + str(time.time())[:10]
        self.data['linkUrl'] = 'www.baidu.com'
        self.data['beginTime'] = str(datetime.datetime.now())[:19]       # 发布开始时间

        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_screen_content_banner(self):
        # 筛选banner内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['positionId'] = RWYaml(self.Public_path).read_yaml_value('banner', 'addid')
        self.data['startDate'] = str(datetime.datetime.now())[:10]
        self.data['endDate'] = str(datetime.datetime.now())[:10]
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            # print(r.json()['data']['list'])
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_findname_content_banner(self):
        # name搜索banner内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['positionId'] = RWYaml(self.Public_path).read_yaml_value('banner', 'addid')
        self.data['keywords'] = '添加'
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

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
    def test_ydelete_content_banner(self):
        # 删除banner内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['ids'] = RWYaml(self.Public_path).read_yaml_value('banner', 'content_id')
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

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
    def test_flipover_content_banner(self):
        # 翻页banner内容
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        number = RWYaml(self.Public_path).read_yaml_value('banner', 'content_number')
        if int(number) > 15:  # 15表示单页最多显示15条，大于15表示有翻页
            self.data['currentPage'] = 2
            # 修改翻页数，默认是1
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            print(r.json()['data']['list'][0]['id'])
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_editpage_content_banner(self):
        # 编辑banner内容页面
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.data['id'] = RWYaml(self.Public_path).read_yaml_value('banner', 'content_id')
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, params=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
            print_debug_info('--->pass')
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        