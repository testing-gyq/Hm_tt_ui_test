import time

from selenium.webdriver.common.by import By

from base.mis_base.mis_base_page import BasePage, BaseHandle, BaseHandle1
from utils import check_channel_option, DriverUtils


class RewAriPage(BasePage):
    def __init__(self):
        super().__init__()
        self.article_title = (By.CSS_SELECTOR, "[placeholder='请输入: 文章名称']")
        self.select_btn = (By.XPATH, "//*[text()='查询']")
        self.pass_btn = (By.XPATH, "//tbody/tr[1]/td[8]/div/button[2]/span")
        self.reject_btn = (By.XPATH, "//tbody/tr[1]/td[8]/div/button[3]/span")
        self.confirm_btn = (By.CSS_SELECTOR, ".el-button--primary")

    def find_article_title(self):
        return self.find_ele(self.article_title)

    def find_select_btn(self):
        return self.find_ele(self.select_btn)

    def find_pass_btn(self):
        return self.find_ele(self.pass_btn)

    def find_reject_btn(self):
        return self.find_ele(self.reject_btn)

    def find_confirm_btn(self):
        return self.find_ele(self.confirm_btn)


class RewAriHandle(BaseHandle, BaseHandle1):
    def __init__(self):
        self.rew_ari_page = RewAriPage()

    def input_article_title(self, article_title):
        self.input_text(self.rew_ari_page.find_article_title(), article_title)

    def choose_state(self, channel_name):
        check_channel_option(DriverUtils.get_mis_driver(), "请选择状态", channel_name)

    def click_select_btn(self):
        self.click_cz(self.rew_ari_page.find_select_btn())

    def click_pass_btn(self):
        self.click_cz(self.rew_ari_page.find_pass_btn())

    def click_reject_btn(self):
        self.click_cz(self.rew_ari_page.find_reject_btn())

    def click_confirm_btn(self):
        self.click_cz(self.rew_ari_page.find_confirm_btn())


class RewAriProxy:
    def __init__(self):
        self.rew_ari_handle = RewAriHandle()

    # 测试通过案例
    def check_pass(self, article_title):
        self.rew_ari_handle.input_article_title(article_title)
        self.rew_ari_handle.choose_state("待审核")
        self.rew_ari_handle.click_select_btn()
        time.sleep(3)
        self.rew_ari_handle.click_pass_btn()
        self.rew_ari_handle.click_confirm_btn()
        # 为了校验通过是否成功，选择已通过的状态断言数据
        self.rew_ari_handle.choose_state("审核通过")
        self.rew_ari_handle.click_select_btn()

    def check_reject(self):
        # 默认选择第一条，不需要选择了
        # self.rew_ari_handle.input_article_title(article_title)
        self.rew_ari_handle.choose_state("待审核")
        self.rew_ari_handle.click_select_btn()
        time.sleep(3)
        self.rew_ari_handle.click_reject_btn()
        self.rew_ari_handle.click_confirm_btn()
        # 切换到审核失败，断言驳回成功
        self.rew_ari_handle.choose_state("审核失败")
        self.rew_ari_handle.click_select_btn()
