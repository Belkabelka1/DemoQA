import time
from pages.TextBox_page import TextBox


def test_clear(browser):
    text_box = TextBox(browser)
    text_box.visit()
    text_box.name.send_keys('belka')
    time.sleep(2)
    text_box.name.clear()
    time.sleep(2)
    assert text_box.name.get_text() == ''
    text_box.current_address.send_keys('pp@aa.ru')
    text_box.current_address.clear()
    assert text_box.current_address.get_text() == ''
    # text_box.p_name.send_keys('submit')
    # text_box.submit.clear()
    # assert text_box.p_name.get_text() == ''
