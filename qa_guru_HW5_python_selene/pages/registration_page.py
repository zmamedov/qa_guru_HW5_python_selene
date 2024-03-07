from selene import browser, have

from qa_guru_HW5_python_selene.recource import path


class RegistrationPage():

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_user_email(self, value):
        browser.element('#userEmail').type(value)

    def click_gender_checkbox(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    def fill_user_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_birthday(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__day--016').type(day).click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def click_hobby(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def upload_picture(self, file_name):
        browser.element('#uploadPicture').send_keys(path('Chester-Mills.jpeg'))
