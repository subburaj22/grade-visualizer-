a=int(input("select the student number\n1-roll-1\n2-roll-2\n3-roll-3"))
if a==1:
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.array("Sub-1", "Sub-2", "Sub-3", "Sub-4", "Sub-5")
    y = np.array(90,85, 95, 70, 100)

    plt.plot(x, y)


    plt.title("mark of student-1 in each subjects")


    plt.xlabel("subject name ")
    plt.ylabel("total marks scored in each subject")

    plt.plot(y,'o:r')


    plt.plot(y, marker = '+')
    plt.grid()
    plt.show()
elif a==2:
    import numpy as np
    import matplotlib.pyplot as plt
    x = np.array(["Sub-1", "Sub-2", "Sub-3", "Sub-4", "Sub-5"])
    y = np.array([100,75, 85, 70, 100])

    plt.plot(x, y)


    plt.title("mark of student-2 in each subjects")

    plt.xlabel("subject name ")
    plt.ylabel("total marks scored in each subject")

    plt.plot(y, 'o:r')


    plt.plot(y, marker = '+')
    plt.grid()

    plt.show()
elif a==3:


        import numpy as np
        import matplotlib.pyplot as plt



        x = np.array(["Sub-1", "Sub-2", "Sub-3", "Sub-4", "Sub-5"])
        y = np.array([90, 82, 85, 100, 95])

        plt.plot(x, y)

        plt.title("mark of student-3 in each subjects")

        plt.xlabel("students name ")
        plt.ylabel("total marks scored in each subject")

        plt.plot(y, 'o:r')

        plt.plot(y, marker='+')
        plt.grid()
        plt.show()


else:
    print("invalid input")