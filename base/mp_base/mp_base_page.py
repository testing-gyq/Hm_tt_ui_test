from utils import DriverUtils


# 封装查找元素的方法
class BasePage:
    def __init__(self):
        self.driver = DriverUtils.get_mp_driver()

    def find_ele(self, location):
        return self.driver.find_element(*location)


# 封装输入元素操作的方法
class BaseHandle:
    def input_text(self, element, text):
        # 先清除框内内容
        element.clear()
        element.send_keys(text)


# 封装点击操作
class BaseHandle1:
    def click_cz(self, element):
        element.click()
