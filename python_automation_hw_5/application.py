from selene import browser
from python_automation_hw_5.model.components.panel import Panel
from python_automation_hw_5.model.pages.text_box import TextBox


class Application:
    def __init__(self):
        self.text_box = TextBox()
        self.panel = Panel()

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        return self