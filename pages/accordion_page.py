from components.components import WebElement
from pages.base_page import BasePage


class AccordianPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.section1 = WebElement(driver, '#section1Content > p')
        self.section1Heading = WebElement(driver, '#section1Heading')
        self.section21 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.section22 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.section3 = WebElement(driver, '#section3Content > p')