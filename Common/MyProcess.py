import unittest, time, os, multiprocessing
from multiprocessing import Process
from multiprocessing import  Lock
from Common.DataHandle import Get_Skip
# from Common.GetPath import second_path,third_path
from Common.ReadYaml import ConfigYaml
from Common.Route import Any_Path
import os


class  MyProcess(Process):
    def __init__(self,catalog,data):
        '''
        继承多进程，重写该方法
        :param catalog: 目录
        '''
        Process.__init__(self)
        self.catalog = catalog
        self.data = data
        self.lock = Lock()

    def run(self):
        '''
        重写run方法
        :return:
        '''
        testsuite = LoadSuite(self.catalog).load_suite()
        runner = unittest.TextTestRunner(verbosity=1)
        self.lock.acquire()
        result = runner.run(testsuite)
        Get_Skip(result.skipped, self.data).get_skip()
        self.lock.release()


class LoadSuite(object):
    def __init__(self,catalog):
        '''
        封装测试集加载类
        :param catalog: 目录
        '''
        self.catalog = catalog
        self.projectName = ConfigYaml("projectName").base_config
        self.path = Any_Path(self.projectName)
        self.matching = ConfigYaml("matching").base_config

    def load_suite(self):
        '''
        加载测试集
        :return:
        '''
        testsuite = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(
            Any_Path(self.projectName,self.catalog),
            pattern=self.matching,top_level_dir=Any_Path(self.projectName)
            )
        for test_suite in discover:
            if test_suite:
                for test_case in test_suite:
                    testsuite.addTests(test_case)
        return testsuite


class RunFailError:

    def __init__(self,classlist,class_case):
        '''
        运行错误率及失败率较高的用例
        '''
        self.classlist = classlist      #类列表
        self.class_case = class_case       #类方法列表
        self.runner = unittest.TextTestRunner(verbosity=1)


    def get_case(self,classname,funname):
        '''
        获取相应的用例
        :param all_data: 类对应的用例
        :return:
        '''
        testsuite = unittest.TestSuite()
        testsuite.addTest(classname(funname))
        return testsuite


    def run_fail_error(self):
        '''
        运行失败或者错误率达到多少的
        :return:
        '''
        global suite
        if self.classlist and self.class_case:
            for fail_error in self.class_case:
                for classname in self.classlist:
                    class_name = str(classname).split('.')[-1].split("'")[0]
                    if fail_error[0] == class_name:
                        self.runner.run(self.get_case(classname,fail_error[1]))



