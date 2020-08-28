from selenium.webdriver.common.by import By

from base.mis_base.mis_base_page import BasePage, BaseHandle1


class MisHomePage(BasePage):
    def __init__(self):
        super().__init__()
        self.info_management = (By.XPATH, "//*[text()='信息管理']")
        self.con_check = (By.XPATH, "//*[text()='内容审核']")

    def find_info_management(self):
        return self.find_ele(self.info_management)

    def find_con_check(self):
        return self.find_ele(self.con_check)


class MisHomeHandle(BaseHandle1):
    def __init__(self):
        self.mis_home_page = MisHomePage()

    def click_info_management(self):
        self.click_cz(self.mis_home_page.find_info_management())

    def click_con_check(self):
        self.click_cz(self.mis_home_page.find_con_check())


class MisHomeProxy:
    def __init__(self):
        self.mis_home_handle = MisHomeHandle()

    def home(self):
        self.mis_home_handle.click_info_management()
        self.mis_home_handle.click_con_check()
