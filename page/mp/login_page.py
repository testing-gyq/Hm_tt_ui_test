import allure
from selenium.webdriver.common.by import By

from base.mp_base.mp_base_page import BasePage, BaseHandle


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.username = (By.XPATH, "//*[@placeholder='请输入手机号']")
        self.code = (By.XPATH, "//*[@placeholder='验证码']")
        self.login_btn = (By.CSS_SELECTOR, ".el-button--primary")

    def find_username(self):
        return self.find_ele(self.username)

    def find_code(self):
        return self.find_ele(self.code)

    def find_login_btn(self):
        return self.find_ele(self.login_btn)


class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    @allure.step(title="输入用户名")
    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)

    # 给方法添加说明
    @allure.step(title="输入验证码")
    def input_code(self, code):
        self.input_text(self.login_page.find_code(), code)

    @allure.step(title="点击登录")
    def click_login_btn(self):
        self.login_page.find_login_btn().click()


class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    def login(self, username, code):
        self.login_handle.input_username(username)
        self.login_handle.input_code(code)
        self.login_handle.click_login_btn()
