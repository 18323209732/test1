from selenium import webdriver
from Common.Route import Any_Path


def browser(switch=False):
    """Ｆａｌｓｅ
    浏览器驱动程序
    :param switch: 是否开启显示还是隐试浏览器
    :return:
    """
    driver_path = Any_Path('Packages', 'chromedriver.exe')
    if switch:
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('headless')
        driver = webdriver.Chrome(executable_path=driver_path, options=options)
        driver.maximize_window()
    else:
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.maximize_window()

    return driver
