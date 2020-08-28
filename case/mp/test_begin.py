import pytest

from utils import DriverUtils

@pytest.mark.run(order=1)
class TestBegin:
    def test_begin(self):
        print("order_v1.2.0")
        #关闭浏览器驱动的开关
        DriverUtils.chang_mp_key(False)
