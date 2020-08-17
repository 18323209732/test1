import yaml
# from Common.GetPath import second_path
from Common.FontColor import outcome
from Common.Route import Any_Path
import os
current_dir = os.getcwd().split("\\")[-1]


class ConfigYaml:
    def __init__(self, key=None, dir="Config", file='Config.yaml', encoding='utf-8'):
        '''
        :param key:
        :param dir:
        :param file:
        :param encoding:
        '''
        self.key = key
        self.file = file
        self.dir = dir
        self.encoding = encoding

    @property
    def config_data(self):
        """读取yaml里所有的内容"""
        self.path = Any_Path(self.dir, self.file)
        if os.path.exists(self.path):
            f = open(self.path, encoding=self.encoding)
            data = yaml.load(f)
            f.close()
            return data
        else:
            outcome('red', f"请检此路径:{self.path},下的用例文件是否存在")

    @property
    def base_config(self):
        '''

        :return:
        '''
        return self.config_data.get('base_config').get(self.key)

    @property
    def base_url(self):
        '''

        :return:
        '''
        return self.config_data.get('base_url').get(self.key)

    @property
    def email(self):
        '''

        :return:
        '''
        return self.config_data.get('email').get(self.key)

    @property
    def sql(self):
        '''

        :return:
        '''
        return self.config_data.get('sql').get(self.key)

    @property
    def report(self):
        '''

        :return:
        '''
        return self.config_data.get('report').get(self.key)

    @property
    def wechat(self):
        '''

        :return:
        '''
        return self.config_data.get('wechat').get(self.key)


class CaseYaml:
    def __init__(self, key=None, file='Case.yaml', encoding='utf-8'):
        '''

        :param key:
        :param file:
        :param encoding:
        '''
        self.key = key
        self.file = file
        self.dir = ConfigYaml(key='projectName').base_config
        self.encoding = encoding


    @property
    def case_data(self):
        """读取yaml里所有的内容"""
        self.path = Any_Path(self.dir, self.file)
        if os.path.exists(self.path):
            f = open(self.path, encoding=self.encoding)
            data = yaml.load(f)
            f.close()
            return data
        else:
            outcome('red', f"请检此路径:{self.path},下的用例文件是否存在")


    @property
    def all_case(self):
        '''

        :return:
        '''
        return self.case_data.get(self.dir)

    @property
    def class_data(self):
        '''

        :return:
        '''
        return self.all_case.get(self.key)


class ReadPublic:
    def __init__(self, catalog='', key='', file='Public.yaml', encoding='utf-8'):
        '''

        :param key:
        :param file:
        :param encoding:
        '''
        self.key = key
        self.file = file
        self.dir = ConfigYaml(key='projectName').base_config
        self.catalog = catalog
        self.encoding = encoding


    @property
    def public_data(self):
        """读取yaml里所有的内容"""
        self.path = Any_Path(self.dir, self.catalog, self.file)
        if os.path.exists(self.path):
            f = open(self.path, encoding=self.encoding)
            data = yaml.load(f)
            f.close()
            return data
        else:
            outcome('red', f"请检此路径:{self.path},下的用例文件是否存在")
    @property
    def key_value(self):
        '''
        :return:
        '''
        return self.public_data.get(self.key)



    def public_value(self,value):
        '''
        :return:
        '''
        return self.key_value.get(value)




