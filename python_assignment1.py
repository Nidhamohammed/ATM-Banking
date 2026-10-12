print("ATM MENU")
curr_bal=5000
option=0
# option=int(input("1.Check balance,2.Deposit money,3.Withdraw money,4.Exit Chosse an option:"))

while True:
    option=int(input("1.Check balance,2.Deposit money,3.Withdraw money,4.Exit Chosse an option:"))


    if option==1:
        print("Current account balance:",curr_bal)
    elif option==2:
        dep_amt=int(input("Enter the amount to be deposited:"))
        curr_bal+=dep_amt
        print("Amount deposited successfully!")
        print("Current account balance:",curr_bal)
    elif option==3:
        with_amt=int(input("Enter the amount to be withdrawed:"))
        if with_amt<=curr_bal:
            curr_bal-=with_amt
            print("Withdrawal successful!")
            print("Current account balance:",curr_bal)
        else:
            print("Insufficient balance")
            print("Current account balance:",curr_bal)
    
    elif option==4:
        print("Exit successful")
        break
    else:
        print("Invalid option")