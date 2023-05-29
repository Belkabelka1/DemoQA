import time

from pages.form_pages import FormPage


def test_login_form_validate(browser):
    login_form = FormPage(browser)
    login_form.visit()
    assert login_form.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert login_form.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert login_form.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    login_form.btn_submit.click_force()
    time.sleep(10)
    assert login_form.user_form.get_dom_attribute('class') == 'was-validated'