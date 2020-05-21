# coding=utf-8
import subprocess
from datetime import datetime,date,timedelta
from Common.Route import Any_Path
from Common.ReadYaml import ConfigYaml
import os


def results(**kwargs):
    '''

    :param kwargs:
    :return:
    '''
    return kwargs

def cmd(cmd):
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return p.stdout.read().decode('gbk')


class Delete_file(object):

    def __init__(self):
        '''

        '''
        self.days = ConfigYaml('backupCount').base_config    #最大保留天数
        self.log = ConfigYaml('Log').base_config             #log日志文件目录名
        self.path = Any_Path(self.log)                      #日志路径
        self.logname = '{}.log'                               #日志文件

    def get_dir(self):
        '''
        获取目录列表
        :return:
        '''

        return os.listdir(self.path)

    def getdate(self,data):
        '''
        获取日期
        :param data:
        :return:
        '''
        return (datetime.now() + timedelta(days=-data)).strftime('%Y-%m-%d')

    def beforedata(self):
        '''
        :return:
        '''
        files = [self.getdate(index) for index in range(self.days)]
        if files:
            for file in self.get_dir():
                if file.split('.')[0] not in files:
                    os.remove(Any_Path(self.log, file))

