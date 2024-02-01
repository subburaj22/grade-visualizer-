students=tuple(("subburaj","akhil","akash","ajih","sushanthan","mukilan","logesh","prakash"))
a=int(input("choose any one 1-identify the student\n2-change the student name\n3-add student name\n4-remove student name\n5-print students name\n6-add a list of students\n7-count the number of students"))




if a==1:
    print("enter the number of the student")
    x=int(input("enter the value"))
    print(students[x])

elif a==2:
    y = list(students)
    y[3] = "karthick"
    students = tuple(y)
    print(students)

elif a==3:
    y = list(students)
    y.append("nevas")
    students = tuple(y)
    print(students)


elif a==4:
    y = list(students)
    y.remove("subburaj")
    students = tuple(y)
    print(students)

elif a==5:
    for x in students:
        print(x)


elif a==6:
    student2 = ("raj", "kabish", "kumar")
    student3 = students + student2
    print(student3)

elif a==7:
    len(students)









