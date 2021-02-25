import time
from selenium.webdriver.common.by import By
from common.handle_action import BaseAction

class OrgmanagePage(BaseAction):

    add_button_locator = (By.XPATH, '//*[@id="mains"]/section/section/section/main/div/div[2]/div/button[1]')
    edit_button_locator = (By.XPATH, '//*[@id="mains"]/section/section/section/main/div/div[2]/div/button[2]')
    organization_name_locator = (By.XPATH, '//*[@id="mains"]/section/section/section/main/div/div[4]/div/div[2]/form/div[1]/div/div[1]/input')
    province_selector_locator = (By.XPATH, '//*[@id="mains"]/section/section/section/main/div/div[4]/div/div[2]/form/div[2]/div/div/div[1]/input')
    city_selector_locator = (By.XPATH, '//*[@id="mains"]/section/section/section/main/div/div[4]/div/div[2]/form/div[3]/div/div/div[1]/input')
    contact_person_locator = (By.XPATH, '//*[@id="mains"]/section/section/section/main/div/div[4]/div/div[2]/form/div[4]/div/div/input')
    phone_number_locator = (By.XPATH, '//*[@id="mains"]/section/section/section/main/div/div[4]/div/div[2]/form/div[5]/div/div[1]/input')
    organization_status_locator = (By.XPATH, '//*[@id="mains"]/section/section/section/main/div/div[4]/div/div[2]/form/div[6]/div/div/div/input')
    add_save_locator = (By.XPATH, '//*[@id="mains"]/section/section/section/main/div/div[4]/div/div[3]/div/button[1]')
    confirm_message_locator = (By.CSS_SELECTOR, 'body > div.el-dialog__wrapper.tip-messages > div.el-dialog > div.el-dialog__body > div.tip-msg-box > h3')
    first_data_locator = (By.XPATH, '//*[@id="mains"]/section/section/section/main/div/div[3]/div[1]/div/div[3]/table/tbody/tr[1]/td[2]/div/label/span/span')

    def add_organization(self, organization_name, province_num, city_num, contact_person, phone_number, status_num):
        self.click(self.add_button_locator)
        self.type(self.organization_name_locator, organization_name)
        self.click(self.province_selector_locator)
        self.dropdown(6, province_num)
        time.sleep(.5)
        self.click(self.city_selector_locator)
        self.dropdown(7, city_num)
        self.type(self.contact_person_locator, contact_person)
        self.type(self.phone_number_locator, phone_number)
        self.click(self.organization_status_locator)
        self.dropdown(8, status_num)
        self.click(self.add_save_locator)
        time.sleep(2)
        self.screen_shot()
        success_message = self.find(self.confirm_message_locator).text
        self.confirm_button()
        return success_message


    def edit_organization(self, organization_name):
        self.click_sleep(self.first_data_locator)
        self.click(self.edit_button_locator)
        self.clear(self.organization_name_locator)
        self.type(self.organization_name_locator, organization_name)
        self.click(self.add_save_locator)
        time.sleep(2)
        self.screen_shot()
        success_message = self.find(self.confirm_message_locator).text
        self.confirm_button()
        return success_message



