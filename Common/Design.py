
# coding=utf-8
import requests,re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Common.Driver import browser
from Common.FontColor import outcome
from time import sleep
from Common.ReadYaml import ConfigYaml
from selenium.webdriver import ActionChains
import json
import base64
import tesserocr   # 用于图片转文字
from PIL import Image
from Common import Route
projectName = ConfigYaml("projectName").base_config
Url = ConfigYaml(projectName).base_url


def imgdata(src):
    image = src.replace('data:image/JPEG;base64,', '')
    imgdata = base64.b64decode(image)
    path = Route.Any_Path("Img", "imagedata.jpg")
    # print(path)
    fp = open(path, 'wb')  # 'wb'表示写二进制文件
    fp.write(imgdata)
    fp.close()

    image = Image.open(path)  # 传入你所保存的图片路径
    result = tesserocr.image_to_text(image)[0:5]
    
    return result


class Design:
    def __init__(self):
        self.Des_url = ConfigYaml('website').base_config
        self.url = ConfigYaml('Door').base_url
        self.base_url = ConfigYaml('design_web').base_config  # 设计器地址
        self.user_pwd = ConfigYaml('design_pwd').base_config
        self.username = ConfigYaml('design_username').base_config
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

    def drap_drop(self, element, n1, n2):
        return ActionChains(self.driver).drag_and_drop_by_offset(element, n1, n2).perform()

    def more_windows(self):
        return self.driver.window_handles

    def switch_windows(self, name):

        windows = self.more_windows()
        return self.driver.switch_to.window(windows[name])

    def login(self):
        # a = re.findall("(\w+)+", self.url)

        self.driver.get(self.base_url)

        self._send_keys("*", "name", "username", 1, data=self.username)
        self._send_keys("*", "name", "password", 1, data=self.user_pwd)
        self._send_keys("*", "name", "domain", 1, data=self.Des_url)
        self._click("*", "class", "el-button el-button--primary", 1)
        sleep(6)

    def add_page(self, value=None, xpath=None):
        '''
        添加承载组件的首页
        '''
        try:
            Design.login(self)
            # 清空组件
            self._click("*", "class", "icon_pos", 1)  # 点击设置
            sleep(1)
            b = self.driver.find_element_by_xpath("(//*[@class='clearup'])[3]")  # 点击清空所有元素
            ActionChains(self.driver).move_to_element(b).double_click().perform()
            a = self.driver.find_element_by_xpath("(//*[@class='pa icon-closepanle'])[9]")  # 点击关闭浮层
            ActionChains(self.driver).move_to_element(a).double_click().perform()

            self._click("*", "class", "si icon-addpages", 1)  # 获取首页页面
            self._click("*", "class", "displayPageName", 1)  # 点击首页
            self._click("*", "class", "si icon-components", 1)  # 点击添加组件按钮
            self._click("*", "class", "new-search-button", 1)  # 搜索组件
            self.driver.find_element_by_xpath("(//*[@class='new-search'])[1]/*[@type='text']").send_keys(value)   # 输入要搜索的内容
            sleep(0.5)
            self._click("*", "class", "btn normal gray shadow", 1)  # 点击搜索
            sleep(1)
            a = self.driver.find_element_by_xpath(xpath)
            self.drap_drop(a, 756, 66)
            sleep(1)
            if value == "询价":
                self._click("*", "class", "icon_pos", 1)  # 点击设置
                sleep(1)
                b = self.driver.find_element_by_xpath("//*[@class='elements_box']/*/*/span")   # 点击浮窗设置
                ActionChains(self.driver).move_to_element(b).double_click().perform()
                sleep(1.5)
                self.driver.find_element_by_xpath("((//*[@class='form-group  s-15'])[6]/*)[1]").click()
                self.driver.find_element_by_xpath("(//*[@class='right']/*[@class='btn normal shadow blue'])[3]").click()
                # 保存设置
                self.driver.find_element_by_xpath("(//*[div='保存'])/*").click()  # 点击保存
                sleep(2)
                self.driver.find_element_by_xpath("(//*[div='预览'])/*[2]").click()  # 点击预览
                toHandle = self.driver.window_handles
                # print(toHandle)
                self.driver.switch_to.window(toHandle[1])
                sleep(3)
            else:
                # 保存设置
                self.driver.find_element_by_xpath("(//*[div='保存'])/*").click()  # 点击保存
                sleep(2)
                self.driver.find_element_by_xpath("(//*[div='预览'])/*[2]").click()  # 点击预览
                toHandle = self.driver.window_handles
                # print(toHandle)
                self.driver.switch_to.window(toHandle[1])
                sleep(3)
                # print(self.driver.current_window_handle)

        except Exception:

            outcome('red', '设计器页面异常....')

    def add_enquiry(self):
        """
        从设计器添加询价内容
        """
        try:
            Design.add_page(self, value='询价', xpath="(//*[@src='/productimg/thumbnail/c_portalResEnquiry_submitForm-01001.png'])[1]")

            # 选择产品
            self.driver.find_element_by_xpath("(//*[@class='btn btn-primary p_addBtn pcButton'])[1]").click()
            sleep(4)
            # 勾选产品并保存
            self.driver.find_element_by_xpath("((//*[@class='e_box p_sel'])/*)[1]").click()
            self.driver.find_element_by_xpath("((//*[@class='e_box p_submit borderT_default btn-group'])/*)[1]").click()

            # 填写询价说明
            self.driver.find_element_by_xpath("((//*[@class='e_input col-sm-10 formItemInput p_intentionIntro'])/*)[1]").send_keys('AAAAAA')
            # 填写联系人
            self.driver.find_element_by_xpath(
                "((//*[@class='e_input col-sm-10 formItemInput p_contacts'])/*)[1]").send_keys('联系人A')
            # 手机号
            self.driver.find_element_by_xpath(
                "((//*[@class='e_input col-sm-10 formItemInput p_mobile'])/*)[1]").send_keys('1333333333')
            # 填写邮箱
            self.driver.find_element_by_xpath(
                "(//*[@class='form-control InputText js-valid'])[6]").send_keys('jiangna@gouuse.cn')
            # 填写验证码
            src = self.driver.find_element_by_xpath("(//*[@class='e_image col-sm-2 p_imageB p_refreshCode'])[1]/*").get_attribute('src')
            result = imgdata(src)
            self.driver.find_element_by_xpath(
                "((//*[@class='e_input col-sm-10 formItemInput p_captchas'])/*)[1]").send_keys(result)

            # 提交表单

            self.driver.find_element_by_xpath(
                "(//*[@class='btn btn-primary submitPC p_submit submitAll'])[1]").click()

            if self.driver.find_element_by_xpath(
                    "(//*[@class='text-error color_error h6'])"):

                    while 1 < 2:
                        self.driver.find_element_by_xpath(
                            "(//*[@class='e_image col-sm-2 p_imageB p_refreshCode'])[1]/*").click()
                        sleep(1)
                        src = self.driver.find_element_by_xpath(
                            "(//*[@class='e_image col-sm-2 p_imageB p_refreshCode'])[1]/*").get_attribute('src')
                        result = imgdata(src)
                        self.driver.find_element_by_xpath(
                            "//*[@class='form-control InputText']").clear()
                        self.driver.find_element_by_xpath(
                            "//*[@class='form-control InputText']").send_keys(result)
                        sleep(1)
                        self.driver.find_element_by_xpath(
                            "(//*[@class='btn btn-primary submitPC p_submit submitAll'])[1]").click()
                        sleep(0.5)
                        if self.driver.find_element_by_xpath(
                                "(//*[@class='text-error color_error h6'])"):
                            sleep(0.5)
                            continue
                        else:
                            break

            else:
                outcome('green', '询价添加成功....')

        except Exception:
            pass

    def add_intention(self):
        """
        从设计器添加意向单
        """
        try:
            Design.add_page(self, value="意向", xpath="(//*[@src='/productimg/thumbnail/c_portalResIntention_form-01001.png'])[1]")
            # 填写意向说明
            self._send_keys("*", "class", "form-control InputText js-valid", 1, data="AAAAA")
            # 填写联系人
            self._send_keys("*", "class", "form-control InputText js-valid", 2, data="联系人A")
            # 手机号
            self._send_keys("*", "class", "form-control InputText js-valid", 3, data="13333333333")
            src = self.driver.find_element_by_xpath(
                "(//*[@class='e_image col-sm-2 p_imageB'])[1]/*").get_attribute('src')
            result = imgdata(src)
            # print(result)
            self._send_keys("*", "class", "form-control InputText", 1, data=result)
            self._click("*", "class", "btn btn-primary submitPC p_submit", 1)
            if self.driver.find_element_by_xpath(
                    "(//*[@class='text-error color_error h6'])"):
                while 1 < 2:
                    self.driver.find_element_by_xpath(
                        "(//*[@class='e_image col-sm-2 p_imageB'])[1]/*").click()
                    sleep(1)
                    src = self.driver.find_element_by_xpath(
                        "(//*[@class='e_image col-sm-2 p_imageB'])[1]/*").get_attribute('src')
                    result = imgdata(src)
                    self._send_keys("*", "class", "form-control InputText", 1, data=result)
                    sleep(0.5)
                    self._click("*", "class", "btn btn-primary submitPC p_submit", 1)
                    sleep(0.5)
                    if self.driver.find_element_by_xpath(
                            "(//*[@class='text-error color_error h6'])"):
                        sleep(0.5)
                        continue
                    else:
                        break
        except Exception:
            pass


if __name__ == '__main__':
    Design().add_intention()
    # path = Route.Any_Path("Img", "imagedata.jpg")
    # print(path)

