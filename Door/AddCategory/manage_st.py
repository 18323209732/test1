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

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


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
            # url = 'https://2003275126-stsite-oper.pool601.yun300.cn/manager/gwforward/manager-webapi/product/appCategory/save?viewType=1&tenantId=185569&authPermission=classify_update&_d=1592381386593'
            self.data['category']['categoryName'] = '分类%s' % time.time()  # 获取随机分类名称
            # self.headers[self.cookies_key]='GWSESSION=OTRmODM2MDktZDc3ZC00OTI3LWE3MTAtMTNkNzA1ZjllMzgx'
            # print(url)
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()
            with open("Public.yaml", "w", encoding="utf-8") as yaml_file:  # 把传入的分类名称存入Public.yaml
                data = {'categoryName': self.data['category']['categoryName']}
                yaml.dump(data, yaml_file, Dumper=RoundTripDumper, allow_unicode=True)
            # print(self.data['category']['categoryName'])

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
            url = ConfigYaml(self.projectName).base_url + self.url + '&pid=0&appId=2'
            r = requests.get(url, headers=self.headers, stream=True, verify=False)
            self.result = r.json()
            # print(self.result)
            try:
                # path = os.path.dirname(os.path.realpath(__file__))+r"\Public.yaml"
                with open('Public.yaml', 'r', encoding='utf-8') as f:  # 读取Public.yaml中'categoryName'的值
                    value = yaml.load(f.read(), Loader=yaml.Loader)['categoryName']
                    # print(value)
                    for i in self.result['data']:  # 循环判断分类列表名称与存入的是否一致
                        if i['categoryName'] == value:
                            # print(i['categoryName'])
                            id = i['id']
                            with open("Public.yaml", "a", encoding="utf-8") as yaml_file:  # 把传入的分类名称存入Public.yaml
                                data = {'id': id}
                                yaml.dump(data, yaml_file, Dumper=RoundTripDumper, allow_unicode=True)

            except:
                self.singular = str(traceback.format_exc())
                outcome('red', self.singular)
                return self.singular

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
