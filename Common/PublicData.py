from Common.DataHandle import CaseHandle
from Common.ReadYaml import CaseYaml


class Get_Public:
    def __init__(self, class_name, case_name):
        '''
        :param class_name:
        :param case_name:
        '''
        self.data = CaseYaml().all_case
        self.class_name = class_name
        self.case_name = case_name

    def get_data(self):
        '''
        :return:
        '''
        if self.data:
            self.clsdata, self.fundata = CaseHandle(self.class_name, self.case_name, self.data)