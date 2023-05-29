import pytest

from pages.TextBox_page import TextBox
import allure


@pytest.mark.active
@allure.feature('check attr')
@allure.story('Проверка атрибута placeholder')
@allure.title('Проверка поля Имя')
@allure.severity(allure.severity_level.NORMAL)
def test_placeholder(browser):
    text_box = TextBox(browser)
    text_box.visit()
    assert text_box.name.get_dom_attribute('type') == 'text'
