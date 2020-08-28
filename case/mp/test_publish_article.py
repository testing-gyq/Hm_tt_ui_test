import time

import pytest

import config
from page.mp.home_page import HomeProxy
from page.mp.pub_article_page import PubArticleProxy
from utils import DriverUtils, build_data, is_element_exist, get_allure_screenshot


@pytest.mark.run(order=3)
class TestPublishArticle:
    def setup_class(self):
        self.driver = DriverUtils.get_mp_driver()
        self.pub_article_proxy = PubArticleProxy()
        self.home_proxy = HomeProxy()

    def teardown_class(self):
        DriverUtils.quit_mp_driver()

    # setup运行第二个用例是不会执行，需要用下面的方法
    def setup_method(self):
        DriverUtils.get_mp_driver().get("http://ttmp.research.itcast.cn/")

    @pytest.mark.parametrize(("title", "content", "channel_name", "text"), build_data(
        r"F:\黑马\黑马就业班\UI自动化测试\课堂练习\day11\HM_TT_UI_TEST\data\mp_data\mp_publish_data.json"))
    def test_publish_article(self, title, content, channel_name, text):
        config.PUB_ARTICLE_TITLE = title.format(time.strftime("%Y%m%d-%H%M%S"))
        print(config.PUB_ARTICLE_TITLE)
        self.home_proxy.home()
        self.pub_article_proxy.publish_article(title, content, channel_name)
        get_allure_screenshot(self.driver, "发布文章截图")
        assert is_element_exist(self.driver, text)
