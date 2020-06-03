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

    def send_keys(self, element, *args, value):
        self.clear(element, *args)
        self.xpath(element, *args).send_keys(value)

    def _send_keys(self, *args, data):
        return self.send_keys(self.element, *args, value=data)

    def _click(self, *args):
        return self.click(self.element, *args)

    def login(self):
        '''
        :return:
        '''
        try:
            self.driver.get(self.base_url)
            self._send_keys("*", "class", "el-input__inner", 2, data=self.username)
            self._send_keys("*", "class", "el-input__inner", 3, data=self.user_pwd)
            self._send_keys("*", "class", "el-input__inner", 4, data=self.website)
            self._click("*", "class", "el-button el-button--primary", 1)
            sleep(17)
            self._click("*", "class", "pos-icon", 7)
            sleep(3)
            self._click("*", "class", "rel active", 1)
            sleep(2)
        except Exception:
            outcome('red', '登录异常....')


    def get_token(self):
        """
        通过driver获取到driver中的token
        """
        js = "sessionStorage.getItem('token');"
        token = self.driver.execute_script(js)
        print(token)


Login().get_token()

