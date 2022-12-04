from common.read_conf import get_ini


class TestBb:

    host = get_ini('conf/conf.ini', 'qa', 'url')

    def demo(self, token):
        print(token)
        print('demo')

