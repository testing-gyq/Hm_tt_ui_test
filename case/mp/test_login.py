import allure
import pytest

from page.mp.login_page import LoginProxy
from utils import DriverUtils, build_data, is_element_exist


@pytest.mark.run(order=2)
class TestMp:
    def setup_class(self):
        self.driver = DriverUtils.get_mp_driver()
        self.login_proxy = LoginProxy()

    def teardown_class(self):
        DriverUtils.quit_mp_driver()
    #设置用例级别
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize(("username", "code", "text"),
                             build_data(
                                 r"F:\黑马\黑马就业班\UI自动化测试\课堂练习\day11\HM_TT_UI_TEST\data\mp_data\mp_login_data.json"))
    def test_login(self, username, code, text):
        self.login_proxy.login(username, code)
        assert is_element_exist(self.driver, text)
