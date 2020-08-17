# coding=utf-8
import unittest
import traceback
import requests
from Common.FontColor import outcome
from Common.MyUnit import MyTest
from Common.ReadYaml import ConfigYaml
from Common.DataHandle import ReRun
import urllib3
from ddt import ddt, data,file_data
from Common.ReExecution import Get_Cls_Fun


@ddt
class customer_customer_manage(MyTest):

    condition = True
    type_condition = False
    # 客户管理

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_customer_list(self):
        # 客户列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.type_condition = True
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
        