from selene import browser, have

from qa_guru_HW5_python_selene.pages.registration_page import RegistrationPage


def test_filling_form():
    registration_page = RegistrationPage()

    registration_page.open()

    # Filling all fields in the form
    registration_page.fill_first_name('Gercog')
    registration_page.fill_last_name('Perkins')
    registration_page.fill_user_email('Chester@mail.com')
    registration_page.click_gender_checkbox('Male')
    registration_page.fill_user_number('7890005670')
    registration_page.fill_birthday('1950', 'January', '16')
    registration_page.fill_subject('Chemistry')
    registration_page.click_hobby('Reading')
    registration_page.upload_picture('Chester-Mills.jpeg')



    browser.element('#currentAddress').type('Chester-Mills, Center')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()

    browser.element('#submit').click()

    # Checking that all fields are filled correctly
    browser.element('.table').should(have.text('Gercog Perkins'))
    browser.element('.table').should(have.text('Chester@mail.com'))
    browser.element('.table').should(have.text('Male'))
    browser.element('.table').should(have.text('7890005670'))
    browser.element('.table').should(have.text('16 January,1950'))
    browser.element('.table').should(have.text('Chemistry'))
    browser.element('.table').should(have.text('Reading'))
    browser.element('.table').should(have.text('Chester-Mills.jpeg'))
    browser.element('.table').should(have.text('Chester-Mills, Center'))
    browser.element('.table').should(have.text('Haryana Karnal'))
