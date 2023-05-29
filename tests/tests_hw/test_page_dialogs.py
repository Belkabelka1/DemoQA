from pages.demoqa import DemoQA
from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):
    modaldialog_page = ModalDialogs(browser)
    modaldialog_page.visit()
    assert modaldialog_page.btns_third_menu.check_count_elements(count=5)


def test_navigation_modal(browser):
    modaldialog_page = ModalDialogs(browser)
    demoqa_page = DemoQA(browser)
    modaldialog_page.visit()
    modaldialog_page.refresh()
    modaldialog_page.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert demoqa_page.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)
