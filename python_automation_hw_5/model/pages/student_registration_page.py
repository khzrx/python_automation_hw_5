from selene import browser, have, be, command
from selene.core.condition import Condition
from python_automation_hw_5 import resource
from python_automation_hw_5.data.users import Student
import allure


class StudentRegistrationPage:

    @allure.step('Открыть страницу регистрации студента.')
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    @allure.step('Заполнить имя значением {value}.')
    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    @allure.step('Заполнить фамилию значением {value}.')
    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    @allure.step('Заполнить email значением {value}.')
    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    @allure.step('Выбрать значение пола {value}.')
    def choose_gender(self, value):
        browser.all('.custom-radio').element_by(have.text(value)).click()
        return self

    @allure.step('Заполнить номер телефона значением {value}.')
    def fill_mobile_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    @allure.step('Заполнить дату рождения значениями {year}, {month}, {day}.')
    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element(f'.react-datepicker__day--0{day:0>2}').click()
        return self

    @allure.step('Выбрать предмет со значением {value}.')
    def choose_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    @allure.step('Выбрать хобби со значением {value}.')
    def choose_hobbies(self, value):
        browser.all('[for^="hobbies-checkbox"]').element_by(have.exact_text(value)).click()
        return self

    @allure.step('Добавить изображение {filename}.')
    def upload_picture(self, filename):
        browser.element('#uploadPicture').send_keys(resource.path(filename))
        return self

    @allure.step('Заполнить текущий адрес значением {value}.')
    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    @allure.step('Выбрать штат {value}.')
    def choose_state(self, value):
        state = browser.element('#state')
        state.perform(command.js.scroll_into_view)
        state.click()
        browser.element(f'//div[text()="{value}"]').click()
        return self

    @allure.step('Выбрать город {value}.')
    def choose_city(self, value):
        browser.element('#city').click()
        browser.element(f'//div[text()="{value}"]').click()
        return self

    @allure.step('Кликнуть на кнопку подтверждения регистрации.')
    def submit(self):
        browser.element('#submit').click()
        return self

    @allure.step('Проверить наличие заголовка формы успешной регистрации.')
    def should_be_visible_success_title(self):
        browser.element('#example-modal-sizes-title-lg').should(
            have.text('Thanks for submitting the form'))
        return self

    @allure.step('Проверить соответствие заполненных данных в форме успешной регистрации.')
    def should_have_registered(self, student_data: Student):
        browser.all('tbody tr').should(have.exact_texts(
            f'Student Name {student_data.first_name} {student_data.last_name}',
            f'Student Email {student_data.email}',
            f'Gender {student_data.gender}',
            f'Mobile {student_data.mobile_number}',
            f'Date of Birth {student_data.day} {student_data.month},{student_data.year}',
            f'Subjects {student_data.subject}',
            f'Hobbies {student_data.hobbies}',
            f'Picture {student_data.picture}',
            f'Address {student_data.current_address}',
            f'State and City {student_data.state} {student_data.city}'
        ))
        return self

    @allure.step('Проверить наличие кнопки закрытия формы успешной регистрации.')
    def should_be_clickable_modal_close_button(self):
        browser.element('#closeLargeModal').should(
            Condition.by_and(be.visible, be.clickable)
        )
        return self

