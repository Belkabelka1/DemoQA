import time
from pages.accordion_page import AccordianPage


def test_visible_accordion(browser):
    accordian_page = AccordianPage(browser)
    accordian_page.visit()
    assert accordian_page.section1.visible()
    accordian_page.section1Heading.click()
    time.sleep(2)
    assert not accordian_page.section1.visible()


def test_visible_accordion_default(browser):
    accordian_page = AccordianPage(browser)
    accordian_page.visit()
    assert not accordian_page.section21.visible()
    assert not accordian_page.section22.visible()
    assert not accordian_page.section3.visible()