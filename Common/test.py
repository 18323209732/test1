from functools import wraps
from random import choice
from time import sleep


class ReExecution:

    def __init__(self, fun, status=200, response_key='data', response_list='list', value='id'):
        '''

        :param fun:  回调函数
        :param status:  状态
        :param response_key:  响应data数据键
        :param response_list:  响应列表数据
        :param value:  需要获取的值
        '''

        self.fun = fun
        self.status = status
        self.response_key = response_key
        self.response_list = response_list
        self.value = value

    def __call__(self, method):
        '''
        类装饰器，定义重跑结构
        :param method:
        :return:
        '''

        @wraps(method)
        def wrapper(*args, **kwargs):
            result = method(*args, **kwargs)
            if result.get("status") == self.status:
                if not result.get(self.response_key):
                    self.fun(*args, **kwargs)
                    result = method(*args,**kwargs)
                else:
                    value = choice(result.get(self.response_key))
                    yield value.get(self.value)
        return wrapper


class tt:
    def __init__(self):
        pass

    def jj(self):
        print(1111111111)

    @ReExecution(jj)
    def mm(self):
        list = {"status":200,"msg":"success","success":'true',"data":[]}
        return list


print(next(tt().mm()))