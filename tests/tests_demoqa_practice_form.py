from datetime import date
from selene import browser
from selenium.webdriver.chrome.options import Options
from python_automation_hw_5.data.gender_enum import Gender
from python_automation_hw_5.data.hobbies_enum import Hobbies
from python_automation_hw_5.data.users.user import Student
from python_automation_hw_5.model.pages.student_registration_page import StudentRegistrationPage

chrome_options = Options()
chrome_options.page_load_strategy = 'eager'
browser.config.driver_options = chrome_options
browser.config.window_width = 1920
browser.config.window_height = 1080


def test_registration_student():
    registration = StudentRegistrationPage()
    student = Student(
        first_name='Иван',
        last_name='Иванов',
        email='ivan-ivanov@sample.com',
        gender=Gender.MALE,
        mobile_number='0123456789',
        date_of_birth=date(1994, 2, 3),
        subject='Maths',
        hobbies=Hobbies.SPORTS,
        picture='image.jpg',
        current_address='Pushkin street, 87',
        state='Haryana',
        city='Panipat'
    )
    registration.open()

    registration.fill_form(student)
    registration.submit()

    registration.should_have_registered(student)


