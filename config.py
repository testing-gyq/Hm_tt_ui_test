import logging.handlers

PUB_ARTICLE_TITLE = None

# 发布的文章标题数据
PUB_ARITCAL_TITLE = None


# 日志打印基础配置方法
def log_basic_config():
    # 1.创建日志器
    logger = logging.getLogger()
    # 2.设置日志级别
    logger.setLevel(logging.INFO)
    # 3.创建处理器
    ls = logging.StreamHandler()
    lht = logging.handlers.TimedRotatingFileHandler("./log/hmtt_test.log", when="midnight", interval=1, backupCount=2)
    # 4.创建格式化器
    formatter = logging.Formatter(
        fmt='%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s')
    # 5.将格式化器绑定到处理器
    ls.setFormatter(formatter)
    lht.setFormatter(formatter)
    # 6.将处理器添加到日志
    logger.addHandler(ls)
    logger.addHandler(lht)

# allure generate report/ -o report/html --clean
# 用allure generate工具将json报告转换成html格式，从json文件所在目录读取json文件，-o转译成html文件所在目录，
# --clean是因为html文件中可能有内容，需要先删除一下
