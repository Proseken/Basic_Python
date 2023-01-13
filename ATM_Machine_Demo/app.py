import time

print("please insert Your Card")

time.sleep(5)

password = 0000

pin = int(input("Enter your atm pin "))

balance=5000

if pin == password:
    while True:

        print("""
            1 == balance
            2 == withdraw balance
            3 == deposit balance
            4 == exit
            """
            )

        try:
            option=int(input("Please enter your choice "))
        except:
            print("Please enter valid option")

        if option == 1:
            print(f"Your current balance is {balance}")

            print("************************************************")
            print("************************************************")
            print("************************************************")


        if option == 2:
            
                withdraw_amount=int(input("please enter withdraw_amount "))

                balance=balance-withdraw_amount

                print(f"{withdraw_amount} is debited from your account")

                print(f"your updated balance is {balance}")
 
                print("************************************************")
                print("************************************************")
                print("************************************************")       

        if option == 3:

                deposit_amount=int(input("please enter deposit_amount "))

                balance=balance-deposit_amount

                print(f"{deposit_amount} is credited to your account")

                print(f"your updated balance is {balance}")

                print("************************************************")
                print("************************************************")
                print("************************************************")
                
        if option == 4:

                break

else:
    print("wrong pin please")
    
 #if you want to get the description of each lines of code watch out for the README.me files
