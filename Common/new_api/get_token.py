#在new_api package中是代表所有的接口信息的实现。使用一个公共方法代表一个接口
import yaml

from new_api.base_api import BaseApi

from string import Template


class GetToken(BaseApi):

    _corpid = "wwdbf78b1014ed2f3b"
    _corp_secret = "iqlhZWi7pbDSfTd0gOP0NUYd5r8P_LcfvUWYNIp5PfI"

    def template(self):
        with open("../new_api/get_token.yaml") as f:
            data = {
                "corpid":self._corpid,
                "corpsecret":self._corp_secret
            }
            re = Template(f.read()).substitute(data)
            return yaml.safe_load(re)

    def get_token(self):
    # 1.把请求信息转化为一个规范的字典结构体

        req = self.template()
        r = self.requests_http(req)
        print(r.json())
        return r