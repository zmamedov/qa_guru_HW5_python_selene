from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: int
    year_of_birthday: int
    month_of_birthday: str
    day_of_birthday: int
    subject: str
    hobby: str
    picture: str
    current_address: str
    state: str
    state_city: str
