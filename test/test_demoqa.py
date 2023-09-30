from selene import browser, command, be, have
import os


def test_demoqa():
    browser.open('/')
    # Имя, фамилия, электронная почта, пол и номер телефона
    browser.element('#firstName').type('Anna')
    browser.element('#lastName').type('Torgova')
    browser.element('#userEmail').type('test_anna@mail.ru')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('79990001122')
    # Дата рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="10"]').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1996"]').click()
    browser.element('.react-datepicker__day--026').click()
    # Предмет и хобби
    browser.element("#subjectsInput").type("Arts").press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    # Картинка
    browser.element('[id="stateCity-label"]').perform(command.js.scroll_into_view)
    browser.element('#uploadPicture').send_keys(os.path.abspath('picture/test.jpg'))
    # Адрес
    browser.element('#currentAddress').type('Saint-Petersburg')
    browser.element('#react-select-3-input').type('NCR').click().press_enter()
    browser.element('#react-select-4-input').type('Delhi').click().press_enter()
    # Создание анкеты
    browser.element('#submit').click()

    # Проверка данных
    browser.element('.modal-content').should(be.visible)
    browser.element('.table').all('td:nth-of-type(2)').should(have.texts(
        'Anna Torgova',
        'test_anna@mail.ru',
        'Female',
        '7999000112',
        '26 November,1996',
        'Arts',
        'Sports, Reading, Music',
        'test.jpg',
        'Saint-Petersburg',
        'NCR Delhi'))
