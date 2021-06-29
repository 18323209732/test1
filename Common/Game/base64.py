import base64
import json

import requests


class ApiRequset:

    req_data={
        "method":"get",
        "url":"http://127.0.0.1:8888",
        "headers":None,
        "encoding":"base64"
    }

    def send(self,data:dict):
        res = requests.request(data["mothod"],data["url"],headers = data["headers"])
        if data["encoding"] == "base64":
            return json.loads(base64.b64decode(res.content))
        #把加密后的响应值发给第三方服务；让第三方做解密然后返回
        elif data["encoding"] == "private":
            return requests.post("url",data=res.content)
