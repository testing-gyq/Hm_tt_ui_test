from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from base.app_page.app_base_page import BasePage, BaseHandle1
from utils import DriverUtils


class IndexPage(BasePage):
    def __init__(self):
        super().__init__()
        # 频道元素对象
        self.channel_option = (By.XPATH, "//*[contains(@text,'{}')]")
        # 频道选项区域元素对象
        self.channel_area = (By.XPATH, "//*[@class='android.widget.HorizontalScrollView']")
        # 第一条文章的元素对象
        self.first_article = (By.XPATH, "//*[contains(@text,'评论')]")

    def find_channel_option(self, channel_name):
        return DriverUtils.get_app_driver().find_element(self.channel_option[0],
                                                         self.channel_option[1].format(channel_name))

    def find_channel_area(self):
        return self.find_ele(self.channel_area)

    def find_first_article(self):
        return self.find_ele(self.first_article)


class IndexHandle(BaseHandle1):
    def __init__(self):
        self.index_page = IndexPage()

    # 选择频道
    def check_channel_option(self, channel_name):

        # 获取区域元素的所在位置
        area_element = self.index_page.find_channel_area()
        x = area_element.location["x"]
        y = area_element.location["y"]
        # 获取区域元素的大小
        w = area_element.size["width"]
        h = area_element.size["height"]
        # 计算其实按住的滑动点坐标
        start_y = y + h * 0.5
        start_x = x + w * 0.8
        # 计算目标位置的坐标
        end_y = start_y
        end_x = x + w * 0.2
        while True:
            # 获取一次界面信息
            page_old = DriverUtils.get_app_driver().page_source
            # 在当前区域中查找我们想选择的频道元素对象
            try:
                # 如果能找到啧点击，然后退出循环
                self.index_page.find_channel_option(channel_name).click()
                break
            except Exception as e:
                # 如果找不到啧再次滑动页面
                DriverUtils.get_app_driver().swipe(start_x, start_y, end_x, end_y)
                # 再次获取界面信息
                page_new = DriverUtils.get_app_driver().page_source
                # 如果滑动之后的页面信息和滑动之前的相等则抛出异常没找到目标的选项
                if page_new == page_old:
                    raise NoSuchElementException("没有找到{}频道")
                    # 点击第一条文章

    def click_first_article(self):
        self.click_cz(self.index_page.find_first_article())


class IndexProxy:
    # 创建初始化属性是因为对象的生命周期，初始化方法是每次运行前要先运行的，
    # 如果直接用实例化方法调用，需要每次都调用一次别的方法，会影响代码的运行效率
    def __init__(self):
        self.index_handle = IndexHandle()

    def test_qari_by_channel(self, channel_name):
        self.index_handle.check_channel_option(channel_name)
        self.index_handle.click_first_article()
