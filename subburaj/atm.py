print("welcome to IOB ATM")

print("enter your atm card")
print("please don't remove your atm card")
p = int(input("enter your four digit pin"))
a = int(input("please choose banking for for  cash withdraw\n1-banking,\n2-services,\n3-change password"))
b = int(input("please select account type\n1-savings,\n2-current"))

if a == 1 and b == 1:
    c = int(input("enter the amount"))
    print("the transaction is proceed")
elif a == 1 and b == 2:
    c = int(input("enter the amount"))
    print("the transaction is done")
elif a == 2:
    print("what kind of services you want")

elif a == 3:
    int(input("enter the password you want to change"))
    print("your pin is changed ")

else:
    print("invalid input")
