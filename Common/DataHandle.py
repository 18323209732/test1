# from Common.GetPath import second_path,third_path
import base64

from Common.Route import Any_Path
from Common.ReadYaml import CaseYaml,ConfigYaml
from Common.Abnormal import DataException, SqlException, Assert, KeyException
from functools import wraps
from time import sleep
from Common.MySql import Sql
from Common.Log import MyLog
from Common.FontColor import outcome
import re,os
from Common.MyRedis import ReDis
log = MyLog()


def change_str(value:str):
    '''
    将字符解码为json格式
    :param value:
    :return:
    '''
    result = base64.b64decode(value.encode())
    return str(result, "utf-8")


def DataHandle(obj, data):

    '''
    数据类型处理
    :param obj:
    :param data:
    :return:
    '''
    try:
        if obj:
            if isinstance(obj,list):
                for index,value in enumerate(obj):
                    if data==value:
                        return obj.pop(index)
            elif isinstance(obj,tuple):
                for index,value in enumerate(list(obj)):
                    if str(data)==str(value):
                        return list(obj).pop(index)
            elif isinstance(obj,str):
                if str(data) == obj:
                    return obj
            elif isinstance(obj,dict):
                for key,value in obj.items():
                    if str(data) == str(value):
                        return obj.get(key)
            else:
                raise DataException(obj)
        else:
            outcome('red',f"{obj} is not None")
    except Exception as info:
        return info


def Matching(style,string):
    '''
    正则获取数据值
    :param style:
    :param string:
    :return:
    '''
    global result
    if isinstance(string, dict):
        result = string.get(style)
    elif isinstance(string, str):
        data = string.replace("'", '"').replace(' ', '')
        value = re.findall(f'\"{style}\":(.*?),', data)
        if value:
            result = value[0].replace("'", ' ').replace('"', ' ')
    else:
        data = str(string).replace("'", '"').replace(' ', '')
        value = re.findall(f'\"{style}\":(.*?),', data)
        if value:
            result = value[0].replace("'", ' ').replace('"', ' ')
    return result





def CaseHandle(clsname,funname,data):

    '''
    用例数据处理
    :param clsname:
    :param funname:
    :return:
    '''
    allkeys = list(data.keys())
    key = clsname.split('_')[1]
    if key in allkeys:
        for value in data.get(key):
            if value.get("className") == clsname:
                for fun in value['funName']:
                    return value,fun.get(funname)
    else:
        log.info(f'未找到{key}相关目录')
        raise KeyException(key)




class ReRun:
    def __init__(self, setUp):
        '''
        运行失败重跑
        :param setUp:
        '''
        self.setUp = setUp                 #重跑之前，再次重跑setup初始方法获取初始数据
        self.frequency = ConfigYaml(key='frequency').base_config              #重跑次数
        self.intervaltime = ConfigYaml(key='intervaltime').base_config       #重跑间隔时间

    def __call__(self,method):
        '''
        类装饰器，定义重跑结构
        :param method:
        :return:
        '''
        @wraps(method)
        def execute(*args, **kwargs):
            case_method = method(*args, **kwargs)
            if case_method:
                for frequency in range(self.frequency):
                    self.setUp(*args, **kwargs)
                    case_method = method(*args, **kwargs)
                    sleep(self.intervaltime)                #间隔运行时间
                    return case_method
        return execute


class SqlHandle:
    def __init__(self,funname,describe,priority,address,abnormal,
                 writer,usetime,summary,modular):
        '''
        定义参数
        :param funname: 函数名
        :param describe: 描述
        :param priority:优先级
        :param address: 接口地址
        :param abnormal:返回结果
        :param writer:编写者
        :param usetime:用时
        :param summary:总的信息
        '''
        self.funname = funname
        self.modular = modular
        self.insert_response = ConfigYaml(key='insert_response').sql
        self.insert_result = ConfigYaml(key='insert_result').sql%(self.funname,self.modular)
        self.update_result = ConfigYaml(key='update_result').sql
        self.update_ratecl = ConfigYaml(key='update_ratecl').sql
        self.search_result = ConfigYaml(key='search_result').sql%self.funname
        self.describe = describe
        self.priority = priority
        self.address = address
        self.abnormal= abnormal
        self.writer = writer
        self.usetime = usetime
        self.summary =summary
        if self.abnormal:
            if "AssertionError" in self.abnormal:
                self.status = "失败"

            elif 'skip' in self.abnormal:
                self.status = "跳过"

            else:
                self.status = "错误"
        else:
            self.status = "成功"

    def data_handle(self):
        '''
        定义数据写入格式
        :return:
        '''

        self.abnormal_data = {"funname": self.funname, "describe": self.describe,
                              "priority": self.priority, "address": self.address,
                              "status": self.status, "writer": self.writer,
                              "usetime": self.usetime, "summary": self.summary}

        return self.abnormal_data



    def implement(self):
        '''
        将数据插入数据库，在插入异常时，通过列表添加数据
        :return:
        '''

        try:
            sqldata = self.insert_response%(
                self.funname,self.describe,self.priority,self.address,
                self.status,self.writer,self.usetime,self.summary
                )
            Sql(sql=sqldata).execute_sql()
        except:
            Case_data().write_data(self.data_handle())

    def handle_sql(self,statuscl):
        '''
        sql数据处理
        :param totalnumber:
        :param statusnumber:
        :return:
        '''
        return self.update_result%(statuscl,statuscl,self.funname)

    def update_rate(self,clmname,rate):
        '''
        sql语句拼接
        :param clmname:
        :return:
        '''
        return self.update_ratecl % (clmname,rate,self.funname)

    def insert_result_table(self):
        '''
        result表数据插入
        :return:
        '''
        data = Sql(sql=self.search_result).execute_sql()

        if not data:
            Sql(sql=self.insert_result).execute_sql()

        if self.status == '失败':
            Sql(sql=self.handle_sql(statuscl="failnumber")).execute_sql()
            if not data:
                Sql(sql=self.update_rate(clmname="failrate",rate=1)).execute_sql()

            Sql(sql=self.update_rate(clmname="failrate",
            rate=round((data[0][5]+1)/(data[0][2]+1),2))).execute_sql()

        elif self.status == '错误':
            Sql(sql=self.handle_sql(statuscl="errornumber")).execute_sql()
            if not data:
                Sql(sql=self.update_rate(clmname="errorrate", rate=1)).execute_sql()

            Sql(sql=self.update_rate(clmname="errorrate",
            rate=round((data[0][4]+1)/(data[0][2]+1), 2))).execute_sql()

        else:
            Sql(sql=self.handle_sql(statuscl="passnumber")).execute_sql()
            if not data:
                Sql(sql=self.update_rate(clmname="passrate", rate=1)).execute_sql()

            Sql(sql=self.update_rate(clmname="passrate",
            rate=round((data[0][3]+1)/(data[0][2]+1), 2))).execute_sql()


class  Case_data:

    def __init__(self,filename='Data.yaml',encoding='utf-8'):
        '''
        :param filename: 文件名
        :param encoding:
        '''
        self.filename = filename
        self.encoding = encoding
        self.projectName = ConfigYaml("projectName").base_config
        self.path = Any_Path(self.projectName, self.filename)

    def get_data(self):
        '''
        获取未成功插入数据库数据
        :return:
        '''
        if os.path.exists(self.path):
            with open(self.path, "r", encoding=self.encoding) as f:
                content = f.readlines()
                f.close()
        return content

    def handle_data(self,data):
        '''
        数据处理
        :return:
        '''
        value = (data.get('funname'),data.get('describe'),data.get('priority'),
                 data.get('address'),data.get('status'),data.get('writer'),
                 data.get('usetime'),data.get('summary')
                 )
        return value

    def conversion_data(self):
        '''
        数据处理打包
        :return:
        '''
        caselist = []
        data = self.get_data()
        if data:
            for case in data:
                caselist.append(self.handle_data(eval(case)))
            return caselist

    def clear_content(self):
        '''
        清空文件内容
        :return:
        '''
        log.info("开始清空文件.....")
        if os.path.exists(self.path):
            with open(self.path, 'r+', encoding=self.encoding) as f:
                f.readlines()
                f.seek(0)
                f.truncate()
                f.close()
        log.info("清空文件结束.....")

    def write_data(self,content):
        '''
        当写入数据库发生异常时，将其数据写入文件中
        :return:
        '''
        if not os.path.exists(self.path):
            with open(self.path, "w"): pass
        with open(self.path, "a+", encoding=self.encoding) as f:
            f.writelines(str(content) + '\n')
            f.close()


class GetRedis(object):

    def __init__(self,data):
        '''
        :param data:
        '''
        self.data = data
        self.caselist = []

    def get_redis(self):
        if self.data:
            for i in self.data:
                self.caselist.append(Case_data().handle_data(eval(i)))
        return self.caselist


class Assertion:

    def __init__(self,response,assertEqual,actualone='',
                 actualtwo='',expectone='',expecttwo='',
                 msgone='',msgtwo=''):

        '''

        :param response:  接口返回值
        :param assertEqual: 断言方法
        :param actualone: 第一个实际值
        :param actualtwo: 第二个实际值
        :param expectone: 第一个预期值
        :param expecttwo:  第二个预期值
        :param msgone:     第一个接口返回信息
        :param msgtwo:      第二个接口返回信息
        '''
        self.response = response
        self.actualone = actualone
        self.actualtwo = actualtwo
        self.expectone = expectone
        self.expecttwo =  expecttwo
        self.msgone = msgone
        self.msgtwo = msgtwo
        self.assertEqual = assertEqual

    def datahandle(self):

        '''

        :return:
        '''
        actualone = Matching(self.actualone,self.response)
        actualtwo = Matching(self.actualtwo,self.response)
        msgone = Matching(self.msgone,self.response)
        msgtwo = Matching(self.msgtwo, self.response)

        if self.expectone and self.actualone:
            self.assertEqual(actualone,self.expectone,msg=msgone)

        elif self.expectone and not self.actualone:
            raise Assert(self.expectone,self.actualone)

        elif self.actualone and not self.expectone:
            raise Assert(self.expectone, self.actualone)

        if self.expecttwo and self.actualtwo:
            self.assertEqual(actualtwo, self.expecttwo, msg=msgtwo)

        elif self.expecttwo and not self.actualtwo:
            raise Assert(self.expecttwo, self.actualtwo)

        elif self.actualtwo and not self.expecttwo:
            raise Assert(self.expecttwo, self.actualtwo)


class Package_Data:

    def __init__(self,data,sumtime,starttime,endtime,maxtime,mintime,avgtime):
        '''
        :param data: 接受数据
        :param sumtime:  总共用时
        :param startdata: 开始时间
        :param enddata: 结束时间
        :param maxtime: 最大时间
        :param mintime: 最小用时
        :param avgtime: 平均时间
        '''
        self.data = data                                             #传入数据
        self.sql = ConfigYaml('search_response').sql                 #查询语句
        self.searchsql = ConfigYaml("search_desc").sql                #降序查询时间列数据
        self.time = ConfigYaml('timeout').base_config                 #获取超时时间定义
        self.projectName = ConfigYaml("projectName").base_config      #获取工程名
        self.title = self.projectName + ConfigYaml("title").report     # 报告标题
        self.edition = ConfigYaml("edition").report                     # 测试版本
        self.science = ConfigYaml("science").report                     # 测试环境
        self.sumtime = sumtime
        self.starttime = starttime
        self.endtime = endtime
        self.maxtime = maxtime
        self.mintime = mintime
        self.avgtime = avgtime
        self.allcase = []             #所有用例集
        self.success = []            #成功用例集
        self.fail = []                #失败用例集
        self.error = []                 #错误用例集
        self.skip = []                  #跳过用例集
        self.timeout = []               #超时用例集

    def all_data(self,case:list):
        '''
        用例打包公共方法
        :param case:  用例数据
        :return:
        '''
        return {"funname": case[0], "describe": case[1], "priority": case[2],
                 "address": case[3], "status": case[4], "writer": case[5],
                 "usetime": case[6], "summary": case[7]}

    def Summary(self):
        '''
        用例总体信息定义
        :param sumtime:  总共用时
        :param startdata:  开始时间
        :param enddata:   结束时间
        :param totalex:
        :param maxtime: 最大用时
        :param mintime: 最小用时
        :param avgtime: 平均用时
        :param successrate: 成功率
        :return:
        '''
        return {"title": self.title, "edition": self.edition, "science": self.science,
                 "sumtime": self.sumtime, "startdata": self.starttime,
                 "enddata": self.endtime, "maxtime": self.maxtime,
                 "mintime":self.mintime,"avgtime":self.avgtime
                 }

    def package_pata(self):
        '''
        数据分类打包
        :return:
        '''

        alldict = {}
        for rows in self.data:
            if rows[4] == '成功':
                if rows[6] > self.time:
                    self.timeout.append(self.all_data(rows))
                else:
                    self.success.append(self.all_data(rows))

            elif rows[4] == '错误':
                self.error.append(self.all_data(rows))

            elif rows[4] == '失败':
                self.fail.append(self.all_data(rows))

            elif rows[4] == '跳过':
                self.skip.append(self.all_data(rows))

        alldict['success'] = self.success
        alldict['error'] = self.error
        alldict['fail'] = self.fail
        alldict['timeout'] = self.timeout
        alldict['skip'] = self.skip

        info = self.Summary()
        alldict['info'] = info

        return alldict


class Get_Skip:
    def __init__(self,skipped,data):
        '''

        :param skipped:
        '''
        self.skipped = skipped
        self.data = data

    def get_skip(self):
        '''
        获取跳过的用例
        :return:
        '''
        if self.skipped:
            for skip in self.skipped:
                fun_class = str(skip[0]).split(' ')
                funname = fun_class[0]
                key = fun_class[1].split('.')[1]
                classname = fun_class[1].split('.')[-1].split(")")[0]
                for case in self.data.get(key):
                    if classname==case.get('className'):
                        for funs in case.get('funName'):
                            data = funs.get(funname)
                            SqlHandle(funname,data.get('case_name'),data.get('level'),
                            data.get('url'),'skip',data.get('author'),
                            0,skip[1],classname).implement()



