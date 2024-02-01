# atm process

print(input("welcome to SBI atm""\n""please insert your atm card"))

pin = 2243



pin = int(input("please enter your four digit pin"))
if pin == 2243:
    print("your pin is correct")

else:
    print("your pin is incorrect, your password must have only four characters")

if pin == 2243:
    choice = int(input("please choose your option \n1 - banking\n2- ministatement"))
else:
    print("incorrect pin ")
if choice == 1:
    option = int(input(" \n1- withdrawl \n2-deposit\n3- transfer"))
    if option == 1:
        balance = 200000
        withdrawl = int(input("enter the amount"))
        print(withdrawl)
        remain_amount = withdrawl-balance
        print("your available balance", remain_amount)
        print("transcation sucessful")
    elif option == 2:
        balance = 200000
        deposit = int(input("insert the amount"))
        print(deposit)
        remain_balance = deposit+balance
        print("your available balance ", remain_balance)
        print("transcation sucessful")
    elif option == 3:
        ac_no = int(input("enter the 11 digit account number "))
        print(ac_no)
        if ac_no < 99999999999:
            balance = 200000
            rupee = int(input("enter the amount you want to send "))
            print(rupee)
        remain = rupee - balance
        print("your available balance is", remain)
        print("transcation sucessful")
    else:
        print("your a 0000""")
        print(statement)


 elif (choice == 2:ccount number is incorrect"):

  statement = (""" balance = 200000
12/6/22 Transfer to paytm - -2000
20/56/22 Transfer by Gpay - +3000
25/6/22 Transfer  to phone pe - 8000
28/6/22 Tranfer from Tesla - +10
  print("choose correct option")