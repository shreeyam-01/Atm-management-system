print("")
print(" ---------> ATM MANAGEMENT SYSTEM <---------")
print("")
balance= 10000
converted_balance=str(balance)
pin=int(int(input("Enter the PIN: ")))

if(pin==4444):
    print("1. Check balance:")    
    print("2. Cash withdrawl")    
    print("3. Cash deposit")    
    print("4. Change pin")

    option=int(input("Choose your option (1-4): "))

    if(option==1):
        print("Your balance is NPR " + converted_balance)

    elif(option==2):
        entered_amount = int(input("Enter the amount to withdraw: NPR "))
        
        if(entered_amount > balance):
            print("The entered amount exceeds the current balance.")
        else:
            balance -= entered_amount
            str_ra = str(balance)
            str_ea = str(entered_amount)
            print("You have sucessfully debited NPR " + str_ea)
            print("Youe remaining balance is NPR " + str_ra)
            
    elif(option==3):
        deposit_amount = int(input("Enter the amount to deposit: NPR "))

        if(deposit_amount < 0):
            print("Error")
        else:
            balance += deposit_amount
            str_balance = str(balance)
            str_da = str(deposit_amount)

            print("You have sucessfully credited NPR " + str_da)
            print("Your current balance is NPR " + str_balance)

    elif(option==4):
        old_pin = int(input("Please enter your old pin: "))

        if(old_pin == pin):    
            new_pin = int(input("Enter the new pin: "))
            print("You have sucessfully changed your pin.")
        else:
            print("Wrong pin!")

else:
    print("Wrong pin")