from pages.TextBox_page import TextBox


def test_textbox(browser):
    testbox_page = TextBox(browser)
    testbox_page.visit()
    testbox_page.name.send_keys('Belka')
    testbox_page.current_address.send_keys('33')
    testbox_page.submit.click_force()
    assert testbox_page.p_name.get_text() == 'Name:Belka'
    assert testbox_page.p_current_address.get_text() == 'Current Address :33'

