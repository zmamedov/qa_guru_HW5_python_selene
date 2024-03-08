from qa_guru_HW5_python_selene.data.users import User
from qa_guru_HW5_python_selene.pages.registration_page import RegistrationPage


def test_filling_form():
    registration_page = RegistrationPage()
    gercog = User(first_name='Gercog', last_name='Perkins', email='Chester@mail.com', gender='Male',
                  phone_number=7890005670, year_of_birthday=1950, month_of_birthday='January', day_of_birthday=16,
                  subject='Chemistry', hobby='Reading', picture='Chester-Mills.jpeg',
                  current_address='Chester-Mills, Center', state='Haryana', state_city='Karnal')

    registration_page.open()
    registration_page.register(gercog)
    registration_page.should_have_registered(gercog)
