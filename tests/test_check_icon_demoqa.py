from pages.demoqa import DemoQA


def test_icon_exist(browser):
    demo_qa_page = DemoQA(browser)
    demo_qa_page.visit()
    demo_qa_page.icon.click()  # demo_qa_page.click_on_the_icon()
    assert demo_qa_page.icon.exist()
    assert demo_qa_page.equal_url()


def test_equal_url(browser):
    demo_qa_page = DemoQA(browser)
    demo_qa_page.visit()
    assert demo_qa_page.equal_url
