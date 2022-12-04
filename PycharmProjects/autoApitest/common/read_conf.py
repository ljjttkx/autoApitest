"""
读取conf.ini文件
"""
import os
from configparser import ConfigParser


# file-文件目录 section- ini文件内的[环境] option- 内容
def get_ini(file, sec, opt):

    c = ConfigParser()
    c.read(file, encoding='utf-8')
    # 如果内部函数有引用外部函数的同名变量或者全局变量，并且对这个变量有修改。
    # 那么 python 会认为它是一个局部变量,又因为函数中没有 xx 的定义和赋值，所以报错：
    # 会引起UnboundLocalError: local variable 'xx' referenced before assignment，加global变全局变量解决
    global host
    host = c.get(sec, opt)
    return host
