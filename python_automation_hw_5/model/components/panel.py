from selene import browser, by
from python_automation_hw_5.model.pages.text_box import TextBox


class Panel:
    def __init__(self):
        self.container = browser.element('.left-pannel')

    def open(self, group, element):
        self.container.element(by.text(group)).click()
        self.container.element(by.text(element)).click()

    def open_text_box(self):
        self.open('Elements', 'Text Box')
        return TextBox()
