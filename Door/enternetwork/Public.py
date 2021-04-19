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
from Common.ReExecution import ReExecution
from Common.ReadWriteIni import ReadWrite
from Common.ReadYaml import ReadPublic, ConfigYaml
from Common.Route import Any_Path

projectName = ConfigYaml("projectName").base_config
from Door.newsclass.newsmanage_st import pb_data, my_data

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

    def networke_add(self):
        '''
        获取新闻资讯分类数据
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='enternetwork', key="networke_add")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")

        if not pb_data.picture_ids:
            pb_data.picture_ids = my_data.get_picture_ids()
            value = choice(pb_data.picture_ids)
        else:
            value = choice(pb_data.picture_ids)
        # print(self.headers)
        img_id = value.get("id")
        img_url = value.get("imgUrl")
        name = value.get("name")
        data['images'][0]["imgId"] = img_id
        data['images'][0]["url"] = img_url
        data['images'][0]["thumbId"] = img_id
        data['images'][0]["imgUrl"] = img_url
        data['images'][0]["imageName"] = name
        data['name'] = random_str("自动化新增企业网点")
        data['description'] = random_str("<p>自动化新增企业网点详情数据....</p>\n")
        data['keywords'] = random_str("自动化新增企业网点关键词")
        data['summary'] = random_str("自动化新增企业网点描述")
        print(data)
        # data = f"""name={random_str('自动化新增企业网点')}&categoryId=2&locaJson=[]&cityName=成都市&provinceName=四川省&districtName=锦江区&address=天府半岛&lng=104&lat=30&zipCode=&website=&wechat=&statu=1&syncStatu=&images=[{'imgId':{img_id},'url': {img_url},'thumbId':{img_id},'imgUrl': '{img_url}','imageName'':'{name}','iscover'':1,'sequence'':'','height'':'','wide'':''}]&description=random_str('<p>自动化新增企业网点详情数据....</p>\n')&mobileDesc=&keywords=&cardId=&mobileStatu=1&seoAuto=true&viewCount=568&seoTitle=[{'id':'name','name':'网点名称'},{'id':'siteName','name':'网站名称'}]&seoTitleSign=_&seoKeywords=[{'id':'keyword','name':'网点关键词'},{'id':'name','name':'网点关键词'},{'id':'siteName','name':'网点名称'}]&seoKeywordsSign=,&seoDescription=[{'id':'name','name':'网点名称'},{'id':'siteName','name':'网点名称'},{'id':'summary','name':'网点概要'}]&seoDescriptionSign=-&seoAddDescription=undefined&logoUrl={img_url}&logoId={img_id}&fullAddress=成都市锦江区&summary=&locationArray=[]&citys=['四川省','成都市'','锦江区']&relationListJson=[{'appId':11,'appName'':'企业网点','contentList'':[]}]"""

        r = requests.post(url, headers=self.headers, data=data, stream=True, verify=False)
        print(r.json())


    def get_news_ids(self):
        '''
        获取新闻id
        :return:
        '''

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.public_data = ReadPublic(catalog='enternetwork', key="networke_list")
        url = self.public_data.public_value("url") + f"?{self.tenant_key}={self.tenant_value}"
        url = self.url + url
        data = self.public_data.public_value("bar")
        r = requests.get(url, headers=self.headers, json=data, stream=True, verify=False)
        result = r.json()
        if result.get("data").get("pres"):
            return result.get("data").get("pres")
        else:
            self.add_news()
            r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
            result = r.json()
            if result.get("data").get("pres"):
                return result.get("data").get("pres")
            else:
                return False

if __name__=="__main__":
    Public_Data().networke_add()