from selenium.webdriver.common.by import By

from base.mis_base.mis_base_page import BasePage, BaseHandle
from utils import DriverUtils


class MisLoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.mis_username = (By.CSS_SELECTOR, "[name='username']")
        self.mis_password = (By.CSS_SELECTOR, "[name='password']")
        self.mis_login_btn = (By.CSS_SELECTOR, "#inp1")

    def find_mis_username(self):
        return self.find_ele(self.mis_username)

    def find_mis_password(self):
        return self.find_ele(self.mis_password)

    def find_login_btn(self):
        return self.find_ele(self.mis_login_btn)


class MisLoginHandle(BaseHandle):
    def __init__(self):
        self.mis_login_page = MisLoginPage()

    def input_username(self, username):
        self.input_text(self.mis_login_page.find_mis_username(), username)

    def input_password(self, password):
        self.input_text(self.mis_login_page.find_mis_password(), password)

    def click_btn(self):
        # 删除登录按钮元素对象的disabled属性
        js_str = "document.getElementById('inp1').removeAttribute('disabled')"
        DriverUtils.get_mis_driver().execute_script(js_str)
        # 点击登录按钮
        self.mis_login_page.find_login_btn().click()


class MisLoginProxy:
    def __init__(self):
        self.mis_login_handle = MisLoginHandle()

    def mis_login(self, username, password):
        self.mis_login_handle.input_username(username)
        self.mis_login_handle.input_password(password)
        self.mis_login_handle.click_btn()
