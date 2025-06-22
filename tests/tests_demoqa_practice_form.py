from python_automation_hw_5.data.users import Student
from python_automation_hw_5.model.pages.student_registration_page import StudentRegistrationPage


def test_registration_student(setup_browser):
    registration = StudentRegistrationPage()
    registration.browser = setup_browser

    student = Student(
        'Иван',
        'Иванов',
        'ivan-ivanov@sample.com',
        'Male',
        '0123456789',
        '1994',
        'February',
        '03',
        'Maths',
        'Sports',
        'image.jpg',
        'Pushkin street, 87',
        'Haryana',
        'Panipat'
    )

    registration.open()

    registration.fill_first_name(student.first_name)
    registration.fill_last_name(student.last_name)
    registration.fill_email(student.email)
    registration.choose_gender(student.gender)
    registration.fill_mobile_number(student.mobile_number)
    registration.fill_date_of_birth(student.year, student.month, student.day)
    registration.choose_subject(student.subject)
    registration.choose_hobbies(student.hobbies)
    registration.upload_picture(student.picture)
    registration.fill_current_address(student.current_address)
    registration.choose_state(student.state)
    registration.choose_city(student.city)
    registration.submit()

    registration.should_be_visible_success_title()
    registration.should_have_registered(student)
    registration.should_be_clickable_modal_close_button()

