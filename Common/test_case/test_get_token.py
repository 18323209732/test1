import pytest
import requests
# testcase是以pytest为测试框架，一个method 就是一个case
import yaml
from test_case.test_base import TestBase

from new_api.get_token import GetToken


class TestToken(TestBase):
    def setup(self):
        # self.gettoken = GetToken()
        pass
    #@pytest.mark.parametrize("get_token",yaml.safe_load(open("../new_api/get_token.yaml")))
    def test_get_token(self):
        print(self.gettoken.get_token().json())
        assert self.gettoken.get_token().json()["errcode"] == 0