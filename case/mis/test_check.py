import logging
import time

import pytest

import config
from page.mis.mis_home_page import MisHomeProxy
from page.mis.mis_login_page import MisLoginProxy
from page.mis.mis_review_article_page import RewAriProxy
from utils import DriverUtils, is_element_exist


@pytest.mark.run(order=103)
class TestCheck:
    def setup_class(self):
        self.driver = DriverUtils.get_mis_driver()
        self.rew_ari_proxy = RewAriProxy()
        self.mis_home_proxy = MisHomeProxy()
        self.mis_login_proxy = MisLoginProxy()

    def teardown_class(self):
        DriverUtils.quit_mis_driver()

    def setup(self):
        time.sleep(3)
        self.driver.get("http://ttmis.research.itcast.cn/#/home")

    # 为了方便调试
    # @pytest.mark.run(order=1)
    # def test_login(self):
    #     self.mis_login_proxy.mis_login("testid", "testpwd123")

    # @pytest.mark.parametrize(("article_title"),
    #                          build_data(r"F:\黑马\黑马就业班\UI自动化测试\课堂练习\day11\HM_TT_UI_TEST\data\mis_data\check_data.json"))
    def test_check(self):
        title = config.PUB_ARTICLE_TITLE
        logging.info(title)
        self.mis_home_proxy.home()
        self.rew_ari_proxy.check_pass(title)
        assert is_element_exist(self.driver, "驳回")

    def test_reject(self):
        self.mis_home_proxy.home()
        self.rew_ari_proxy.check_reject()
        assert is_element_exist(self.driver, "驳回")
