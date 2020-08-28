from selenium.webdriver.common.by import By

from base.mp_base.mp_base_page import BasePage


class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        self.content_management = (By.XPATH, "//*[text()='内容管理']")
        self.publish_article = (By.XPATH, "//*[contains(text(),'发布文章')]")

    def find_content_management(self):
        return self.find_ele(self.content_management)

    def find_publish_article(self):
        return self.find_ele(self.publish_article)


class HomeHandle:
    def __init__(self):
        self.home_page = HomePage()

    def click_content_management(self):
        self.home_page.find_content_management().click()

    def click_publish_article(self):
        self.home_page.find_publish_article().click()


class HomeProxy:
    def __init__(self):
        self.home_handle = HomeHandle()

    def home(self):
        self.home_handle.click_content_management()
        self.home_handle.click_publish_article()
