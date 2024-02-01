def cm():
    a = int(input("enter cm"))
    print("Answer  = ",float(a/100))
def gm():
    c=int(input("enter gm"))
    print("answer = ",float(c/1000))
def ml():
    d = int(input("enter ml"))
    print("Answer  = ",float(d/1000))


print("unit converter")
b=int(input("choose any one \n1-cm\n2-gm\n3-ml"))
if b==1:
    cm()

elif b==2:
    gm()
elif b==3:
    ml()
else :
    print("invalid input")


