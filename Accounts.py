class Accounts:

    def __init__(self, firstname, lastname):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__username = ""
        self.__password = ""

    def signup(self):
        print("#" * 5 + " Signup Menu " + "#" * 5)
        username = input("Pick a username:  ")
        password = input("Pick a password:  ")

        with open("accounts.csv") as file:
            if username in file.read():
                print("Username already exist")
                self.signup()

        password_confirm = input("Please confirm your password: ")

        if password == password_confirm:
            print("Your Account has been setup.")
            file = open("accounts.csv", "a+")
            file.write(username), file.write(" , ")
            file.write(password), file.write("\n" * 2)
            file.close()
            self.__password = password
            self.__username = username
            self.login()
        elif password != password_confirm:
            print("Your password don't match. Please try again.")
            self.signup()

    def login(self):
        print("\n")
        username = input("Please enter your username:   ")
        password = input("Please enter your password:   ")

        with open("accounts.csv") as file:
            if username and password in file.read():
                print("Access granted")

            elif username and password not in file.read():
                print("Username or Password is wrong")
                self.login()

    def setUsername(self, username):
        self.__username = username

    def setPassword(self, password):
        self.__password = password

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def resetUsername(self):
        old_username = input("Enter old username: ")
        with open("accounts.csv") as file:
            if old_username in file.read():
                new_username = input("Enter new username: ")

            if new_username in file.read():
                print("Username already exist")
                self.resetUsername()
            else:
                self.setUsername(new_username)
                file = open("accounts.csv", "a+")
                file.write(self.getUsername()), file.write(" , ")
                file.write(self.getPassword()), file.write("\n" * 2)
                self.login()

    def resetPassword(self):
        old_password = input("Enter old password: ")
        with open("accounts.csv") as file:
            if old_password in file.read():
                new_password = input("Enter new password: ")

            if new_password in file.read():
                print("Username already exist")
                self.resetPassword()
            else:
                self.setPassword(new_password)
                file = open("accounts.csv", "a+")
                file.write(self.getUsername()), file.write(" , ")
                file.write(self.getPassword()), file.write("\n" * 2)
                self.login()

