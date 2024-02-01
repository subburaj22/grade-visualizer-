a = int(input("Select any one\n1-idly\n2-dhosa"))

if a==1:
    b=int(input("Enter quantity"))
    p=b*10
    print("Price to pay ",p)

elif a==2:
    b=int(input("Enter quantity"))
    p=b*50
    print("Price to pay ",p)

else:
    print("Invalid input")