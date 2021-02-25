
import pytest

from data.base_data import login_data_success
from pages.login_page import LoginPage
from common.handle_logging import log

class TestLogin():

    @pytest.mark.parametrize('test_info', login_data_success)
    def test_login_success(self, test_info, browser):
        '''验证登录成功后，比对账号信息'''
        expected = test_info['expected']
        actual = LoginPage(browser).get().login_success(test_info['username'], test_info['pwd']).get_user_info()
        try:
            assert expected == actual
        except AssertionError as e:
            log.error('用例--登录--执行不通过')
            log.debug('预期结果是：{}'.format(expected))
            log.debug('实际结果是：{}'.format(actual))
            log.critical(e)
            raise e
        else:
            log.info('用例--登录--执行通过')
