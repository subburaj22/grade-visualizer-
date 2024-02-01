a=int(input("enter any number"))
b=int(input("enter another number"))
print("answer",a+b)

f = open("cal.txt", "r")
print(f.read())
f = open("cal.txt", "w")
print(f.write("answer="+str(a+b)))