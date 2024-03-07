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
    registration_page.fill_current_address('Chester-Mills, Center')
    registration_page.fill_state('Haryana')
    registration_page.fill_state_city('Karnal')

    registration_page.submit()

    # Checking that all fields are filled correctly
    registration_page.should_registered_user_with(
        'Gercog Perkins',
        'Chester@mail.com',
        'Male',
        '7890005670',
        '16 January,1950',
        'Chemistry',
        'Reading',
        'Chester-Mills.jpeg',
        'Chester-Mills, Center',
        'Haryana Karnal',
    )
