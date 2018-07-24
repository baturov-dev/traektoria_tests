# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_registration(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_registration(self):
        success = True
        wd = self.wd
        wd.get("http://test.traektoria.ru:8008/")
        wd.find_element_by_css_selector("button").click()
        wd.find_element_by_css_selector("span.trigger").click()
        wd.find_element_by_link_text("Регистрация").click()
        wd.find_element_by_css_selector("button").click()
        wd.find_element_by_name("USER_NAME").click()
        wd.find_element_by_name("USER_NAME").clear()
        wd.find_element_by_name("USER_NAME").send_keys("Петя")
        wd.find_element_by_name("USER_LAST_NAME").click()
        wd.find_element_by_name("USER_LAST_NAME").clear()
        wd.find_element_by_name("USER_LAST_NAME").send_keys("Васин")
        wd.find_element_by_xpath("//div[@class='bx-auth']/noindex/form/table/tbody/tr[3]/td[2]/input").click()
        wd.find_element_by_xpath("//div[@class='bx-auth']/noindex/form/table/tbody/tr[3]/td[2]/input").clear()
        wd.find_element_by_xpath("//div[@class='bx-auth']/noindex/form/table/tbody/tr[3]/td[2]/input").send_keys("pevas")
        wd.find_element_by_xpath("//div[@class='bx-auth']//td[.='*Пароль:']").click()
        wd.find_element_by_xpath("//div[@class='bx-auth']/noindex/form/table/tbody/tr[4]/td[2]/input").click()
        wd.find_element_by_xpath("//div[@class='bx-auth']/noindex/form/table/tbody/tr[4]/td[2]/input").clear()
        wd.find_element_by_xpath("//div[@class='bx-auth']/noindex/form/table/tbody/tr[4]/td[2]/input").send_keys("yes123")
        wd.find_element_by_name("bform").click()
        wd.find_element_by_name("USER_CONFIRM_PASSWORD").click()
        wd.find_element_by_name("USER_CONFIRM_PASSWORD").clear()
        wd.find_element_by_name("USER_CONFIRM_PASSWORD").send_keys("yes123")
        wd.find_element_by_name("USER_EMAIL").click()
        wd.find_element_by_name("USER_EMAIL").clear()
        wd.find_element_by_name("USER_EMAIL").send_keys("pevas@yandex.ru")
        wd.find_element_by_name("Register").click()
        wd.find_element_by_css_selector("button").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
