

from selenium.webdriver.common.by import By
from common.handle_config import read_config
from common.handle_action import BaseAction
from pages.index_page import IndexPage

class LoginPage(BaseAction):

    url = read_config.get('env', 'host') + ''

    username_el_locator = (By.XPATH, '//*[@id="app"]/div/div/div[2]/input[1]')
    password_el_locator =(By.XPATH, '//*[@id="app"]/div/div/div[2]/input[2]')
    login_el_locator = (By.XPATH, '//*[@id="app"]/div/div/div[2]/button')

    def get(self):
        self.browser.get(self.url)
        return self

    def login_success(self, username, password):
        '''登录'''
        self.type(self.username_el_locator, username)
        self.type(self.password_el_locator, password)
        self.click(self.login_el_locator)
        return IndexPage(self.browser)
