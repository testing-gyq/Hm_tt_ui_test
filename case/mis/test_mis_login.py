import pytest

from page.mis.mis_login_page import MisLoginProxy
from utils import DriverUtils, is_element_exist, build_data


@pytest.mark.run(order=102)
class TestMisLogin:
    def setup_class(self):
        self.driver = DriverUtils.get_mis_driver()
        self.mis_login_proxy = MisLoginProxy()

    @pytest.mark.parametrize(("mis_username", "mis_password", "text"),
                             build_data(
                                 r"F:\黑马\黑马就业班\UI自动化测试\课堂练习\day11\HM_TT_UI_TEST\data\mis_data\mis_login_data.json"))
    def test_mix_login(self, mis_username, mis_password, text):
        self.mis_login_proxy.mis_login(mis_username, mis_password)
        assert is_element_exist(self.driver, text)
