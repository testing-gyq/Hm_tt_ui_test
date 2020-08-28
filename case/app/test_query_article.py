import unittest

from parameterized import parameterized

from page.app.index_page import IndexProxy
from utils import DriverUtils, is_attribute_element_exist, get_allure_screenshot


class TestQyArticle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtils.get_app_driver()
        cls.index_proxy = IndexProxy()

    @classmethod
    def tearDownClass(cls):
        DriverUtils.quit_app_driver()

    def setUp(self):
        self.driver.start_activity("com.itcast.toutiaoApp", ".MainActivity")

    @parameterized.expand(["软件测试", "linux"])
    def test_query_article(self, channel_name):
        # channel_name = "数据库"
        self.index_proxy.test_qari_by_channel(channel_name)
        get_allure_screenshot(self.driver, "查找频道名")
        self.assertTrue(is_attribute_element_exist(self.driver, "text", "关注"))
