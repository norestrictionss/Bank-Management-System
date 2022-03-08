def get_name(user):
    user.name = input("Please enter your name:")
    conditions = [True for x in user.name if x in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]]
    print(conditions)
    while True in conditions:
        print("Your name can't include numeric character. Please try again.")
        user.name = input("Please enter your name:")
        conditions = [True for x in user.name if x in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]]


def get_surname(user):
    user.surname = input("Please enter your surname:")
    conditions = [True for x in user.surname if x in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]]
    while True in conditions:
        print("Your surname can't include numeric character. Please try again.")
        surname = input("Please enter your surname:")
        conditions = [True for x in user.surname if x in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]]


def get_password(user):
    while True:
        try:
            user.password = int(input("Please enter your password:"))
            while len(str(user.password)) != 4:
                print("Your password's length must be 4. Please try again.")
                password = int(input("Please enter your password:"))
            if type(user.password) == int:
                break
        except:
            print("Your password can't include any letter. Please try again.")
