from Student import Student


def main():
    while True:
        print("#" * 75)
        choice = input("#1 Login | #2 Signup | #3 Reset Username | #4 Reset Password | #5 Exist:  ")
        print("#" * 75)
        print("\n")
        student = Student("", "")

        if choice == "1":
            student.login()
        elif choice == "2":
            student.signup()
        elif choice == "3":
            student.resetUsername()
        elif choice == "4":
            student.resetPassword()
        elif choice == "5":
            exit()


main()
