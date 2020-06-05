# coding=utf-8
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Common.Driver import browser
from Common.ReadYaml import ConfigYaml
from time import sleep
from Common.FontColor import outcome
import requests
class Login:
    def __init__(self):
        self.base_url = ConfigYaml('Design').base_url
        self.user_pwd = ConfigYaml('user_pwd').base_config
        self.username = ConfigYaml('user_name').base_config
        self.key = ConfigYaml('key').base_config
        self.project_url = ConfigYaml('project_url').base_config
        self.cookies = ConfigYaml('cookies').base_config
        self.website = ConfigYaml('website').base_config
        self.new_website = ConfigYaml('new_website').base_config
        self.session = ConfigYaml('session').base_config
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

    def get_cookie(self):
        '''
        :return:
        '''
        try:
            outcome('green', "请稍等,正在登陆中....")
            self.driver.get(self.base_url)
            self._send_keys("*", "id", "username", 1, data=self.username)
            self._send_keys("*", "id", "password", 1, data=self.user_pwd)
            self._click("*", "class", "input-box-button m20", 1)
            sleep(10)
            self._click("*", "class", "closeCode abs", 1)
            cookies = self.driver.get_cookies()[1].get('value')
            _cookies = f"{self.key}={cookies}"
            count, index = self.get_index(_cookies)
            for pages in range(count):
                if pages == 0:
                    self._click("*", "class", "arrow-border active", 1)
                    sleep(1)
                else:
                    self._click("*", "class", "arrow-border active", 2)
                    sleep(1)
            self._click("*", "class", "el-button el-button--primary el-button--small", index)
            sleep(7)
            self.driver.get(self.new_website)
            Cookis = self.driver.get_cookies()[1].get("value")
            outcome('green', "登陆完成,获取【Cookie】成功....")
            return f"{self.session}={Cookis}"

        except Exception:
            outcome('red', '登录异常....')

    def get_index(self, cookies):
        '''
        :return:
        '''
        global all_count, result_count
        headers = {self.cookies: cookies}
        response = requests.get(url=self.project_url, headers=headers)
        result = response.json()
        if result.get('status') == 101:
            for index, value in enumerate(result.get('data').get('jsonVoList')):
                if self.website == value.get('domain'):
                    all_count = index + 1
            count, remainder = divmod(all_count, 3)
            if remainder:
                result_count = count
            else:
                result_count = count - 1

            return result_count, remainder

        else:
            outcome('red', "获取网站【index】失败....")


