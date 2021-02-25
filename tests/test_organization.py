import pytest

from data.base_data import organization_data_info
from common.handle_logging import log

class TestOrganage():

    @pytest.mark.parametrize('test_info', organization_data_info)
    def test_add_organization(self, login, test_info):
        index_page = login
        expected = '恭喜您，提交成功！'
        actual = index_page.select_menu_info(test_info['main_menu'], test_info['module_menu']).add_organization(test_info['organization_name'], test_info['province_num'], test_info['city_num'], test_info['contact_person'], test_info['phone_number'], test_info['status_num'])
        try:
            assert expected == actual
        except AssertionError as e:
            log.error('用例--添加机构--执行不通过')
            log.debug('预期结果是：{}'.format(expected))
            log.debug('实际结果是：{}'.format(actual))
            log.critical(e)
            raise e
        else:
            log.info('用例--添加机构--执行通过')


    @pytest.mark.parametrize('test_info', organization_data_info)
    def test_edit_organization(self, login, test_info):
        index_page = login
        expected = '恭喜您，提交成功！'
        actual = index_page.select_menu_info(test_info['main_menu'], test_info['module_menu']).edit_organization(test_info['organization_name'] + 'modify')
        print (actual)
        try:
            assert expected == actual
        except AssertionError as e:
            log.error('用例--编辑机构--执行不通过')
            log.debug('预期结果是：{}'.format(expected))
            log.debug('实际结果是：{}'.format(actual))
            log.critical(e)
            raise e
        else:
            log.info('用例--编辑机构--执行通过')
