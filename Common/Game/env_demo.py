import requests


class Api:

    env = {
        "default":"dev",
        "testing.studio":
        {
            "dev":"127.0.0.1",
            "test":"127.0.0.2"
        }
    }

    data = {
        "method":"get",
        "url":"http://testing.studio:8888",
        "headers":None
    }

    #data是一个请求的信息
    def send(self,data:dict):
        #替换
        data["url"] = str(data["url"]).replace("testing.studio",self.env["testing.studio"][self.env["default"]])
        requests.request(method=data["method"],url=data["url"],headers=data["headers"])