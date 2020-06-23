from functools import wraps
from random import choice
from time import sleep


class ReExecution:

    def __init__(self, fun):
        '''

        :param fun:  回调函数
        :param status:  状态
        :param response_key:  响应data数据键
        :param response_list:  响应列表数据
        :param value:  需要获取的值
        '''
        # self.fun = fun
        # self.status = status
        # self.response_key = response_key
        # self.response_list = response_list
        self.fun = fun
        # self.status = status
        # self.response_key = response_key
        # self.response_list = response_list

    def __call__(self, method):
        '''
        类装饰器，定义重跑结构
        :param method:
        :return:
        '''

        @wraps(method)
        def wrapper(*args, **kwargs):
            kwargs["response_key"] = 'data'
            kwargs["response_list"] = 'list'
            # kwargs['status'] = status
            result = method(*args)
            if result.get("status") == kwargs.get('status'):
                if not result.get(kwargs.get('response_key')).get(kwargs.get('response_list')):
                    self.fun(*args)
                    result = method(*args)
                    if result.get("status") == kwargs.get('status'):
                        value = result.get(kwargs.get('response_key')).get(kwargs.get('response_list'))
                        yield value.get(kwargs.get('value'))

                else:
                    value = result.get(kwargs.get('response_key')).get(kwargs.get('response_list'))
                    yield value.get(kwargs.get('value'))

        return wrapper

        # @wraps(method)
        # def wrapper(*args, **kwargs):
        #     result = method(*args)
        #     if result.get("status") == self.status:
        #         if not result.get(self.response_key).get(self.response_list):
        #             self.fun(*args)
        #             result = method(*args)
        #             if result.get("status") == self.status:
        #                 value = choice(result.get(self.response_key).get(self.response_list))
        #                 yield value.get(kwargs.get('value'))
        #
        #         else:
        #             value = choice(result.get(self.response_key).get(self.response_list))
        #             yield value.get(kwargs.get('value'))
        #
        # return wrapper


# def yy():
#     print(1111111)
#
#
# @ReExecution(yy)
# # tt = ReExecution(yy)
# def ff():
#     r = {"status": 200, "msg": "success", "data": {"list": [{"atlasNum": 0, "id": 1, "mobileStatus": "显示", "name": "lhj1", "nodeType": 0, "pId": 0, "pageId": "-1","pcStatus": "显示", "type": 1}]}}
#     return r
# # tt(ff,value=11)
# print(next(ff(value="mobileStatus")))