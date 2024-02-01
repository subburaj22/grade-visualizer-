a=int(input("enter the number\n1-student name,\n2-number of student,\n3-add new student"))
stu=["subburaj","akhil","akash","ajith","jeyaadithiya","sushanthan","mukilan","logesh","kabish","samuvel","ashok","santhosh","nevas","kannan","prakash","santhanakumar"]


if a==1:
    print(stu[1])

elif a==2:
    print("number of students",len(stu))



elif a==3:
    print("add a new student ",stu.insert(2,"raj"))

else:
    print("invalid input")