import pytest

from utils import DriverUtils


@pytest.mark.run(order=99)
class TestEnd:
    def test_end(self):
        # 将关闭浏览器驱动的开关打开
        DriverUtils.chang_mp_key(True)
        # 主动调用依稀关闭浏览器驱动的方法
        DriverUtils.quit_mp_driver()
