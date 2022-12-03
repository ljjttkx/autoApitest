# -*- coding: UTF8 -*-
import logging, time
import os


class Log:
    def __init__(self, level='INFO'):
        # 创建日志器
        self.logger = logging.getLogger(name='日志信息')
        # 获取日志模块的级别对象属性
        level = getattr(logging, level)
        # 设置日志级别
        self.logger.setLevel(level)
        # 防止重新生成处理器
        if not self.logger.handlers:
            # 创建控制台日志处理器
            sh = logging.StreamHandler()
            # 创建日志文件处理器
            fh = logging.FileHandler(filename=self.get_log(), mode='a', encoding='utf-8')

            # 创建格式器
            fmt = logging.Formatter("[%(asctime)s] [%(levelname)s] [%(filename)s] :%(message)s")

            # 给处理器添加格式
            sh.setFormatter(fmt=fmt)
            fh.setFormatter(fmt=fmt)

            # 给日志器添加处理器
            self.logger.addHandler(sh)
            self.logger.addHandler(fh)

    # 创建存放日志目录
    def make_log(self, dirname='log'):
        dir = os.path.dirname(__file__)
        f_path = os.path.split(dir)[0]
        path = os.path.join(f_path, dirname)
        path = os.path.normpath(path)
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    # 创建日志文件的文件名格式，便于区分每天日志
    def get_log(self):
        filename = "{}.log".format(time.strftime("%Y-%m-%d", time.localtime()))
        filename = os.path.join(self.make_log(), filename)
        filename = os.path.normpath(filename)
        return filename