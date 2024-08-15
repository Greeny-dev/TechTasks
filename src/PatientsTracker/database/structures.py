from dataclasses import dataclass
from datetime import date


@dataclass
class Patient:
    fullname: str
    date_of_birth: date
    date_of_visit: date

    def convert_to_tuple(self) -> tuple:
        return self.fullname, self.date_of_birth, self.date_of_visit
