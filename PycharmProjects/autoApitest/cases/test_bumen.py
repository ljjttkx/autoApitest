import pytest
import allure

from common.read_conf import get_ini
from common.read_yaml import read_yaml
from keys.keys import Keys
from common.logger_util import Log


@allure.feature('测试用例 - 部门')
class TestBm:
    host = get_ini('conf/conf.ini', 'qa', 'url')
    k = Keys()
    log = Log().logger

    @pytest.mark.parametrize('args', read_yaml('data/bumen.yaml'))
    def test_create(self, token, args):
        self.log.info('创建部门')

        url = self.host + args['path']
        self.log.info('url：{}'.format(url))

        r = self.k.post(url=url, params=token, json=args['data'])
        self.log.info('参数：{}'.format(args['data']))

        self.k.assert_equal(r.text, 'errmsg', args['validate']['errmsg'])
        self.log.info('返回结果为：{}'.format(r.text))






        


