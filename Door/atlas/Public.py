
# coding=utf-8
import requests
from random import randint,choice
import random,os,re
import json
import requests
import time
from random import randint
from datetime import date,timedelta
import urllib3
from Common.CusMethod import random_str
from Common.GetToken import Get_Cookies
from Common.ReadWriteIni import ReadWrite
from Common.ReadYaml import ReadPublic, ConfigYaml
from Common.Route import Any_Path

projectName = ConfigYaml("projectName").base_config
from Common.ReExecution import ReExecution
from Door.picture.Public import Public_Data as picture


picture_pd = picture()
picture_ids = picture_pd.get_picture_ids()

picture_data = type("picture_data", (object,), {})
setattr(picture_data, "picture_ids", picture_ids)


class Public_Data:
    def __init__(self):
        '''
        '''
        self.type = ConfigYaml('type_key').base_config
        self.form_type = ConfigYaml('form_type').base_config
        self.cookies_key = ConfigYaml('cookies').base_config
        self.json_type = ConfigYaml('json_type').base_config
        self.cookies_value = ReadWrite(sign='session', option='cookies').read_ini_cookies()
        self.headers = {self.type: self.form_type}
        self.headers.update({self.cookies_key: self.cookies_value})
        self.projectName = ConfigYaml("projectName").base_config
        self.url = ConfigYaml(projectName).base_url
        self.tenant_key = ConfigYaml('tenant_key').base_config
        self.tenant_value = ConfigYaml('tenant_value').base_config

    def add_atlas(self):
        '''
        添加分类
        :return:
        '''
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='atlas', key="add_atlas")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")

        if not picture_data.picture_ids:
            picture_data.picture_ids = picture_pd.get_picture_ids()
            value = choice(picture_data.picture_ids)
        else:
            value = choice(picture_data.picture_ids)
        if not class_data.get_class:
            class_data.get_class = class_pd.get_class()
            id_ = choice(class_data.get_class).get("id")
        else:
            id_ = choice(class_data.get_class).get("id")
        img_url = value.get("imgUrl")
        id = value.get("id")
        name = value.get("name")
        data['commonAtlasName'] = random_str("自动化企业图册...")
        data['commonAtlasDescription'] = random_str("<p>自动化企业图册详细内容数据...</p>\n")
        data['commonAtlasSummary'] = random_str("自动化企业图册描述数据...")
        data['keywords'] = random_str("关键词...")
        data['atlasCategoryArr'] = [f"{id_}"]
        data["atlasImgs"][0]['id'] = f"{id}"
        data["atlasImgs"][0]['imgId'] = f"{id}"
        data["atlasImgs"][0]['thumbId'] = f"{id}"
        data["atlasImgs"][0]['name'] = name
        data["atlasImgs"][0]['relativeImgUrl'] = img_url
        data["atlasImgs"][0]['imgUrl'] = img_url
        data["atlasImgs"][0]['thumbUrl'] = img_url
        data["atlasImgs"][0]['relativeThumbUrl'] = img_url

        self.headers[self.type] = self.json_type
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)



    def file_upload(self):
        '''
        添加新闻资讯
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        file_path = Any_Path("File", "picture.jpg")
        del self.headers[self.type]
        f = open(file_path, "rb")
        file = {"file": f}
        self.public_data = ReadPublic(catalog='atlas', key="file_upload")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, data=data, files=file, stream=True, verify=False)


    def add_class(self):
        '''
        添加分类
        :return:
        '''
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='atlas', key="add_class")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")

        if not picture_data.picture_ids:
            picture_data.picture_ids = picture_pd.get_picture_ids()
            value = choice(picture_data.picture_ids)
        else:
            value = choice(picture_data.picture_ids)


        img_url = value.get("imgUrl")
        img_id = value.get("id")

        data['atlasCategory']['name'] = random_str("自动化企业图册分类...")
        data['atlasCategory']['imgUrl'] = img_url
        data['atlasCategory']['imgId'] = img_id
        data['atlasCategory']['keywords'] = random_str("关键词...")
        data['atlasCategory']["imgThumbUrl"] = img_url
        data['atlasCategory']["des"] = random_str("自动化企业图册分类描述内容...")
        data['atlasCategory']["summary"] = random_str("自动化企业图册分类描述内容...")
        self.headers[self.type] = self.json_type

        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)

    # @ReExecution(add_atlas, status=200, response_list="pres")
    def get_atlas(self):
        '''
        获取新闻资讯列表数据
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='atlas', key="get_atlas")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        self.headers[self.type] = self.json_type
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
        result = r.json()
        if result.get("data").get("pres"):
            return result.get("data").get("pres")
        else:
            self.add_atlas()
            r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
            result = r.json()
            if result.get("data").get("pres"):
                return result.get("data").get("pres")
            else:
                return False


    # @ReExecution(add_class, status=200)
    def get_class(self):
        '''
        获取新闻资讯列表数据
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='atlas', key="get_class")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        r = requests.get(url, headers=self.headers, stream=True, verify=False)
        result = r.json()

        if result.get("data").get("list"):
            return result.get("data").get("list")
        else:
            self.add_class()
            r = requests.post(url, headers=self.headers, stream=True, verify=False)
            result = r.json()
            if result.get("data").get("list"):
                return result.get("data").get("list")
            else:
                return False

    def get_pictures(self):
        '''
        获取新闻资讯分类数据
        :return:
        '''
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='atlas', key="get_picture")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.get(url, headers=self.headers, data=data, stream=True, verify=False)
        result = r.json()
        if result.get("data").get("list"):
            return result.get("data").get("list")
        else:
            self.file_upload()
            r = requests.post(url, headers=self.headers, data=data, stream=True, verify=False)
            result = r.json()
            if result.get("data").get("list"):
                return result.get("data").get("list")
            else:
                return False

    def add_classnews(self):
        '''
        添加分类
        :return:
        '''
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='atlas', key="add_classnews")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        self.headers[self.type] = self.json_type

        data = self.public_data.public_value("bar")
        if not picture_data.picture_ids:
            picture_data.picture_ids = picture_pd.get_picture_ids()
            img_url = choice(picture_data.picture_ids).get("imgUrl")
        else:
            img_url = choice(picture_data.picture_ids).get("imgUrl")

        data['name'] = random_str("自动化新增分类...")
        data['des'] = random_str("<p>自动化新增分类描述数据...</p>\n")
        data['imgUrl'] = img_url
        data['imgThumbUrl'] = img_url
        data['imgThumbUrl'] = img_url
        data['summary'] = random_str("自动化新增分类来源数据...")
        data['keywords'] = random_str("关键词...")
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)

    # @ReExecution(add_classnews, response_list='data')  # value='id'
    def get_news_class(self):
        '''
        获取新闻资讯分类数据
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='atlas', key="get_news_class")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
        result = r.json()

        if result.get("data").get("data"):
            return result.get("data").get("data")
        else:
            self.add_classnews()
            r = requests.post(url, headers=self.headers, data=data, stream=True, verify=False)
            result = r.json()
            if result.get("data").get("data"):
                return result.get("data").get("data")
            else:
                return False

    def add_news(self):
        '''
        获取新闻资讯分类数据
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='atlas', key="add_news")
        self.headers[self.type] = self.json_type
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")

        if not class_data.class_ids:
            class_data.class_ids = class_pd.get_news_class()
            id_ = choice(class_data.class_ids).get("id")
        else:
            id_ = choice(class_data.class_ids).get("id")

        data['title'] = random_str("自动化新增新闻资讯")
        data['content'] = random_str("<p>自动化新增新闻资讯内容....</p>\n")
        data['infotype'] = id_
        data['cateGoryIds'] = id_

        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)


    # @ReExecution(add_news, response_list='pres')
    def get_news_id(self):
        '''
        获取新闻资讯列表数据
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='atlas', key="get_news")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
        result = r.json()
        if result.get("data").get("pres"):
            return result.get("data").get("pres")
        else:
            self.add_news()
            r = requests.post(url, headers=self.headers, data=data, stream=True, verify=False)
            result = r.json()
            if result.get("data").get("pres"):
                return result.get("data").get("pres")
            else:
                return False


class_pd = Public_Data()
class_ids = class_pd.get_news_class()
get_class = class_pd.get_class()
class_data = type("class_data", (object,), {})
setattr(class_data, "class_ids", class_ids)
setattr(class_data, "get_class", get_class)

