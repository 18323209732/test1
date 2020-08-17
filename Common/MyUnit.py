# coding=utf-8
import base64
import traceback

from Common.ReadWriteIni import ReadWrite

from Common.FontColor import outcome
from Common.DataHandle import SqlHandle,Assertion,Matching
from Common.DataHandle import CaseHandle
import unittest
from Common.GetToken import Get_Cookies
from unittest import TestCase
import json
from Common.MySql import Sql
from Common.Log import MyLog
from Common.ReadYaml import ConfigYaml,CaseYaml
from Common.ReadWriteIni import ReadWrite
from Common.Results import results
import warnings
# from Common.GetToken import getCookie
import re
from Common.MyRedis import ReDis
from Common.DataHandle import SqlHandle,Assertion
from time import sleep
import os
from Common.Route import Any_Path


class MyTest(TestCase):
    def __init__(self, methodName='runTest', param=None):
        TestCase.__init__(self, methodName)
        self.param = param
        self.result = None
        self.time = 0
        self.abnormal = ''

    @classmethod
    def setUpClass(self):
        '''
        :return:
        '''
        self.type = ConfigYaml('type_key').base_config
        self.json_type = ConfigYaml('json_type').base_config
        self.form_type = ConfigYaml('form_type').base_config
        self.cookies_key = ConfigYaml('cookies').base_config
        self.tenant_key = ConfigYaml('tenant_key').base_config
        self.tenant_value = ConfigYaml('tenant_value').base_config
        Get_Cookies().write_cookies()

        self.cookies_value = ReadWrite(sign='session', option='cookies').read_ini_cookies()
        self.headers = {self.cookies_key: self.cookies_value}


    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        '''
        初始化数据
        :return:
        '''
        self.className = self.__class__.__name__
        false_case = self._testMethodName
        try:
            if isinstance(int(false_case.rsplit("_", 1)[1]), int):
                self.casename = false_case.rsplit("_", 1)[0]
        except:
            self.casename = false_case

        self.projectName = ConfigYaml("projectName").base_config
        self.headers.update({self.type: self.json_type})
        case_list = Any_Path(self.projectName)
        case_file = os.listdir(case_list)
        yaml_list = [file for file in case_file if file.endswith(".yaml") and file != "Data.yaml"]
        case_dict = {}
        if yaml_list:
            for file in yaml_list:
                value = CaseYaml(file=file).all_case
                case_dict.update(value)

        self.casedata = case_dict

        if self.casedata:
            self.clsdata,self.fundata = CaseHandle(self.className, self.casename,self.casedata)
        self.sql = ConfigYaml('sql').base_config
        self.redis = ConfigYaml('redis').base_config
        if self.fundata.get('url'):
            self.url = self.fundata.get('url') + f"?{self.tenant_key}={self.tenant_value}"
        else:
            self.url = self.clsdata.get('url') + f"?{self.tenant_key}={self.tenant_value}"
        if self.fundata.get('author'):
            self.author = self.fundata.get('author')
        else:
            self.author = "None"
        if self.fundata.get('case_name'):
            self.notes = self.fundata.get('case_name')
        else:
            self.notes = "None"
        if self.fundata.get('bar'):
            self.data = self.fundata.get('bar')
        else:
            self.data = {}
        if self.fundata.get('level'):
            self.level = self.fundata.get('level')
        else:
            self.level = "中"
        self.test_data = self.fundata.get('test_data')
        self.method = self.fundata.get('mode')
        self.expected = self.fundata.get('expected')


    def tearDown(self):
        try:
            self.actual = Matching("status",self.result)
        except Exception:
            self.actual = 'None'
        try:
            self.msg = Matching("msg",self.result)
        except:
            self.msg = 'None'
        try:
            Assertion(self.result, self.assertEqual, actualone="status",
                      expectone=self.expected[0],
                      ).datahandle()
        except:
            self.abnormal = str(traceback.format_exc())
            outcome('red',self.abnormal)
        resonse = results(
            expected=self.expected[0],
            actual=self.actual,
            parameter=self.data,
            usetime=self.time,
            results=self.result
            )
        Resonse = str(base64.b64encode(str(resonse).encode('utf-8')), 'utf-8')
        if self.sql:
            mysql = SqlHandle(self.casename,self.notes,self.level, self.url, self.abnormal,self.author,self.time, Resonse, self.className)
            mysql.implement()
            mysql.insert_result_table()

        if self.redis:
            data = SqlHandle(self.casename,self.notes,self.level,self.url,self.abnormal,self.author,self.time,Resonse,self.className).data_handle()
            ReDis(data).lpush()



    @staticmethod
    def parametrize(class_name, param=None):
        '''
        :param testcase_klass:
        :param param:
        :return:
        '''
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(class_name)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(class_name(name, param=param))
        return suite

