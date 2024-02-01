a=int(input("select any one\n1-idly,\n2-dosa,\n3-vadai,"))

if a==1:
    b=int(input("enter quantity"))
    p=b*10
    print("your bill is ",p)


elif a==2:
    b=int(input("enter quantity"))
    p=b*20
    print("your bill is ",p)

elif a==3:
    b=int(input("enter quantity"))
    p=b*6
    print("your bill is ",p)

else:
    print("invalid input")