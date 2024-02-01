import numpy as np
import matplotlib.pyplot as plt

x = np.array(["subburaj", "akil", "akash", "mukilan", "prakash"])
y = np.array([450,440, 490, 463, 450])

plt.plot(x, y)


plt.title("average mark of students")

plt.xlabel("students name ")
plt.ylabel("total marks scored in 10th std")

plt.plot(y, 'o:r')


plt.plot(y, marker = '*')
plt.grid()

plt.show()