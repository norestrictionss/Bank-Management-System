import database_processes
import input_processes


def first_process(process, user1):
    if process == '1':
        while True:
            input_processes.get_name(user1)
            input_processes.get_surname(user1)
            input_processes.get_password(user1)
            database_processes.mycursor.execute("SELECT * FROM bilgiler")
            informations = database_processes.mycursor.fetchall()
            account_controller = find_user(user1, informations)
            if account_controller:
                print("Account is already exist. Please try again.")
            else:
                database_processes.insert_account(user1.name, user1.surname, user1.password)
                print("Your account has been created succesfully.")
                break


def second_process(process, user1):
    if process == '2':
        input_processes.get_name(user1)
        input_processes.get_surname(user1)
        input_processes.get_password(user1)
        database_processes.delete_account(user1.name, user1.surname, user1.password)
        print("Your delete proccess has been achieved succesfully.")


def third_process(process, user1):
    if process == '3':
        account_controller = False
        while True:
            input_processes.get_name(user1)
            input_processes.get_surname(user1)
            input_processes.get_password(user1)
            database_processes.mycursor.execute("SELECT * FROM bilgiler")
            informations = database_processes.mycursor.fetchall()
            for x in range(len(informations)):
                if informations[x][1] == user1.name and informations[x][2] == user1.surname and \
                        informations[x][3] == user1.password:
                    money_amount = informations[x][4]
                    user_id = informations[x][0]
                    account_controller = True
            if not account_controller:
                print("Account couldn't be found. Please try again.")
            else:
                database_processes.withdraw(money_amount, user_id)
                break


def find_user(user1, informations):
    for x in range(len(informations)):
        if informations[x][1] == user1.name and informations[x][2] == user1.surname and \
                informations[x][3] == user1.password:
            user1.name = informations[x][1]
            user1.surname = informations[x][2]
            user1.password = informations[x][3]

            user1.money = informations[x][4]
            user1.user_id = informations[x][0]

            return True


def fourth_process(process, user1):
    if process == '4':
        account_controller = False
        while True:
            input_processes.get_name(user1)
            input_processes.get_surname(user1)
            input_processes.get_password(user1)
            database_processes.mycursor.execute("SELECT * FROM bilgiler")
            informations = database_processes.mycursor.fetchall()
            account_controller = find_user(user1, informations)

            if not account_controller:
                print("Account couldn't be found. Please try again.")
            else:
                database_processes.deposit(user1.money, user1.user_id)
                break


def fifth_process(process, user1):
    if process == '5':
        while True:
            input_processes.get_name(user1)
            input_processes.get_surname(user1)
            input_processes.get_password(user1)
            database_processes.mycursor.execute("SELECT * FROM bilgiler")
            informations = database_processes.mycursor.fetchall()
            account_controller = find_user(user1, informations)
            if not account_controller:
                print("User couldn't be found. Please try again.")
            else:
                print("Your name:", user1.name)
                print("Your surname:", user1.surname)
                print("Your money quantity:", user1.money)
                break
