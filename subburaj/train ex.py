a=int(input("select bording station\n1-rajapalayam\n2-sivakasi\n3-madurai"))
b=int(input("select destination station\n1-rajayapalayam\n2-sivakasi\n3-madurai"))
c=int(input("enter how many passengers travels"))


if a==1 and b==1:
    print("invalid statement")


elif a==1 and b==2:
    ticket=20
    print("your travel is from\n rajapalayam to sivakasi ")
    print("ammount for the ticket\n",ticket*c)

elif a==1 and b==3:
    ticket=90
    print("your travel is from\n rajapalayam to madurai ")
    print("ammount for the ticket\n",ticket*c)

elif a==2 and b==1:
    ticket2=20
    print("your travel is from\n sivakasi to rajapalayam ")
    print("ammount for the ticket\n",ticket2*c)
elif a==2 and b==2:
    print("invalid input")
elif a==2 and b==3:
    ticket=100
    print("your travel is from\n sivakasi to madurai ")
    print("ammount for the ticket\n",ticket*c)

elif a==3 and b==1:
    ticket3=90
    print("your travel is from\n madurai to rajapalayam ")
    print("ammount for the ticket\n",ticket3*c)

elif a==3 and b==2:
    ticket5=100
    print("your travel is from\n madurai to sivakasi ")
    print("ammount for the ticket\n",ticket5*c)
elif a==3 and b==3:
    print("invalid input")
else :
    print("choose any one")


f = open("raj.txt", "r")
print(f.read())
f = open("raj.txt", "a")
f.write("bording station"+  str(a) +  "destination station station"+  str(b) + "number of passengers"+  str(c) +  "you want to pay" + str(ticket*c ))
