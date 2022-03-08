import optional_processes


class User:
    name = ""
    surname = ""
    password = ""
    money=""
    user_id=""


def main():
    print("Welcome to the bank account management system.\nPlease enter the process that you want to do:")
    while True:
        user1 = User()
        print("1.Create account")
        print("2.Delete account")
        print("3.Withdraw")
        print("4.Deposit")
        print("5. Show account information")
        process = input()
        optional_processes.first_process(process, user1) or optional_processes.second_process(process, user1) or \
        optional_processes.third_process(process, user1) or optional_processes.fourth_process(process, user1) or \
        optional_processes.fifth_process(process,user1)

        validation = input("Do you want to continue?(y/n):")
        while validation not in ["Y", "y", "N", "n"]:
            print("Invalid character. Please try again.")
            validation = input("Do you want to continue for other processes?(y/n):")
        if validation in ["Y", "y"]:
            pass
        else:
            break


if __name__ == "__main__":
    main()
