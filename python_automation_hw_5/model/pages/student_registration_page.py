from selene import browser, have
from python_automation_hw_5 import resource
from python_automation_hw_5.data.users.user import Student


class StudentRegistrationPage:
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        return self

    def fill_form(self, student: Student):
        browser.element('#firstName').type(student.first_name)
        browser.element('#lastName').type(student.last_name)
        browser.element('#userEmail').type(student.email)
        browser.all('.custom-radio').element_by(have.text(student.gender.value)).click()
        browser.element('#userNumber').type(student.mobile_number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(student.date_of_birth.strftime('%B'))
        browser.element('.react-datepicker__year-select').send_keys(student.date_of_birth.year)
        browser.element(f'.react-datepicker__day--0{student.date_of_birth.day:02d}').click()
        browser.element('#subjectsInput').type(student.subject).press_enter()
        browser.all('[for^="hobbies-checkbox"]').element_by(have.exact_text(student.hobbies.value)).click()
        browser.element('#uploadPicture').send_keys(resource.path(student.picture))
        browser.element('#currentAddress').type(student.current_address)
        browser.element('#state').click()
        browser.element(f'//div[text()="{student.state}"]').click()
        browser.element('#city').click()
        browser.element(f'//div[text()="{student.city}"]').click()
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def should_have_registered(self, student: Student):
        browser.all('tbody tr').should(have.exact_texts(
            f'Student Name {student.first_name} {student.last_name}',
            f'Student Email {student.email}',
            f'Gender {student.gender.value}',
            f'Mobile {student.mobile_number}',
            f'Date of Birth {student.date_of_birth.day:02d} {student.date_of_birth.strftime("%B")},{student.date_of_birth.year}',
            f'Subjects {student.subject}',
            f'Hobbies {student.hobbies.value}',
            f'Picture {student.picture}',
            f'Address {student.current_address}',
            f'State and City {student.state} {student.city}'
        ))
        return self