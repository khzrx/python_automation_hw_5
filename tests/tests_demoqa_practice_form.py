from selene import browser, have, be
from selene.core.condition import Condition
from selenium.webdriver.chrome.options import Options

# Обновлена 'page_load_strategy', сайт долго подгружал дополнительные ресурсы
chrome_options = Options()
chrome_options.page_load_strategy = 'eager'
browser.config.driver_options = chrome_options


def test_fill_form():
    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('Иван')
    browser.element('#lastName').type('Иванов')
    browser.element('#userEmail').type('ivan-ivanov@sample.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('0123456789')

    #Заполнение даты рождения в дейтпикере
    browser.element('#dateOfBirthInput').click()
    browser.element('//option[text()="February"]').click() # Поиск по тексту показался более читаемым
    browser.element('option[value="1994"]').click()
    browser.element('.react-datepicker__day--003').click()

    browser.element('#subjectsInput').type('maths').press_enter()
    browser.element('#subjectsInput').type('chem').press_enter()

    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element('[for=hobbies-checkbox-3]').click()

    browser.element('#uploadPicture').send_keys(r"C:\Users\user\Pictures\image.png")
    browser.element('#currentAddress').type('Не дом и не улица')

    browser.element('#state').click()
    browser.element('//div[text()="Haryana"]').click()

    browser.element('#city').click()
    browser.element('//div[text()="Panipat"]').click()

    browser.element('#submit').click()

    # Проверки по соответствию данных
    browser.element('#example-modal-sizes-title-lg').should(
        have.text('Thanks for submitting the form'))
    browser.all('tbody tr').should(have.exact_texts(
        'Student Name Иван Иванов',
        'Student Email ivan-ivanov@sample.com',
        'Gender Male',
        'Mobile 0123456789',
        'Date of Birth 03 February,1994',
        'Subjects Maths, Chemistry',
        'Hobbies Reading, Music',
        'Picture image.png',
        'Address Не дом и не улица',
        'State and City Haryana Panipat'
    ))

    # Проверка видимости и кликабельности кнопки закрытия окна
    browser.element('#closeLargeModal').should(
        Condition.by_and(be.visible, be.clickable)
    )
