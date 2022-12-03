# -*- coding: UTF8 -*-
import os

import openpyxl

from common.logger_util import Log


log = Log().logger

# 获取文件路径列表
def get_file(dir):
    file_list = []

    for file_name in os.listdir(dir):
        if file_name.startswith('~'):
            pass
        else:
            f_path = os.path.abspath(dir)
            path = os.path.join(f_path, file_name)
            file_list.append(path)

    return file_list

# 循环找文件
def get_xlsx():
    dir = '../xlsx/'

    file_path = get_file(dir)
    f_data = []

    for f in file_path:
        book = openpyxl.load_workbook(f)
        sheet = book.active

        log.info('用例文件: {}'.format(f))

        title_list = []
        for i in sheet[1]:
            title_list.append(i.value)

        datas = []
        for i in range(2, sheet.max_row+1):
            l = []
            for cell in sheet[i]:
                l.append(cell.value)

            z_data = dict(zip(title_list, l))
            datas.append(z_data)
        f_data.append(datas)
    return f_data

# 写入csv文件
def write_to_csv(self):
    pass


# if __name__ == '__main__':
#     get_xlsx()

