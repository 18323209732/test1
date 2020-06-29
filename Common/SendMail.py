# coding=utf-8
import platform
import smtplib
import time
import os
import warnings
from email.mime.multipart import MIMEMultipart
from Common.FontColor import outcome
# from Common.GetPath import second_path
from Common.Route import Any_Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from Common.ReadYaml import ConfigYaml


class MyMail(object):

    def __init__(self,url,filedir, filename='report.png'):
        '''
        初始化数据
        :param url: 图片地址
        :param filename:  保存图片名
        '''
        self.url = url
        self.filedir = filedir
        self.title = ConfigYaml('title').email
        self.send_person = ConfigYaml('send_person').email
        self.receive_person = ConfigYaml('receive_person').email
        self.smtp_sever = ConfigYaml('smtp_sever').email
        self.send_pwd = ConfigYaml('send_pwd').email
        self.image = ConfigYaml('image').base_config
        self.filename = filename
        self.msg_info = MIMEMultipart("mixed")
        self.dir_path = Any_Path("Packages","chromedriver.exe")
        self.options = Options()
        self.image_path = Any_Path(self.image)
        self.mail_file = ConfigYaml('mail_file').base_config
        self.mail_picture = ConfigYaml('mail_picture').base_config


    def screen_shot(self):
        '''
        截图方法
        :return:
        '''
        self.options.add_argument('--headless')
        warnings.simplefilter("ignore")
        driver = webdriver.Chrome(self.dir_path, chrome_options=self.options)
        driver.get(self.filedir)
        driver.implicitly_wait(10)
        driver.set_window_size(1800,900)
        sleep(3)
        if not os.path.exists(self.image_path):
            os.makedirs(self.image_path)
        driver.get_screenshot_as_file(Any_Path(self.image, self.filename))
        driver.quit()

    def text_header(self):
        '''
        邮件正文
        :return:
        '''
        self.msg_info['From'] = self.send_person
        self.msg_info['To'] = ','.join(self.receive_person)
        self.msg_info['Subject'] = Header(self.title, 'utf-8').encode()
        msg_text = MIMEText(
            '''
            <p><font size="3" color="red">Hi ALL!</font></p>
            <p><font size="3" color="red">      邮件已发送至各位人员邮箱,请注意查收! 谢谢！</font></p>
            <p><i><font size="3" color="blue"><a href="http://{}" target="_blank" class="mnav">
            点击此处在线查看测试报告</a></font></i></p><img alt="" src="cid:image1"/><br/><br/>'''.format(self.url), 'html',
            'utf-8')
        self.msg_info.attach(msg_text)
        return self.msg_info

    def send_picture(self):
        '''
        放置图片于邮件正文中
        :param dress:
        :param filename:
        :return:
        '''
        self.text_header()
        f = open(Any_Path(self.image,self.filename), 'rb')
        mail_body = MIMEImage(f.read())
        f.close()
        mail_body.add_header('Content-ID', '<image1>')
        self.msg_info.attach(mail_body)
        return self.msg_info

    def send_file(self):
        '''
        发送邮件附件
        :return:
        '''
        self.text_header()
        text = MIMEText(open(self.filedir, 'rb').read(), 'base64', 'utf-8')
        text['Content-Type'] = 'application/octet-stream'
        text["Content-Disposition"] = 'attachment; filename="report.html"'
        self.msg_info.attach(text)
        return self.msg_info

    def send_msg(self):
        '''
        发送邮件信息
        :return:
        '''
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtp_sever)  # 连接至邮件服务器
            smtp.login(self.send_person, self.send_pwd)  # 登录邮件服务器
            smtp.sendmail(self.send_person, self.receive_person, self.msg_info.as_string())  # 发送邮件
            smtp.quit()
            outcome('green',"给【%s】发送邮件成功" % ','.join(self.receive_person))
        except Exception as f:
            outcome("red","给%s发送邮件失败,失败原因：%s" % (','.join(self.receive_person),f))

    def send_info(self):
        '''
        邮件发送封装
        :return:
        '''
        if self.mail_file:
            self.send_file()
        if self.mail_picture:
            self.screen_shot()
            self.send_picture()
        self.send_msg()



