import json
import jsonpath

import requests


class Keys:
    def __init__(self):
        self.session = requests.Session()

    # get
    def get(self, url, params, **kwargs):
        return self.session.get(url=url, params=params, **kwargs)

    # post
    def post(self, url, **kwargs):
        return self.session.post(url=url, **kwargs)

    # get assert text
    def get_text(self, text, key):
        text = json.loads(text)
        value = jsonpath.jsonpath(text, '$..{}'.format(key))
        return value

    # assert 指定字段值
    def assert_equal(self, text, key, expect):
        ac = self.get_text(text, key)
        actual = ''.join(ac)
        assert actual == expect, "ERROR: 预期值: {},实际值: {}".format(expect, actual)

    # 赋值函数：处理数据yaml文件内的字典结构
    '''
        k1:v1
        k2:
            k2.1:v2.1
            k2.2:
        k3:
        有待优化  目前无法处理参数传空的情况，和返回值类型问题，当需要断言内容为字符串时，返回的列表断言会报错
    '''
    def assigment(self, kwars):
        for k, v in kwars.items():
            if type(v) is dict:
                self.assigment(v)
            else:
                if v:

                    pass
                else:
                    kwars[k] = eval(getattr(self, k))
        return kwars
    #  可尝试try except：pass