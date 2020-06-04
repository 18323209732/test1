# coding=utf-8
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Common.Driver import browser
from Common.ReadYaml import ConfigYaml
from time import sleep
from Common.FontColor import outcome

class Login:
    def __init__(self):
        self.base_url = ConfigYaml('Design').base_url
        self.user_pwd = ConfigYaml('user_pwd').base_config
        self.website = ConfigYaml('Door').base_url
        self.username = ConfigYaml('user_name').base_config
        self.cookie_url = ConfigYaml('cookie_url').base_config
        self.driver = browser()
        self.support = WebDriverWait(driver=self.driver, timeout=30)
        self.element = (By.XPATH, "(//{}[@{}='{}'])[{}]")

    def operation_element(self, element):
        return self.support.until(EC.presence_of_element_located(element), message=f'元素:【{element}】超时...')

    def xpath(self, element, *args):
        if "$" in element[1]:
            now_value = element[1].replace("$", "{}")
        elif "{}" in element[1]:
            now_value = element[1].format(*args)
        elif "%s" in element[1]:
            now_value = element[1]%(args)
        else:
            now_value = element[1]

        return self.operation_element((element[0], now_value))

    def clear(self, element, *args):
        self.xpath(element, *args).clear()

    def click(self, element, *args):
        self.xpath(element, *args).click()

    def double_click(self, element, *args):
        self.xpath(element, *args).double_click()

    def send_keys(self, element, *args, value):
        self.clear(element, *args)
        self.xpath(element, *args).send_keys(value)

    def _send_keys(self, *args, data):
        return self.send_keys(self.element, *args, value=data)

    def _click(self, *args):
        return self.click(self.element, *args)


    def more_windows(self):
        return self.driver.window_handles

    def switch_windows(self, name):

        windows = self.more_windows()
        return self.driver.switch_to.window(windows[name])

    def login(self):
        '''
        :return:
        '''
        try:
            outcome('green', "请稍等,正在登陆中....")
            self.driver.get(self.base_url)
            self._send_keys("*", "class", "el-input__inner", 2, data=self.username)
            self._send_keys("*", "class", "el-input__inner", 3, data=self.user_pwd)
            self._send_keys("*", "class", "el-input__inner", 4, data=self.website)
            self._click("*", "class", "el-button el-button--primary", 1)
            sleep(15)
            self._click("*", "class", "pos-icon", 7)
            self.switch_windows(2)
            sleep(3)
            self.driver.get(self.cookie_url)
            cookies = self.driver.get_cookies()[1]['value']
            sleep(2)
            outcome('green', "登陆完成,获取【Cookie】成功....")
            return cookies
        except Exception:
            outcome('red', '登录异常....')

