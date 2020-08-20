
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
from Door.news.Public import Public_Data as pub_news


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

        img_url = next(pub_news().get_pictures(value='imgUrl'))
        id = next(picture().picture_name(value='id'))

        data['commonAtlasName'] = random_str("自动化企业图册...")
        data['commonAtlasDescription'] = random_str("<p>自动化企业图册详细内容数据...</p>\n")
        data['commonAtlasSummary'] = random_str("自动化企业图册描述数据...")
        data['keywords'] = random_str("关键词...")
        data["atlasImgs"][0]['id'] = id
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

        img_url = next(pub_news().get_pictures(value='imgUrl'))
        img_id = next(pub_news().get_pictures(value='id'))
        data['atlasCategory']['name'] = random_str("自动化企业图册分类...")
        data['atlasCategory']['imgUrl'] = img_url
        data['atlasCategory']['imgId'] = img_id
        data['atlasCategory']['keywords'] = random_str("关键词...")
        data['atlasCategory']["imgThumbUrl"] = img_url
        data['atlasCategory']["des"] = random_str("自动化企业图册分类描述内容...")
        data['atlasCategory']["summary"] = random_str("自动化企业图册分类描述内容...")
        self.headers[self.type] = self.json_type

        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)

    @ReExecution(add_atlas, status=200, response_list="pres")
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

        return result

    @ReExecution(add_class, status=200)
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

        return result


    @ReExecution(file_upload, status='200', response_list='list')
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

        return result

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
        img_url = next(Public_Data().get_pictures(value='imgUrl'))

        data['name'] = random_str("自动化新增分类...")
        data['des'] = random_str("<p>自动化新增分类描述数据...</p>\n")
        data['imgUrl'] = img_url
        data['imgThumbUrl'] = img_url
        data['imgThumbUrl'] = img_url
        data['summary'] = random_str("自动化新增分类来源数据...")
        data['keywords'] = random_str("关键词...")
        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)

    @ReExecution(add_classnews, response_list='data')  # value='id'
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

        return result

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

        id = str(next(Public_Data().get_news_class(value='id')))
        data['title'] = random_str("自动化新增新闻资讯")
        data['content'] = random_str("<p>自动化新增新闻资讯内容....</p>\n")
        data['infotype'] = id
        data['cateGoryIds'] = id

        r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)


    @ReExecution(add_news, response_list='pres')
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

        return result

    @ReExecution(file_upload, status='200')   #imgUrl
    def picture_name(self):
        '''
        获取新闻资讯列表数据
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='atlas', key="picture_url")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}&pageSize=15&currentPage=1&queryStatus=&startDate=&endDate=&name=&classId="
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.get(url, headers=self.headers, json=data, stream=True, verify=False)
        result = r.json()

        return result

# if __name__=="__main__":
#     print(next(Public_Data().get_class(value='id')))
    # pass