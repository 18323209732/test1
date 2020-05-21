import logging
import time
# from Common.GetPath import second_path
from Common.Route import Any_Path
from termcolor import cprint,colored
from logging.handlers import TimedRotatingFileHandler
import sys,os
from Common.ReadYaml import ConfigYaml,CaseYaml
now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

class MyLog:
    '''
    1.创建日志记录对象
    2.创建日志文件过滤器
    3.创建日志文件处理器
    '''

    def __init__(self,encoding="utf-8"):
        self.level = ConfigYaml('log_level').base_config  #日志文件级别
        self.file_handler = ConfigYaml('file_handler').base_config  #文件输入
        self.steam_handler = ConfigYaml('steam_handler').base_config #控制台输入
        self.interval = ConfigYaml('interval').base_config   # 日志间隔
        self.backupCount = ConfigYaml('backupCount').base_config  #日志保存天数
        self.Log = ConfigYaml('Log').base_config  # 日志保存天数
        self.logger = logging.getLogger()  # 创建日志记录对象示例
        self.logger.setLevel(self.level)  #日志级别
        formatter = logging.Formatter(  # 指定logger输出格式
                '时间:%(asctime)s '  # 时间，默认精确到毫秒
                ' 方法:%(funcName)s '  # 日志函数名
                ' 级别:%(levelname) s '  # log级别
                ' 消息:%(message) s'   # 打印的消息
                ' 行数:%(lineno) d'   #行号
                ' 文件名:%(filename)s'  #    调用日志输出函数的模块的文件名
                )

        current_data = time.strftime('%Y-%m-%d', time.localtime(time.time())) #日志名称
        log_name = '{}.log'.format(current_data)   #创建日志文件名称
        log_path = Any_Path(self.Log)     #创建日志目录路径
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        log_path = Any_Path(self.Log,log_name)
        file_handler= TimedRotatingFileHandler(filename=log_path, when="D", interval=self.interval, backupCount=self.backupCount, encoding=encoding) #每天创建一份日，最大保存7天
        file_handler.setFormatter(formatter)  #设置日志文件输出格式
        console_handler = logging.StreamHandler(sys.stdout)  # 输出到控制台
        console_handler.setFormatter(formatter)  # 设置控制台输出格式
        if self.file_handler:
            self.logger.addHandler(file_handler)  #添加文件处理器
        if self.steam_handler:
            self.logger.addHandler(console_handler) #添加控制台处理器

    def debug(self, content):
        self.logger.debug(content)

    def info(self, content):
        self.logger.info(content)

    def warning(self, content):
        self.logger.warning(content)

    def error(self, content):
        self.logger.error(content)

    def fatal(self, content):
        self.logger.fatal(content)

    def critical(self, content):
        self.logger.critical(content)



