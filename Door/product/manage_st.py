# coding=utf-8
import unittest
import traceback
import requests
from Common.FontColor import outcome
from Common.MyUnit import MyTest
from Common.ReadYaml import ConfigYaml
from Common.DataHandle import ReRun

class manage_product(MyTest):

    condition = True
    # 产品列表 22222222

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_product33_getlist(self):
        # 产品列表111111
        try:
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True)
            self.result = r.json()

            self.time=r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular
        