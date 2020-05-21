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
    def __init__(self,filename='config.ini',sign='session',encoding='utf-8',option='token',value=''):
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
        self.dir = Any_Path(self.projectName)
        self.path = Any_Path(self.projectName, self.ini)
        self.config = ConfigParser()
        self.encoding = encoding
        self.option = option
        self.value = value
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)
            with open(self.path,'w'):pass

    def write_ini(self):
        '''
        写入数据到ini文件里面
        :return:
        '''
        try:
            if not self.config.has_section(self.sign):
                self.config.add_section(self.sign)
            self.config.set(section=self.sign,option=self.option,value=self.value)
        except:
            outcome('red', "ini配置文件写入失败")
        with open(self.path,"w",encoding=self.encoding) as f:
            self.config.write(f)
            f.close()

    def read_ini(self):
        '''
        读取ini文件内容，并返回
        :return:
        '''
        try:
            if not self.config.has_section(self.sign):
                self.write_ini()
            content = self.config.get(self.sign, self.option)
            return content
        except:
            outcome('red',"ini配置文件读取失败！")

