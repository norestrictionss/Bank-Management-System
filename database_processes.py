from database import mydb

mycursor = mydb.cursor()


def insert_account(name, surname, password):
    money = 0
    informations = "INSERT INTO bilgiler (isim,soyisim,sifre,para) VALUES (%s,%s,%s,%s)"
    values = (name, surname, password, money)
    mycursor.execute(informations, values)
    mydb.commit()


def delete_account(name, surname, password):

    informations = "DELETE FROM bilgiler WHERE isim=%s AND soyisim=%s AND sifre=%s"
    infos = (name, surname, password)
    mycursor.execute(informations, infos)
    mydb.commit()


def withdraw(money_amount, user_id):
    while True:
        try:
            change_quantity = int(input("How much money do you want to withdraw?:"))
            if type(change_quantity) == int:
                if change_quantity > money_amount:
                    print("Quantity of your money is not sufficient for this demand. Try later. ")
                    break
                else:
                    money_amount = money_amount - change_quantity
                    info_update = "UPDATE bilgiler SET para=%s WHERE ID=%s"
                    informations = (money_amount, user_id)
                    mycursor.execute(info_update, informations)
                    mydb.commit()
                    print("Process has been achieved successfully.")
                    break
        except:
            print("You must enter valid data type. Please try again.")


def deposit(money_amount, user_id):
    while True:
        try:
            change_quantity = int(input("How much money do you want to deposit?:"))
            if type(change_quantity) == int:
                money_amount = money_amount + change_quantity
                info_update = "UPDATE bilgiler SET para=%s WHERE ID=%s"
                informations = (money_amount, user_id)
                mycursor.execute(info_update, informations)
                mydb.commit()
                print("Process has been achieved successfully.")
                break
        except:
            print("You must enter valid data type. Please try again.")
