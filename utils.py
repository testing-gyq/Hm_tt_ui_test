import json
import logging
import time

import allure
import selenium.webdriver
import appium.webdriver

# 定义浏览器驱动的工具类-自定义
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class DriverUtils:
    # 自媒体驱动对象私有属性
    __mp_driver = None
    # 后台管理系统
    __mis_driver = None
    # APP
    __app_driver = None
    # 浏览器驱动开关
    __mp_key = True
    __mis_key = True

    @classmethod
    def get_mp_driver(cls):
        if cls.__mp_driver is None:
            # 创建浏览器驱动对象 --> 打开浏览器
            cls.__mp_driver = selenium.webdriver.Chrome()
            cls.__mp_driver.maximize_window()  # 窗口最大化
            cls.__mp_driver.implicitly_wait(30)  # 隐式等待
            cls.__mp_driver.get("http://ttmp.research.itcast.cn/")
        return cls.__mp_driver

    # 自媒体-关闭浏览器驱动的方法
    @classmethod
    def quit_mp_driver(cls):
        # 为了保障代码的健壮性,防止异常报错,先判断当前是否有浏览器驱动对象是否存在
        if cls.__mp_driver is not None and cls.__mp_key:
            # 关闭浏览器
            time.sleep(4)
            # quit()只是关闭整个浏览器但是并不会将__driver的值设置为空,而是保留一串缓存字符串
            cls.__mp_driver.quit()
            # 将__driver设置为空
            cls.__mp_driver = None

    # 修改mp关闭浏览器驱动的方法(因为是私有方法，所以需要重新在类内部定义）
    @classmethod
    def chang_mp_key(cls, key):
        cls.__mp_key = key

    # 后台管理系统获取驱动对象得方法
    @classmethod
    def get_mis_driver(cls):
        if cls.__mis_driver is None:
            # 创建浏览器驱动对象 --> 打开浏览器
            cls.__mis_driver = selenium.webdriver.Chrome()
            cls.__mis_driver.maximize_window()  # 窗口最大化
            cls.__mis_driver.implicitly_wait(30)  # 隐式等待
            cls.__mis_driver.get("http://ttmis.research.itcast.cn/")
        return cls.__mis_driver

        # 修改mp关闭浏览器驱动的方法(因为是私有方法，所以需要重新在类内部定义）

    @classmethod
    def chang_mis_key(cls, key):
        cls.__mis_key = key

    # 后台管理系统-关闭浏览器驱动的方法
    @classmethod
    def quit_mis_driver(cls):
        # 为了保障代码的健壮性,防止异常报错,先判断当前是否有浏览器驱动对象是否存在
        if cls.__mis_driver is not None and cls.__mis_key:
            # 关闭浏览器
            time.sleep(4)
            # quit()只是关闭整个浏览器但是并不会将__driver的值设置为空,而是保留一串缓存字符串
            cls.__mis_driver.quit()
            # 将__driver设置为空
            cls.__mis_driver = None

    # app系统获取驱动对象得方法
    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            desired_caps = dict()
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = 'emulator-5554'
            desired_caps['appPackage'] = 'com.itcast.toutiaoApp'
            desired_caps['appActivity'] = '.MainActivity'
            # 保存登录信息
            desired_caps['noReset'] = True
            cls.__app_driver = appium.webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            # 隐式等待
            cls.__app_driver.implicitly_wait(30)
        return cls.__app_driver

    # 后台管理系统-关闭浏览器驱动的方法
    @classmethod
    def quit_app_driver(cls):
        # 为了保障代码的健壮性,防止异常报错,先判断当前是否有浏览器驱动对象是否存在
        if cls.__app_driver is not None:
            # 关闭浏览器
            time.sleep(4)
            # quit()只是关闭整个浏览器但是并不会将__driver的值设置为空,而是保留一串缓存字符串
            cls.__app_driver.quit()
            # 将__driver设置为空
            cls.__app_driver = None


# 公共获取测试数据方法
def build_data(data_file_path):
    test_data = []
    with open(data_file_path, encoding='utf-8') as f:
        case_data = json.load(f)
        for i in case_data.values():
            test_data.append(list(i.values()))
        print(test_data)
    return test_data


# 二次封装，显示等待
def my_wait(driver, str_xpath):
    try:
        element = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_xpath(str_xpath))
        return element
    except Exception as e:
        NoSuchElementException("找不到{}的元素对象".format(str_xpath))


# 根据文本判断的公共断言方法
def is_element_exist(driver, text):
    str_xpath = "//*[contains(text(),'{}')]".format(text)
    try:
        msg = WebDriverWait(driver, 10, 1).until(lambda x: x.find_element_by_xpath(str_xpath))
        return msg
    except Exception as e:
        logging.error(e)
        NoSuchElementException('no find this xpath{}'.format(text))


# 根据属性判断的公共断言方法
def is_attribute_element_exist(driver, attr_name, attr_value):
    str_xpath = "//*[contains(@{},'{}')]".format(attr_name, attr_value)
    try:
        msg = my_wait(driver, str_xpath)
        return msg
    except Exception as e:
        logging.error(e)
        NoSuchElementException('没找到属性名{}和属性值{}'.format(attr_name, attr_value))
        return False


# 公共下拉框方法
def check_channel_option(driver, option_name, channel_name):
    # 1、选择频道框
    str_xpath = "//*[contains(@placeholder,'{}')]".format(option_name)
    driver.find_element_by_xpath(str_xpath).click()
    # 2、获取所有选项的频道名称
    channel_option = driver.find_elements_by_css_selector(".el-select-dropdown__item span")
    # 默认定义一个是否找到的标识，默认为False
    is_suc = False
    # 3、对获取的频道名称进行遍历
    for option_element in channel_option:
        # 4、判断当前遍历元素的文本信息是否等于我们所想选择的频道名称
        if option_element.text == channel_name:
            # 如果找到，则点击，跳出循环，把默认标识改为True
            option_element.click()
            is_suc = True
            break
            # 如果不相等，鼠标悬浮到当前遍历的元素对象上并按向下键，继续遍历
        else:
            # 创建鼠标对象
            action = ActionChains(driver)
            # 悬停到当前元素对象并按向下的按键
            action.move_to_element(option_element).send_keys(Keys.DOWN).perform()
        # 如果表示任为False，则抛出没找到对应的频道的选项
        if is_suc is False:
            NoSuchElementException("cann't find such element{}".format(channel_name))


# 公用截图方法，截图可以加在程序的任意位置
def get_allure_screenshot(driver, picture_name):
    allure.attach(driver.get_screenshot_as_png(), picture_name, allure.attachment_type.PNG)
