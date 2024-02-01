list=["subburaj","akhil","akash","ajih","sushanthan","mukilan","logesh","prakash"]
a=int(input("choose any one  1-student name\n2-change student name \n3-identify student name \n4-add student \n5-change student name  \n6-remove student"))

if a==1:
    print(list)


elif a==2:
    list[1] = "ashok"
    print(list)


elif a==3:
    print(list[-1])

elif  a==4:
    list.append("orange")
    print(list)

elif a==5:
    list[1:3] = ["raj", "subbu"]
    print(list)
elif a==6:
    list.remove("logesh")
    print(list)
else :
    print("invalid input")




