from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# class TestHgws():
#     def setup(self):
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(5)
#
#     def teardown(self):
#         self.driver.quit()
#
#     def test_hgws(self):
#         self.driver.get("http://www.testerhome.com")
#         self.driver.find_element_by_link_text("社团").click()
#
# class TestWait:
#     def setup(self):
#         self.driver = webdriver.Firefox()
#         self.driver.get("https://www.baidu.com/")
#         self.driver.implicitly_wait(3)
#     def teardown(self):
#         # self.driver.quit()
#         pass
#     def test_wait(self):
#         # self.driver.find_element_by_xpath('//*[@id="js-tab"]/li[2]').click()
#         # def wait(x):
#         #     return len(self.driver.find_element_by_class_name('course-total-title')) >= 1
#         # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@class="course-total-title"]')))
#         # self.driver.find_element_by_xpath('/html/body/section[2]/div[2]/div[2]/div[1]/div[3]/ul/li[2]').click()
#         # self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("霍格沃兹测试学院")
#         self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys("霍格沃兹测试学院")
#         self.driver.find_element(By.ID,'su').click()

class TestActionChains():
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()
    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        element_click = self.driver.find_element_by_xpath('//input[@value="click me"]')
        element_doubleclick = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        element_rightclick = self.driver.find_element_by_xpath('//input[@value="right click me"]')
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        sleep(3)
        action.perform()
        sleep(3)
    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get('https://www.baidu.com/')
        ele = self.driver.find_element(By.XPATH,'//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)
    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        drag_element = self.driver.find_element(By.XPATH,'//*[@id="dragger"]')
        drop_element1 = self.driver.find_element(By.XPATH,'//*[@class="item"][1]')
        drop_element2 = self.driver.find_element(By.XPATH,'//*[@class="item"][2]')
        drop_element3 = self.driver.find_element(By.XPATH,'//*[@class="item"][3]')
        drop_element4 = self.driver.find_element(By.XPATH,'//*[@class="item"][4]')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_element,drop_element1)
        sleep(1)
        action.drag_and_drop(drag_element,drop_element2)
        sleep(1)
        action.drag_and_drop(drag_element, drop_element3)
        sleep(1)
        action.drag_and_drop(drag_element, drop_element4)
        action.perform()
        sleep(3)
    def test_keys(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        ele = self.driver.find_element_by_xpath('/html/body/label[1]/input').click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)

class TestTouchAction():
    def setup(self):
        # option = webdriver.FirefoxOptions()
        # option.add_argument('w3c',False)
        self.driver = webdriver.Firefox()#options=option
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    def test_touchaction_scrollbottom(self):
        self.driver.get('https://www.baidu.com/')
        ele = self.driver.find_element(By.XPATH,'//*[@id="kw"]')
        ele_search = self.driver.find_element(By.XPATH,'//*[@id="su"]')
        ele.send_keys("selenium测试")
        ele_search.click()
        #action = TouchActions(self.driver)
        # action.tap(ele_search)
        # action.perform()

        #action.scroll_from_element(ele,0,10000).perform()
        sleep(3)

class TestWindows():
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()

    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text('登录').click()
        print(self.driver.current_window_handle)
        self.driver.find_element(By.XPATH,'//*[@class="pass-reglink pass-link"]').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_4__userName"]').send_keys('username')
        self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_4__phone"]').send_keys('15854215874')
        # self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_4__password"]').send_keys('123456789')
        # self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_4__verifyCodeSend"]').click()
        # self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_4__verifyCode"]').send_keys('efefg')
        # self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_4__isAgree"]').click()
        # self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_4__submit"]').click()
        sleep(2)
        self.driver.switch_to.window(windows[0])
        self.driver.find_element(By.XPATH,'//*[@class="tang-pass-footerBarULogin pass-link"]').click()
        self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__userName"]').send_keys('18323209732')
        self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__password"]').send_keys('lhj15892641840')
        self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__submit"]').click()
        sleep(3)

class TestJs():
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_js_scroll(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('selenium测试')
        ele = self.driver.execute_script('return document.getElementById("su")')
        ele.click()
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        self.driver.find_element_by_partial_link_text('下一页').click()
        sleep(3)
        for code in [
            'return document.title','return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))

    def test_datetime(self):
        self.driver.get('https://www.12306.cn/index/')
        ele_time = self.driver.execute_script('document.getElementById("train_date").removeAttribute("readonly")')
        self.driver.execute_script('document.getElementById("train_date").value="2021-6-30"')
        sleep(5)
        print(self.driver.execute_script('return document.getElementById("train_date").value'))

class TestFile():
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_file_upload(self):
        self.driver.get('https://image.baidu.com/')
        self.driver.find_element(By.XPATH,'//*[@class="st_camera_off"]').click()
        #self.driver.find_element_by_id('uploadImg').send_keys('D:\Download\x1 (1).jpg')
        sleep(3)

class TestAlert():
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_alert(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame("iframeResult")
        ele1 = self.driver.find_element_by_id('draggable')
        ele2 = self.driver.find_element_by_id('droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(ele1,ele2).perform()
        sleep(3)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id('submitBTN').click()
        sleep(3)


class Testcase():
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        #self.driver.quit()
        pass
    def test_case(self):
        self.driver.get('https://www.tapd.cn/53545889/sparrow/tcase/tcase_list?category_id=1153545889001001011&data[Filter][name]=&data[Filter][status]=')
        ele_name = self.driver.find_element(By.XPATH,'//*[@id="username"]')
        ele_name.click()
        sleep(1)
        # 输入用户名
        ele_name.send_keys('liuhongjiang@300.cn')
        ele_pwd = self.driver.find_element(By.XPATH,'//*[@id="password_input"]')
        ele_pwd.click()
        #输入密码
        ele_pwd.send_keys('Lhj15892641840')
        ele_login = self.driver.find_element(By.XPATH,'//*[@id="tcloud_login_button"]')
        #点击登录按钮
        ele_login.click()

        #点击创建用例按钮
        self.driver.find_element(By.XPATH,'//*[@class="bug-list-head-btn-span"]').click()
        sleep(1)
        #获取全部窗口的句柄
        all_handle = self.driver.window_handles
        #获取当前窗口的句柄
        sreach_windows = self.driver.current_window_handle
        for handle in all_handle:
            if handle != sreach_windows:
                self.driver.switch_to.window(handle)
                ele_name = self.driver.find_element_by_xpath('//*[@id="TcaseName"]')
                ele_name.click()
                #输入标题
                ele_name.send_keys("易强傻子")
                sleep(1)

                ele_option = self.driver.find_element_by_xpath('/html/body')
                ele_option.click()
                #输入前置条件
                ele_option.send_keys('易强是傻子吗？')
                sleep(1)

                # self.driver.switch_to.frame('editor-iframe')
                # self.driver.find_element(By.XPATH,'//*[@class="editor-iframe"]').send_keys('易强还是傻呀')

                # ele_step = self.driver.find_element(By.XPATH,'//*[@class="editor-toolbar"]')
                # ele_step.click()
                # ele_step.send_keys('易强就是大傻子！')

                # 获取邮件正文编辑区域的iframe页面元素对象

                # iframe = self.driver.find_element_by_xpath ('//iframe[contains(@class, "editor-toolbar")]')
                #
                # # 通过switch_to.frame()方法切换进入富文本框中
                #
                # self.driver.switch_to.frame(iframe)
                #
                # # 通过JavaScript代码向邮件正文编辑框中输入正文
                #
                # self.driver.execute_script("document.getElementsByTagName('body')\[0].innerHTML = '易强还是个傻子'")
                # js = "document.getElementsByClassName(\"webkit-scrollbar editor-content rich-editor-content\")[0].contentWindow.document.body.innerHTML=\"%s\"" % ("易强还是个傻子")
                # self.driver.execute_script(js)
                self.driver.switch_to.default_content()
                action = ActionChains(self.driver)
                action.move_by_offset(118,622).send_keys('易强还是个傻子').perform()


        # ele_option = self.driver.find_element_by_link_text('请输入前置条件')
        # ele_option.click()
        # ele_option.send_keys('易强真是个傻子')
        # sleep(1)
        # ele_setcase = self.driver.find_element_by_link_text('请输入预期结果')
        # ele_setcase.click()
        # ele_setcase.send_keys('易强还是个傻子')



# if __name__ == '__main__':
#     pytest.main(["-v","-s","test1.py"])

# drive = webdriver.Firefox()
# drive.get("https://www.baidu.com/")
# def provider():
#     for i in range(5):
#         yield i
# #yield 激活teardown的方法
# p = provider()
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
#
# class Person:
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         print(f"{self.name} is eating")
# p = Person('jerry')
#
# print(hasattr(p,"eat"))
# print(getattr(p, "name"))


