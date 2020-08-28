import time

from selenium.webdriver.common.by import By

from base.mp_base.mp_base_page import BasePage, BaseHandle, BaseHandle1
from utils import DriverUtils, check_channel_option


class PubArticlePage(BasePage):
    def __init__(self):
        super().__init__()
        self.article_title = (By.XPATH, "//*[@placeholder='文章名称']")
        self.frame_ele = (By.XPATH, "//*[@id='publishTinymce_ifr']")
        self.article_content = (By.XPATH, "//*[@id='tinymce']")
        self.choose_picture = (By.XPATH, "//*[text()='自动']")
        self.publish_article_btn = (By.XPATH, "//*[text()='发表']")

    def find_article_title(self):
        return self.find_ele(self.article_title)

    def find_frame_ele(self):
        return self.find_ele(self.frame_ele)

    def find_article_content(self):
        return self.find_ele(self.article_content)

    def find_choose_picture(self):
        return self.find_ele(self.choose_picture)

    def find_publish_article_btn(self):
        return self.find_ele(self.publish_article_btn)


class PubArticleHandle(BaseHandle, BaseHandle1):
    def __init__(self):
        self.pub_article_page = PubArticlePage()

    def input_article_title(self, title):
        self.input_text(self.pub_article_page.find_article_title(), title)

    def input_article_content(self, content):
        DriverUtils.get_mp_driver().switch_to.frame(self.pub_article_page.find_frame_ele())
        self.input_text(self.pub_article_page.find_article_content(), content)
        DriverUtils.get_mp_driver().switch_to.default_content()

    def click_choose_picture(self):
        self.click_cz(self.pub_article_page.find_choose_picture())

    def click_choose_channel(self, channel_name):
        check_channel_option(DriverUtils.get_mp_driver(), "请选择", channel_name)

    def click_publish_article_btn(self):
        self.click_cz(self.pub_article_page.find_publish_article_btn())


class PubArticleProxy:
    def __init__(self):
        self.pub_article_handle = PubArticleHandle()

    def publish_article(self, title, content, channel_name):
        self.pub_article_handle.input_article_title(title)
        time.sleep(3)
        self.pub_article_handle.input_article_content(content)
        self.pub_article_handle.click_choose_picture()
        self.pub_article_handle.click_choose_channel(channel_name)
        self.pub_article_handle.click_publish_article_btn()
