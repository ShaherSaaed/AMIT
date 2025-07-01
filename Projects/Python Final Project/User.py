import time

class User:
    def __init__(self, ID, first_name, last_name, age):
        self.__ID = ID
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.registration_date = time.asctime()
