# coding=utf-8

import schedule
import os
import sys
import platform
env = os.path.dirname(__file__)
sys.path.append(env)
from Common.Log import MyLog
from Common.ReadYaml import CaseYaml,ConfigYaml
from Common.Results import cmd
from Run import RunAll
from apscheduler.schedulers.blocking import BlockingScheduler


log = MyLog()


class TimingTask:
    def __init__(self):
        self.timing = ConfigYaml('timing').base_config
        self.company = ConfigYaml('company').base_config
        self.task = BlockingScheduler()

    def Perform_Task(self):
        '''
        需要调度的任务
        :return:
        '''
        log.info('开始执行任务')
        RunAll().send_mail()

    def DoJob(self):
        '''
        将执行任务加入定时器
        :return:
        '''
        if self.company=='分':
            self.task.add_job(self.Perform_Task, trigger='interval', seconds=self.timing*60)   # 每隔多少分钟执行一次

        elif self.company=='时':
            self.task.add_job(self.Perform_Task, trigger='interval', seconds=self.timing*60*60)  # 每隔多少小时执行一次任务

        elif self.company == '秒':
            self.task.add_job(self.Perform_Task, trigger='interval', seconds=self.timing)  # 每隔多少小时执行一次任务

        self.task.start()

        log.info('任务执行完成')

if __name__ == '__main__':
    job = TimingTask().DoJob()

