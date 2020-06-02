# coding=utf-8
import os
from configparser import  ConfigParser
# from Common.GetPath import second_path
from Common.Route import Any_Path
from Common.ReadYaml import ConfigYaml
from Common.FontColor import outcome


class ReadWrite:
    '''
    ini文件读写
    '''
    def __init__(self, filename='config.ini', sign='session', encoding='utf-8',
                 option='token', value='', time_sign='time', time_option='times',
                 time_value=''):
        '''
        :param filename: 文件名
        :param sign: 标识
        :param encoding:
        :param option: 键
        :param value: 值
        '''
        self.projectName = ConfigYaml('projectName').base_config
        self.ini = filename
        self.sign = sign
        self.time_sign = time_sign
        self.time_option = time_option
        self.time_value = time_value
        self.dir = Any_Path(self.projectName)
        self.path = Any_Path(self.projectName, self.ini)
        self.config = ConfigParser()
        self.encoding = encoding
        self.option = option
        self.value = value
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)
            with open(self.path, 'w'):pass

    def write_ini(self):
        '''
        写入数据到ini文件里面
        :return:
        '''
        try:
            if not self.config.has_section(self.sign):
                self.config.add_section(self.sign)
            self.config.set(section=self.sign, option=self.option, value=self.value)

            if not self.config.has_section(self.time_sign):
                self.config.add_section(self.time_sign)
            self.config.set(section=self.time_sign, option=self.time_option, value=self.time_value)
        except:
            outcome('red', "ini配置文件写入失败")
        with open(self.path, "w", encoding=self.encoding) as f:
            self.config.write(f)
            f.close()

    def read_ini_cookies(self):
        '''
        读取ini文件内容，并返回
        :return:
        '''

        try:
            self.config.read(self.path)
            content = self.config.get(self.sign, self.option)
            return content
        except:
            outcome('red', "ini配置文件读取【cookies】失败！")

    def read_ini_time(self):
        '''
        读取ini文件内容，并返回
        :return:
        '''

        try:
            self.config.read(self.path)
            content = self.config.get(self.time_sign, self.time_option)
            return content
        except:
            outcome('red', "ini配置文件读取【time】失败！")

