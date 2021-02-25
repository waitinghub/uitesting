
import logging
import os
import time
# import pyautogui
# import pyperclip
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from common.handle_config import read_config
from common.handle_path import IMG_PATH

DEFAULT_TIMEOUT = 20
DEFAULT_POLL = .5

class BaseAction:

    host = read_config.get('env', 'host')   # goto()使用

    def __init__(self, browser):
        self.browser = browser

    def refresh(self):
        '''刷新'''
        self.browser.refresh()

    def quit(self):
        '''关闭浏览器'''
        self.browser.quit()

    def clear(self, locator):
        '''清空'''
        el = self.wait_presence(locator)
        el.clear()
        return self

    def type(self, locator, words):
        '''输入'''
        el = self.wait_presence(locator)   # 将显性等待封装到各种操作中
        el.send_keys(words)
        return self

    def click(self, locator):
        '''点击'''
        el = self.wait_clickable(locator)
        el.click()
        return self

    def click_sleep(self,locator):
        el = self.browser.find_element(*locator)
        time.sleep(3)
        el.click()
        return self

    def right_click(self, locator):
        '''右击'''
        el = self.wait_clickable(locator)
        ActionChains(self.browser).context_click(el).perform()
        return self

    def double_click(self, locator):
        '''双击'''
        el = self.wait_clickable(locator)
        ActionChains(self.browser).double_click(el).perform()
        return self

    def select(self, locator, words):
        Select(self.wait_clickable(locator)).select_by_visible_text(words)
        return self

    def drag(self, start_locator, end_locator):
        ac = ActionChains(self.browser)
        el_start = self.wait_clickable(start_locator)
        el_end = self.wait_clickable(end_locator)
        ac.drag_and_drop(el_start, el_end).perform()
        return self

    def move_to(self, locator):
        ac = ActionChains(self.browser)
        el = self.wait_clickable(locator)
        ac.move_to_element(el).perform()
        return self

    def switch_to_window(self, window_name):
        self.browser.switch_to.window(window_name=window_name)
        return self

    # def switch_to_frame(self, locator, timeout=TIME_OUT, interval=INTERVAL):
    #     wait = WebDriverWait(self.browser, timeout=timeout, poll_frequency=interval)
    #     wait.until(expected_conditions.frame_to_be_available_and_switch_to_it(locator))
    #     return self
    #
    # def switch_to_alert(self, locator, timeout=TIME_OUT, interval=INTERVAL):
    #     wait = WebDriverWait(self.browser, timeout=timeout, poll_frequency=interval)
    #     el = wait.until(expected_conditions.alert_is_present)
    #     return el

    def scroll_to_bottom(self):
        '''滚动到底部'''
        self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        return self

    def scroll_to(self, width, height):
        '''滚动到'''
        self.browser.execute_script(f'window.scrollTo({width}, {height})')
        return self

    # def upload(self, locator, file):
    #     el = self.wait_element(locator)
    #     if el.tag_name == 'input':
    #         el.send_keys(file)
    #         return self
    #     el.click()
    #     pyperclip.copy(file)
    #     time.sleep(.2)
    #     pyautogui.hotkey('ctrl', 'v')
    #     pyautogui.press('enter', presses=2)
    #     return self

    def find(self, locator):
        return self.browser.find_element(*locator)

    def goto(self, url:str):
        '''访问url'''
        if url.startswith(('http://', 'https://')):
            return self.browser.get(url)
        if not url.startswith('/'):
            return ValueError('url must start with /.')
        url = self.host + url
        return self.browser.get(url)

    def screen_shot(self):
        '''截图保存'''
        pic_name = os.path.join(IMG_PATH, time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + '.png')
        self.browser.save_screenshot(pic_name)

    def wait_clickable(self, locator, timeout=DEFAULT_TIMEOUT, poll=DEFAULT_POLL):
        """显性等待 - 等待可点击"""
        el = ''
        try:
            wait = WebDriverWait(self.browser, timeout=timeout, poll_frequency=poll)
            el = wait.until(expected_conditions.element_to_be_clickable(locator))
        except Exception as er:
            self.screen_shot()
            logging.error("等待元素超时{}".format(er))
        return el


    def wait_visible(self, locator, timeout=DEFAULT_TIMEOUT, poll=DEFAULT_POLL):
        '''显性等待 - 等待可见'''
        el = ''
        try:
            wait = WebDriverWait(self.browser, timeout=timeout, poll_frequency=poll)
            el = wait.until(expected_conditions.visibility_of_element_located(locator))
        except Exception as er:
            self.screen_shot()
            logging.error("等待元素超时{}".format(er))
        return el


    def wait_presence(self, locator, timeout=DEFAULT_TIMEOUT, poll=DEFAULT_POLL):
        '''显性等待 - 等待出现'''
        el = ''
        try:
            wait = WebDriverWait(self.browser, timeout=timeout, poll_frequency=poll)
            el = wait.until(expected_conditions.presence_of_element_located(locator))
        except Exception as er:
            self.screen_shot()
            logging.error("等待元素超时{}".format(er))
        return el


    def dropdown(self, div_child_num, item_child_num):
        '''
        Element UI下select方法
        :param div_child_num: el-select-dropdown.el-popper:nth-child所在的div是第几层（包含script，div）
        :param item_child_num: 下拉菜单中的选项是第几个
        :return:
        '''
        drop_down = self.browser.find_element_by_css_selector(
            'body > div.el-select-dropdown.el-popper:nth-child(' + str(div_child_num) + ') > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')
        time.sleep(.5)
        drop_down.find_element_by_css_selector(
            'body > div.el-select-dropdown.el-popper:nth-child(' + str(div_child_num) + ') > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(' + str(item_child_num) + ') > span').click()
        return self

    def confirm_button(self):
        '''Element UI下确认弹出框上的按钮点击'''
        dialog = self.browser.find_element_by_css_selector('body > div.el-dialog__wrapper.tip-messages')
        time.sleep(1)
        dialog.find_element_by_css_selector(
            'body > div.el-dialog__wrapper.tip-messages > div.el-dialog > div.el-dialog__body > div.tip-msg-box > div.text-center > button').click()
        return self