import time

from selenium.webdriver.common.by import By

from common.handle_action import BaseAction
from pages.orgmanage_page import OrgmanagePage

class IndexPage(BaseAction):

    user_info_locator = (By.XPATH, '//*[@id="mains"]/section/header/div/div[2]/div/div[2]/div')

    def get_user_info(self):
        '''获取用户名信息'''
        el = self.wait_clickable(self.user_info_locator)
        time.sleep(1)
        self.screen_shot()
        return el.text

    def select_menu_info(self, main_menu, module_menu):
        '''菜单'''
        self.click((By.XPATH, '//*[@id="mains"]/section/section/aside/ul/li[' + str(main_menu) + ']/div/span'))
        self.click((By.XPATH, '//*[@id="mains"]/section/section/aside/ul/li[' + str(main_menu) + ']/ul/li[' + str(module_menu) + ']/span'))
        if main_menu == 2 and module_menu == 1:
            return OrgmanagePage(self.browser)
        else:
            return self











