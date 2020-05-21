import re
import warnings

from Common.Abnormal import RepeatClass,RepeatCase
from Common.ReadYaml import ConfigYaml,CaseYaml
import os
# from  Common.GetPath import second_path,third_path
from Common.Route import Any_Path
from Common.FontColor import outcome
from Common.Template import case_data,case_body,class_title,pypublic,publicyaml


class Initialization(object):


    def __init__(self,encoding='utf-8',casefile='Case.yaml',datafile='Data.yaml'):

        '''
        初始化数据内容
        :param encoding:
        '''
        self.encoding = encoding
        self.publicyaml = "Public.yaml"
        self.publicpy = "Public.py"
        self.init = "__init__.py"
        self.projectName = ConfigYaml('projectName').base_config
        self.re = ConfigYaml('matching').base_config
        self.casefile = casefile
        self.datafile = datafile
        if self.projectName:
            self.init_path = Any_Path(self.projectName, self.init)
            self.project_path = Any_Path(self.projectName)
            self.case_path = Any_Path(self.projectName, self.casefile)
            self.data_path = Any_Path(self.projectName, self.datafile)
            if not os.path.exists(self.project_path):
                os.makedirs(self.project_path)
            if not os.path.exists(self.init_path):
                with open(self.init_path, 'w'):pass
            if not os.path.exists(self.data_path):
                with open(self.data_path, 'w'):pass
            if not os.path.exists(self.case_path):
                with open(self.case_path,"w",encoding=self.encoding) as f :
                    f.write(case_data%(self.projectName))
        else:
            outcome('red',f'请检查配置文件是否存在{self.projectName}....')

        self.data = CaseYaml().all_case


    def search_pyfun(self,module,pyfile):

        '''
        查找py用例文件方法名
        :param module: 目录名
        :param pyfile:  文件名
        :return:
        '''

        file_path = Any_Path(self.projectName,module,pyfile)
        funlist = []
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding=self.encoding) as f:
                for line in f:
                    if "#" not in line:
                        fun = re.findall("def (.*?)\\(self\\):", line)
                        if fun and fun[0]:
                            funlist.append(fun[0])
            return funlist
        else:
            outcome('red',f"{file_path}  is not exist !" )

    def write_data(self,data,module='',pyfile=''):

        '''
        获取封装文件内容
        :param data: 数据
        :param module: 模块
        :param pyfile: 文件名
        :return:
        '''
        strfun = ''
        strclass = ''
        strclass += class_title.format(data["className"], data['modular'])
        self.pyfun = self.search_pyfun(module, pyfile)
        self.yafun = [list(i.keys()) for i in data['funName']][0]
        self.surplus = [fun for fun in self.yafun if fun not in self.pyfun]
        if not self.pyfun:
            for fun in data['funName']:
                for funname in self.yafun:
                    strfun += case_body.format(funname, fun[funname]['case_name'], fun[funname]['mode'],
                                                 fun[funname]['re_bar'])
            class_case = strclass + strfun

            return class_case

        if self.surplus and self.pyfun:
            for fun in data['funName']:
                for funname in self.yafun:
                    if funname in self.surplus:
                        strfun += case_body.format(funname, fun[funname]['case_name'], fun[funname]['mode'],
                                                 fun[funname]['re_bar'])

            return strfun


    def create_file(self,module,pyfile):

        '''
        创建文件目录
        :param module: 模块
        :param pyfile: 文件名
        :return:
        '''

        self.module_path = Any_Path(self.projectName,module)
        if not os.path.exists(self.module_path):
            os.makedirs(self.module_path)
        self.file_path = Any_Path(self.projectName,module,pyfile)
        self.init_path = Any_Path(self.projectName,module,self.init)
        self.publicpy_path = Any_Path(self.projectName,module,self.publicpy)
        self.publicyaml_path = Any_Path(self.projectName, module, self.publicyaml)
        if not os.path.exists(self.file_path):
            with open(self.file_path,'w'):pass
        if not os.path.exists(self.init_path):
            with open(self.init_path,'w'):pass
        if not os.path.exists(self.publicpy_path):
            with open(self.publicpy_path,'w',encoding=self.encoding) as f:
                f.write(pypublic)
        if not os.path.exists(self.publicyaml_path):
            with open(self.publicyaml_path,'w',encoding=self.encoding) as f:
                f.write(publicyaml)


    def handle_data(self):
        '''
        处理数据，生成文件数据
        :return:
        '''
        self.check_repeat()
        allvalue = [i for i in self.data]
        for key in allvalue:
            for value in self.data[key]:
                filename = value.get('className').split('_')[0]+self.re.split("*")[1]
                self.create_file(key,filename)
                file_path = Any_Path(self.projectName,key,filename)
                with open(file_path,'a+',encoding=self.encoding) as f:
                    content = self.write_data(data=value,module=key,pyfile=filename)
                    if content:
                        f.write(content)
                        f.close()
        outcome('green','初始化已执行完成....')


    def check_repeat(self):
        '''
        检查用例中是否存在重复类名，方法名
        :return:
        '''
        case_name = []
        class_name = []
        allkey = [i for i in self.data]
        for module in allkey:
            for case in self.data[module]:
                class_name.append(case['className'])
                for fun in case['funName']:
                    for funname in list(fun.keys()):
                        case_name.append(funname)
        if class_name:
            repeat_class = [val for val in set(class_name) if class_name.count(val) > 1]
            if repeat_class:
                warnings.warn(f"用例中存在重复的类名:{repeat_class},请修确认改后，再执行操作....",stacklevel=2)
        if case_name:
            repeat_case = [val for val in set(case_name) if case_name.count(val) > 1]
            if repeat_case:
                warnings.warn(f"用例中存在重复的方法名:{repeat_case},请修确认改后，再执行操作....",stacklevel=2)


if __name__=="__main__":
    Initialization().handle_data()