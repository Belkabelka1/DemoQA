from components.components import WebElement
from pages.base_page import BasePage


class TextBox(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.name = WebElement(driver, '#userName')
        self.current_address = WebElement(driver, 'textarea#currentAddress')
        self.submit = WebElement(driver, 'button#submit')
        self.p_name = WebElement(driver, 'p#name')
        self.p_current_address = WebElement(driver, 'p#currentAddress')
