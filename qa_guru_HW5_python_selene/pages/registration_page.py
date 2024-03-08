from selene import browser, have

from qa_guru_HW5_python_selene.data.users import User
from qa_guru_HW5_python_selene.recource import path


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.gender = browser.all('[name=gender]')
        self.user_number = browser.element('#userNumber')
        self.birthday = browser.element('#dateOfBirthInput')
        self.year_of_birthday = browser.element('.react-datepicker__year-select')
        self.month_of_birthday = browser.element('.react-datepicker__month-select')
        self.day_of_birthday = browser.element('.react-datepicker__day--016')
        self.subject = browser.element('#subjectsInput')
        self.hobby = browser.all('.custom-checkbox')
        self.picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#react-select-3-input')
        self.state_city = browser.element('#react-select-4-input')
        self.submit_button = browser.element('#submit')

    def open(self):
        browser.open('/automation-practice-form')

    def register(self, user: User):
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.user_email.type(user.email)
        self.gender.element_by(have.value(user.gender)).element('..').click()
        self.user_number.type(user.phone_number)
        self.birthday.click()
        self.month_of_birthday.type(user.month_of_birthday)
        self.year_of_birthday.type(user.year_of_birthday)
        self.day_of_birthday.type(user.day_of_birthday).click()
        self.subject.type(user.subject).press_enter()
        self.hobby.element_by(have.exact_text(user.hobby)).click()
        self.picture.send_keys(path(user.picture))
        self.current_address.type(user.current_address)
        self.state.type(user.state).press_enter()
        self.state_city.type(user.state_city).press_enter()

        self.submit_button.click()

    def should_have_registered(self, user: User):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            str(user.phone_number),
            f'{user.day_of_birthday} {user.month_of_birthday},{user.year_of_birthday}',
            user.subject,
            user.hobby,
            user.picture,
            user.current_address,
            f'{user.state} {user.state_city}'))
