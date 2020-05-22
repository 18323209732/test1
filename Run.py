import time
import unittest
from threading import Thread,Lock
from Common.MyUnit import MyTest
from Common.Route import Any_Path
from Common.DataHandle import Package_Data, Get_Skip, SqlHandle, Case_data, GetRedis
from Common.ImportClass import ImportClass
from Common.MySql import Sql
import os
from Common.Report import GetReport
from Common.FontColor import outcome
from Common.MyRedis import ReDis
import requests
from Common.Results import Delete_file
from Common.Log import MyLog
from  queue import Queue
from Common.MyProcess import MyProcess
from Common.ReadYaml import ConfigYaml, CaseYaml
from Common.SendMail import  MyMail
from Common.MyProcess import RunFailError
from Common.QqWatch import Send_Wechat
log= MyLog()

class MyThread(Thread):
    '''
    重写多线程方法
    '''
    def __init__(self,moudle,data=None):
        Thread.__init__(self)
        self.moudle = moudle    #目录名称,所要运行的那个目录
        self.data = data
        self.lock = Lock()     #示例锁对象，获取对象id

    def run(self):
        '''
        重写run方法
        :return:
        '''
        log.info("开启多线程并进行加锁....")
        self.lock.acquire()
        RunClass(self.moudle, self.data).run_moudle()
        self.lock.release()
        log.info("多线程结束释放锁....")

class RunClass(object):

    def __init__(self, moudle, data=None):
        '''
        运行单个类
        :param moudle:
        '''
        self.moudle = moudle
        self.data = data

    def run_moudle(self):
        '''
        :return:
        '''
        log.info('开始运行单个模块用例...')
        runner = unittest.TextTestRunner(verbosity=1)
        result = runner.run(MyTest.parametrize(self.moudle))
        Get_Skip(result.skipped, self.data).get_skip()
        log.info('运行单个模块用例结束...')

class RunAll:

    def __init__(self, report='report.html',encoding='utf-8'):
        '''
        运行所有用例
        :param report:    报告名称 ，存放地址template目录下
        :param encoding:   编码格式
        '''
        self.report = report
        self.encoding = encoding
        self.domain = ConfigYaml('domain').base_config                  #域名
        self.title = ConfigYaml('title').base_config                    # 标题
        self.EnvName = ConfigYaml('title').base_config                  #环境
        self.projectName = ConfigYaml("projectName").base_config        #工程名称
        self.moudleName = ConfigYaml('moudleName').base_config          #运行的模块名称
        self.matching = ConfigYaml('matching').base_config              #文件后缀样式
        self.thread_count = ConfigYaml('thread_count').base_config      #开启线程
        self.serverip = ConfigYaml('serverip').base_config              #接口服务器ip，及测试报告的服务器ip
        self.serverport = ConfigYaml('serverport').base_config          #服务端口
        self.delsql = ConfigYaml('del_response').sql                    #清空数据
        self.search_sql = ConfigYaml('search_response').sql             #查询数据
        self.search_desc = ConfigYaml('search_desc').sql                #按降序查询数据（time）
        self.thread = ConfigYaml('threadrun').base_config               #是否开启多线程运行
        self.process = ConfigYaml('process').base_config                #是否开启多进程运行
        self.data = CaseYaml().all_case                                 # 获取用例所有数据
        self.sql = ConfigYaml('sql').base_config                        # 是否开启mysql存储数据
        self.redis = ConfigYaml('redis').base_config                    #是否开始redis存储数据
        self.eachtimes = ConfigYaml('eachtimes').base_config            #运行次数
        self.search_max_result = ConfigYaml('search_max_result').sql    #查询最大数字
        self.operatmode = ConfigYaml('operatmode').base_config          #选择执行方式，
        self.basenumber = ConfigYaml('basenumber').base_config          #执行次数，基数
        self.runfrequency = ConfigYaml('runfrequency').base_config      #只运行失败和错误的用例次数
        self.againrunall = ConfigYaml('againrun').base_config           #运行失败和错误的用例多少次数之后再整体运行多少次
        self.create_table = ConfigYaml('create_table').sql              #创建response表
        self.create_result = ConfigYaml('create_result').sql            #创建result表
        self.report_path = Any_Path("template", 'report.html')       #测试报告存放路径
        self.oldstrcs = '../../static/mycss.css'                       #静态文件地址css
        self.oldstrjs = '../../static/alljs.js'                         #静态js文件地址
        self.newstrcs = '../static/mycss.css'
        self.newstrjs = '../static/alljs.js'
        if self.domain:
            self.url = 'http://{}/get_report/'.format(self.domain)
        else:
            self.url = 'http://{}:{}/get_report/'.format(self.serverip, self.serverport)

        ImportClass().moudle_write()


    def runallmodul(self):
        '''
        非多线程运行
        :return:
        '''
        log.info("单线程用例执行开始....")
        if self.moudleName:
            self.current_path = Any_Path(self.projectName, self.moudleName)
        else:
            self.current_path = Any_Path(self.projectName)
        discover = unittest.defaultTestLoader.discover(
            self.current_path,pattern=self.matching,top_level_dir=None
            )
        runner = unittest.TextTestRunner(verbosity=1)
        result = runner.run(discover)
        log.info("单线程用例执行完成....")
        Get_Skip(result.skipped,self.data).get_skip()

    def runthread(self):
        '''
        多线程运行
        :return:
        '''
        from Scrm import all_class
        mythreads = []
        for mythread in all_class:
            mythreads.append(MyThread(mythread,self.data))

        for start in mythreads:
            start.start()

        for end in mythreads:
            end.join()

    def run_fail_error(self,allclass,classcase):
        '''
        运行失败或者错误率达到多少的
        :return:
        '''
        RunFailError(allclass,classcase).run_fail_error()

    def runprocess(self):
        '''
        多进程运行
        :return:
        '''
        from Scrm import all_dirs
        myprocess = []
        for process in all_dirs:
            myprocess.append(MyProcess(process, self.data))

        for start in myprocess:
            start.start()

        for end in myprocess:
            end.join()

    def sql_handle(self, data):
        '''
        获取总共时间，和用时集合
        :return:
        '''
        all_time = []
        sumtime = 0
        if data:
            for times in data:
                if times[0] != 0:
                    all_time.append(times[0])
                    sumtime += float(times[0])
                else:
                    all_time = sumtime = 0

            return all_time,sumtime

    def runmethod(self):
        '''
        运行方法
        :return:
        '''
        log.info('开始运行用例....')
        if self.thread:
            self.runthread()
        elif self.process:
            self.runprocess()
        else:
            self.runallmodul()


    def runcase(self):
        '''
        运行用例
        :return:
        '''
        from Scrm import class_case
        from Scrm import all_class
        from Scrm import fail_error
        self.clean_data()
        self.startdata = time.strftime("%Y-%m-%d:%H:%M:%S")
        self.startime = time.time()
        max_number = Sql(self.search_max_result).execute_sql()
        if max_number[0][0]:
            operatimes = max_number[0][0]
        else:
            operatimes = 0
        if self.operatmode == 0:                            #执行方式
            if operatimes % self.eachtimes == 0:
                self.runmethod()
            else:
                self.run_fail_error(all_class,class_case)

        elif self.operatmode == 1:
            deviation = operatimes - self.basenumber
            valuesum = self.runfrequency + self.againrunall
            if operatimes < self.basenumber:
                self.runmethod()

            elif (deviation - (deviation//valuesum)*valuesum) % valuesum <= self.runfrequency:
                self.run_fail_error(all_class, fail_error)

            else:
                self.runmethod()

        else:
            self.runmethod()
        log.info('用例运行结束....')
        self.enddata = time.strftime("%Y-%m-%d:%H:%M:%S")
        self.endtime = time.time()
        self.sumtime = round((self.endtime - self.startime), 2)

        return self.startdata, self.enddata, self.sumtime

    def collect_data(self):
        '''
        收集数据
        :return:
        '''
        starttime, endtime, sumtime = self.runcase()
        if self.sql:
            data = Sql(self.search_sql).execute_sql()    #数据库数据
        else:
            cases = ReDis().lrange()
            data = GetRedis(cases).get_redis()         #redis库数据
        case_data = Case_data().conversion_data()      #插入异常文件数据
        if case_data:
            all_data = data + case_data               #拼接数据
        else:
            all_data = data
        times = Sql(self.search_desc).execute_sql()
        all_time, run_sumtime = self.sql_handle(times)
        if isinstance(all_time,list):
            max_time = round(all_time[0], 2)
            min_time = round(all_time[-1], 2)
            avg_time = round(run_sumtime/len(all_time), 2)
        else:
            max_time = min_time = avg_time =0

        value = Package_Data(
                all_data, sumtime, starttime, endtime,
                max_time, min_time, avg_time).package_pata()

        log.info('测试结果数据收集成功....')
        return value

    def get_report(self):
        '''
        发送数据到服务器
        :return:
        '''
        value = self.collect_data()

        r = requests.post(url=self.url, json=value, stream=True, timeout=60)
        if r.json().get('code') == 0:
            url = r.json().get('data').get('report_url')
            file = r.json().get('data').get('report_dir')

            log.info('获取测试报告数据相关内容成功...')

            return url, file, len(value['success']), len(value['error']), len(value['fail']), \
                   len(value['timeout']), len(value['skip'])

    def download_report(self):
        '''
        将服务器的测试报告下载到本地接口
        :return:
        '''
        url, file_path, success, error, fail, timeout, skip = self.get_report()
        data = {'report_dir': file_path}
        re_url = self.url.replace("get_report", "download_report")
        r = requests.post(url=re_url, data=data, stream=True, timeout=60)

        if r.content:
            with open(self.report_path, 'w', encoding=self.encoding) as f:
                content = str(r.content, encoding=self.encoding).\
                replace(self.oldstrcs, self.newstrcs).replace(self.oldstrjs, self.newstrjs)
                f.write(content)
                f.close()
        log.info('下载测试报告至本地成功....')

        return url, file_path, success, error, fail, timeout, skip


    def send_mail(self):
        '''
        发送邮件
        :return:
        '''
        url, file_path, success, error, fail, timeout, skip = self.download_report()
        sum_case = success + error + fail + timeout + skip
        title = '{}({})'.format(self.title,self.EnvName)
        description = '''本次接口运行总数: {}, 成功: {}, 错误: {}, 失败: {}, 超时: {}, 跳过: {}'''\
            .format(sum_case, success, error, fail, timeout, skip)
        img_url = self.url.replace('get_report', 'image')
        Send_Wechat().send_picture(title, description, url, img_url)
        outcome("green", "请稍后!正在发送邮件....")
        MyMail(url, self.report_path).send_info()


    def clean_data(self):
        '''
        运行前数据清理
        :return:
        '''

        Sql(self.create_table).execute_sql()            #创建表response
        Sql(self.create_result).execute_sql()           #创建表result
        if self.sql:
            Sql(self.delsql).execute_sql()              #清空response表
        if self.redis:
            ReDis().delete()                            #清空redis表
        Case_data().clear_content()                     #清空文件存储
        Delete_file().beforedata()                      #删除7天前的日志

        log.info("表创建及清空前置相关工作运行成功....")

if __name__=='__main__':

    RunAll().send_mail()
1111