# coding=utf-8
import unittest
import traceback
import requests
from Common.FontColor import outcome
from Common.MyUnit import MyTest
from Common.ReadYaml import ConfigYaml
from Common.DataHandle import ReRun
import urllib3
import time, yaml, os
from ruamel.yaml import RoundTripDumper
from Common.Route import Any_Path
from Door.AddCategory.Public import writeyaml


class manage_AddCategory(MyTest):
    condition = True

    # 添加产品分类,然后获取分类列表，验证创建分类是否存在

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_add_category(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        # 添加产品分类
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            self.data['category']['categoryName'] = '分类%s' % time.time()  # 获取随机分类名称
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            writeyaml(w_key='categoryName', w_value=self.data['category']['categoryName'], n='w', file="Door\AddCategory")


            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_category_list(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        # 获取产品分类列表
        try:
            url = ConfigYaml(self.projectName).base_url + self.url + '&appId=2'
            r = requests.get(url, headers=self.headers, stream=True, verify=False)
            self.result = r.json()

            try:
                path = Any_Path("Door\AddCategory", "Public.yaml")
                with open(path, 'r', encoding='utf-8') as f:  # 读取Public.yaml中'categoryName'的值
                    value = yaml.load(f.read(), Loader=yaml.Loader)['categoryName']
                    # print(self.result['data'])
                    for i in self.result['data']:  # 循环判断分类列表名称与存入的是否一致
                        if i['categoryName'] == value:
                            id = i['id']
                            writeyaml(w_key='id', w_value=id, n='a', file= "Door\AddCategory")

            except:
                self.singular = str(traceback.format_exc())
                outcome('red', self.singular)
                return self.singular

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
