from Accounts import Accounts


class Student(Accounts):

    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)

    def __str__(self):
        return self.__firstname + " " + self.__lastname

