from dataclasses import dataclass


@dataclass
class Student:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile_number: str
    year: str
    month: str
    day: str
    subject: str
    hobbies: str
    picture: str
    current_address: str
    state: str
    city: str

