from uuid import uuid4
from time import asctime
class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__ID = uuid4()
        self.registration_date = asctime()

    def get_id(self):
        return self.__ID

    