a=int(input("enter phy mark"))
b=int(input("enter che mark"))
c=int(input("enter maths mark"))
if(a==b==c==100):
    {
        print("scholarship is 50%")
    }
elif(a==b==100 or a==c==100 or b==c==100):
    {
        print("scholarship is 30%")
    }
elif(a==100 or b==100 or c==100):
    {
        print("scholarship is 10%")
    }
else:
    {
        print("scholarship is 0%")
    }