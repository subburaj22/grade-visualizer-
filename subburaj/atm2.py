print("welcome to SBI ATM")
a=int(input("enter use card or cardless\n1-card\n2-cardless"))
print("please enter your ATM card ")
b=int(input("enter your four digit pin"))
if b==2004:
    c=int(input("enter banking or ministatement\n1-banking,\n2-ministatement"))

    if c==1:
            d=int(input("choose the option\n1-withdrwal\n2-deposit\n3-transfer"))
            if d==1:
                balance=10000
                e=int(input("enter the ammount"))
                print("collect the cash")
                print("balance ammount",balance-e)
            elif d==2:
                balance=10000
                i=int(input("enter the account number"))
                f=int(input("insert the deposit ammount"))
                print("the ammount is deposited")
                print("balance ammount",balance+f)
            elif d==3:
                balance=10000
                g=int(input("enter the account number"))
                h=int(input("enter the ammount you transfer"))
                print("your transfer is successfull")
                print("balance ammount",balance-h)
            else:
                print("invalid input")
    else:
        print("ministatement")

else:
     print("invalid pin")