from dataclasses import dataclass
from python_automation_hw_5.data.gender_enum import Gender
from python_automation_hw_5.data.hobbies_enum import Hobbies
from datetime import date


@dataclass
class Student:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile_number: str
    date_of_birth: date
    subject: str
    hobbies: Hobbies
    picture: str
    current_address: str
    state: str
    city: str