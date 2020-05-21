import re
from Common.Abnormal import RepeatClass,RepeatCase
from Common.ReadYaml import ConfigYaml,CaseYaml
import os,re
from  Common.GetPath import second_path,third_path
from Common.FontColor import outcome
from Common.Template import case_data
from Common.MySql import Sql


class BatchProcess(object):

    '''
    批处理文件自动检索文件，发现文件异常
    '''

    def __init__(self,encoding='utf-8',casefile='Case.yaml',datafile='Data.yaml'):

        '''
        初始化数据内容
        :param encoding:
        '''
        self.encoding = encoding
        self.casefile = casefile
        self.projectName = ConfigYaml('projectName').base_config
        self.init = "__init__.py"
        self.datafile = datafile
        if self.projectName:
            self.init_path = second_path(self.projectName, self.init)
            self.project_path = second_path(dir=self.projectName)
            self.case_path = second_path(self.projectName, self.casefile)
            self.data_path = second_path(self.projectName,self.datafile)
            if not os.path.exists(self.project_path):
                os.makedirs(self.project_path)
            if not os.path.exists(self.init_path):
                with open(self.init_path, 'w'):pass
            if not os.path.exists(self.data_path):
                with open(self.data_path, 'w'):pass
            if not os.path.exists(self.case_path):
                with open(self.case_path,"w",encoding=self.encoding) as f :
                    f.write(case_data%(self.projectName))
                    f.close()

        else:
            outcome('red',f'请检查配置文件是否存在{self.projectName}....')

        self.data = CaseYaml().all_case

    def check_file(self):

        '''
        检查用例文件编写的所有用例是否符合要求
        :return:
        '''

        with open(self.case_path,'r',encoding=self.encoding) as f:
            content = f.readlines()
            f.close()

        with open(self.data_path,'w',encoding=self.encoding) as f:
            for index,value in enumerate(content):
                if "name:" in value and 'case_name' not in value:
                    name = value.replace('name:','modular:')
                    f.writelines(name)
                elif 'test_data:' in value:
                    relation_data = value.replace('test_data', 'relation_data')
                    f.writelines(relation_data)
                else:
                    if 'test_' in value and '{' in value:
                        self.index = index
                        f.writelines(value)
                        if 'bar:' in content[self.index+1]:
                            content.insert(self.index + 1, ' ' * 10 + 'level: 中,\n')
                            content.insert(self.index + 2, ' ' * 10 + 'author: 陈建波,\n')
                        if 'url:' in content[self.index+1]:
                            content.insert(self.index+2, ' '*10 + 'level: 中,\n')
                            content.insert(self.index + 3, ' ' * 10 + 'author: 陈建波,\n')
                    else:
                        f.writelines(value)

