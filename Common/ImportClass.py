from Common.MySql import Sql
from Common.ReadYaml import ConfigYaml
# from Common.GetPath import second_path, third_path
import re
import os
import unittest
from Common.Route import Any_Path


class ImportClass(object):
    def __init__(self, discover='', encoding='utf-8'):
        '''

        :param discover:
        :param encoding:
        '''
        self.discover = discover
        self.encoding = encoding
        self.module = ConfigYaml('moudleName').base_config
        self.project = ConfigYaml('projectName').base_config
        self.matching = ConfigYaml('matching').base_config
        self.errorrate = ConfigYaml('errorrate').base_config
        self.failrate = ConfigYaml('failrate').base_config
        self.search_all_result = ConfigYaml("search_all_result").sql
        self.search_fail_error = ConfigYaml('search_fail_error').sql % (self.errorrate, self.failrate)
        self.init = "__init__.py"

    def moudle_write(self):
        '''
        写入模块数据
        :return:
        '''
        project_path = Any_Path(self.project)
        dir_file_list = os.listdir(project_path)
        moudle_list = []
        all_import_class = []
        class_list = []
        all_dirs = [catalog for catalog in dir_file_list
                   if "." not in catalog and '__' not in catalog]

        if self.module is None:
            for dirs in dir_file_list:
                if '.' not in dirs and '__' not in dirs:
                    if os.path.exists(Any_Path(self.project, dirs, self.init)):
                        moudle_list.append(dirs)

        elif isinstance(self.module, list):
            for dirs in self.module:
                if dirs in dir_file_list:
                    if '.' not in dirs and '__' not in dirs:
                        if os.path.exists(Any_Path(self.project, dirs, self.init)):
                            moudle_list.append(dirs)
        else:
            if os.path.exists(Any_Path(self.project, self.module, self.init)):
                moudle_list.append(self.module)

        for moudle in moudle_list:
            global classname
            dir_path = Any_Path(self.project, moudle)
            dir_list = os.listdir(dir_path)
            for file in dir_list:
                if self.matching.split('*')[1] in file:
                    classname = '{}_{}'.format(file.split('_')[0], moudle)
                    all_import_class.append('from {}.{}.{} import {}\n'.format(self.project,moudle,file.split('.')[0],classname))
                    class_list.append(classname)
        if all_import_class and class_list:
            all_moudle = re.sub("'", '', str(class_list))
            content = '\nall_class = {}\n'.format(all_moudle)
            alldirs = '\nall_dirs = {}\n'.format(all_dirs)
            class_case = '\nclass_case = {}\n'.format(Sql(self.search_all_result).execute_sql())
            fail_error = '\nfail_error = {}'.format(Sql(self.search_fail_error).execute_sql())
            self.write_data(all_import_class, content, alldirs, class_case, fail_error)


    def write_data(self,module,classname,alldir,class_case,fail_error):
        '''

        :param module:
        :param classname:
        :return:
        '''
        init_path = Any_Path(self.project, self.init)
        if not os.path.exists(init_path):
            with open(init_path):pass

        with open(init_path,'w',encoding=self.encoding) as f:
            f.writelines(module)
            f.close()

        with open(init_path, 'a', encoding=self.encoding) as f:
            f.writelines(classname)
            f.close()

        with open(init_path, 'a', encoding=self.encoding) as f:
            f.writelines(alldir)
            f.close()

        with open(init_path, 'a', encoding=self.encoding) as f:
            f.writelines(class_case)
            f.close()

        with open(init_path, 'a', encoding=self.encoding) as f:
            f.writelines(fail_error)
            f.close()

# if __name__=="__main__":
#
#     ImportClass().moudle_write()