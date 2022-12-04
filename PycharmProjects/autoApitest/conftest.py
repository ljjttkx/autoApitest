# global conftest.py
# -*- coding: UTF8 -*-

import pymysql
import pytest

from keys.keys import Keys


@pytest.fixture(scope="session", autouse=True)
# session > module > class > function
# function - 所有文件的测试用例执行前都会执行一次
# class - 测试文件中测试类执行前都会执行一次
# module - 每个.py文件执行前都会执行一次
# session - 所有测试文件执行前都执行一次
def token():
    host = 'https://oapi.dingtalk.com'
    path = "/gettoken"
    data = {
            'appkey':"dingds7gtnehss0j02jv",
            'appsecret':"h7NcGdj787qjta3gJla9loSnR6L4SoSE7ENS0o9xQqL3EPnAab8nPAyBZ7_x_eZD"
    }
    k = Keys()
    url = host + path
    r = k.get(url=url, params=data)
    token = r.json()['access_token']
    t = {
        'access_token': token
    }
    return t


@pytest.fixture()
def conn_db():
    db = pymysql.connect('localhost', 'root', '123456', charset='utf8', db='school')
    cur = db.cursor()
    data = cur.fetchall('select * from school')
    print(data)
    yield data
    db.close()
