from selene import browser
from selenium.webdriver.chrome.options import Options
from python_automation_hw_5.application import Application

chrome_options = Options()
chrome_options.page_load_strategy = 'eager'
browser.config.driver_options = chrome_options
browser.config.window_width = 1920
browser.config.window_height = 1080


def test_registration_text_box():
    app = Application()
    app.open()
    app.panel.open_text_box()

    app.text_box.fill_form('Ivanov Ivan', 'ivanov@ivan.com', 'Pushkina', 'Lenina')
    app.text_box.submit()

    app.text_box.should_be_registered('Ivanov Ivan', 'ivanov@ivan.com', 'Pushkina', 'Lenina')