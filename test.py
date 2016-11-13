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

class test(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test(self):
        success = True
        wd = self.wd
        wd.get("https://market.yandex.ru/")
        if not ("Маркет" in wd.find_element_by_xpath("//a[@class='logo logo_type_link logo_part_market']/span[@class='logo_text']").text):
            success = False
            print("verifyTextPresent failed")
        wd.find_element_by_link_text("Каталог").click()
        check_exists_by_xpath("//h1[text()='основные категории товаров']")
        check_exists_by_xpath("//h1[text()='Популярные товары']")
        check_exists_by_xpath("//h1[text()='Вас также могут заинтересовать']")
        check_exists_by_xpath("//h1[text()='Статьи и подборки']")
        wd.find_element_by_link_text("Электроника").click()
        wd.find_element_by_link_text("Телефоны").click()
        count_phone_by_xpath("//div(include(a[text()='Популярные'])/ul/li")
        count_phone_by_xpath("//div(include(a[text()='Новинки'])/ul/li")
        wd.find_elements_by_xpath("//a[text()='Расширенный поиск->']").click()
        check_exists_by_xpath("//a[@title='Мобильные телефоны']")
        wd.find_element_by_xpath("//input[@name='glf-pricefrom-var']").send_keys("5125")
        count_price_by_text(5125)
        wd.find_element_by_xpath("//input[@name='glf-priceto-var']").send_keys("10123")
        count_price_by_text(10123)
        if not wd.find_elements_by_xpath("//input[@id='glf-onstock-select']").is_selected():
           wd.find_element_by_id("glf-onstock-select").click()
        if check_exists_by_xpath("//label[text()='смартфон' or text()='телефон' or text()='телефон для детей' or text()='телефон для пожилых']"):
           pass
        else:
           wd.find_elements_by_xpath("//span[text()='Тип']").click()
        if not wd.find_elements_by_xpath("//label(text()='смартфон')/preceding::[2]/span[@class='checkbox checkbox_size_s i-bem checkbox_theme_normal checkbox_js_inited checkbox_checked_yes checkbox_hovered_yes']]").is_selected():
           wd.find_elements_by_xpath("//label(text()='смартфон')/preceding-sibling::[1]/input").click()
        if not wd.find_elements_by_xpath("//label(text()='Android')/preceding::[2]/span[@class='checkbox checkbox_size_s checkbox_theme_normal i-bem checkbox_js_inited checkbox_checked_yes checkbox_hovered_yes]").is_selected():
           wd.find_elements_by_xpath("//label(text()='Android')/preceding-sibling::[1]/span/input").click()
        f = open('log_phone.txt','w')
        for i in range(1,3):
            rating = wd.find_elements_by_xpath("//div[@class='rating hint i-bem rating_outline_yes hint_js_inited']").text()
            if rating>=3.5 and rating<=4.5:
                name_phone = wd.find_elements_by_xpath("//div[@class='rating hint i-bem rating_outline_yes hint_js_inited']//preceding-sibling::[1]//a[@class='snippet-card__header-link shop-history__link link i-bem link_js_inited'/span").text()
                sum_from = wd.find_elements_by_xpath("//div[@class='rating hint i-bem rating_outline_yes hint_js_inited']//preceding-sibling::[1]//div[@class='snippet-card__info']/a/div(include(text(),'от'))/span").text()
                sum_to = wd.find_elements_by_xpath("//div[@class='rating hint i-bem rating_outline_yes hint_js_inited']//preceding-sibling::[1]//div[@class='snippet-card__info']/a/div(include(text(),'до'))/span").text()
                f.write(name_phone+' '+sum_from+'-'+sum_to+'\n')
        f.close()

    def check_exists_by_xpath(xpath):
        return len(webdriver.find_elements_by_xpath(xpath)) > 0

    def count_phone_by_xpath(xpath):
        return len(webdriver.find_elements_by_xpath(xpath))== 3

    def count_price_by_text(text):
        return len(webdriver.find_elements_by_xpath("//input[text()='$text'")) > 0

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
