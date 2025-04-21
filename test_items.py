import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class TestLanguages:
    def test_items_in_cart(self, browser, request):
        language = request.config.getoption("browser_language")
        link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
        browser.get(link)
        browser.implicitly_wait(30)

        addToBasketButton = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
        assert addToBasketButton.is_displayed(), "Кнопка 'Добавить в корзину' не найдена" 