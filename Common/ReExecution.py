import unittest
from functools import wraps
from random import choice
from time import sleep

import requests
import urllib3
from ddt import ddt,data

from Common.DataHandle import Get_Data
from Common.ReadYaml import CaseYaml, ConfigYaml


class ReExecution:

    def __init__(self, fun, status=200, response_key='data', response_list='list', swich=True, isuse=0, key=''):
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
        self.swich = swich
        self.isuse = isuse
        self.key = key

    def __call__(self, method):
        '''
        类装饰器，定义重跑结构
        :param method:
        :return:
        '''
        @wraps(method)
        def wrapper(*args, **kwargs):
            result = method(*args)
            if result.get("status") == self.status:
                if self.response_list:
                    if not result.get(self.response_key).get(self.response_list):
                        self.fun(*args)
                        result = method(*args)
                        if result.get("status") == self.status:
                            if self.swich:
                                value = choice(result.get(self.response_key).get(self.response_list))
                                yield value.get(kwargs.get('value'))

                            else:
                                data_list = result.get(self.response_key).get(self.response_list)
                                for value in data_list:
                                    if value.get(self.key) != self.isuse:
                                        yield value.get(kwargs.get('value'))
                                # value = choice(result.get(self.response_key).get(self.response_list))
                                # if value.get(self.key) == self.isuse:
                                #     yield value.get(kwargs.get('value'))

                    else:
                        if self.swich:
                            value = choice(result.get(self.response_key).get(self.response_list))
                            yield value.get(kwargs.get('value'))

                        else:
                            data_list = result.get(self.response_key).get(self.response_list)
                            for value in data_list:
                                if value.get(self.key) != self.isuse:
                                    yield value.get(kwargs.get('value'))
                            # value = choice(result.get(self.response_key).get(self.response_list))
                            # if value.get(self.key) == self.isuse:
                            #     yield value.get(kwargs.get('value'))

                else:

                    if not result.get(self.response_key):
                        self.fun(*args)
                        result = method(*args)
                        if result.get("status") == self.status:
                            if self.swich:
                                value = choice(result.get(self.response_key))
                                yield value.get(kwargs.get('value'))

                            else:
                                data_list = result.get(self.response_key)
                                for value in data_list:
                                    if value.get(self.key) != self.isuse:
                                        yield value.get(kwargs.get('value'))
                                # value = choice(result.get(self.response_key))
                                # if value.get(self.key) == self.isuse:
                                #     yield value.get(kwargs.get('value'))
                    else:
                        if self.swich:
                            value = choice(result.get(self.response_key))
                            yield value.get(kwargs.get('value'))

                        else:
                            data_list = result.get(self.response_key).get(self.response_list)
                            for value in data_list:
                                if value.get(self.key) != self.isuse:
                                    yield value.get(kwargs.get('value'))
                            # value = choice(result.get(self.response_key))
                            # if value.get(self.key) == self.isuse:
                            #     yield value.get(kwargs.get('value'))

        return wrapper


def Get_Cls_Fun(fun):
    '''
    动态获取类名及方法名
    :param fun:
    :return:
    '''

    cla_name = str(fun).split(" ")[1].split(".")[0]    #类名
    fun_name = fun.__name__        #方法名
    datas = CaseYaml().all_case    #数据
    value = Get_Data(cla_name, fun_name, datas)   #对应用例数据

    @data(*value)
    @wraps(fun)
    def Inner(*args, **kwargs):
        '''
        :param args:
        :param kwargs:
        :return:
        '''
        fun(*args, **kwargs)

    return Inner

