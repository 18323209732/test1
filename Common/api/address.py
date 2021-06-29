from api.base_api import BaseApi
from api.wework import WeWork


class Address(BaseApi):

    def __init__(self):
        secrete = "iqlhZWi7pbDSfTd0gOP0NTMG9ncVTu6x6Tl87Oyw6fM"
        self.token = WeWork().get_token(secrete)

    def get(self,userid):
        data = {
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params":{
                "access_token":{self.token},
                "userid": userid
            }
        }
        return self.send(data)

    def create(self,userid, name, mobile):
        # 创建成员
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params":{
                "access_token":{self.token}
            },
            "json":{
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": [1]
        }
        }
        return self.send(data)

    def update(self,userid, name, mobile):
        # 更新成员信息
        data = {
            "method":"post",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params":{
                "access_token":{self.token}
            },
            "json":{
                "userid": userid,
                "name": name,
                "mobile": mobile,
            }
        }
        return self.send(data)

    def delete(self,userid):
        # 删除成员
        data = {
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params":{
                "access_token":{self.token},
                "userid":userid
            }
        }
        return self.send(data)

