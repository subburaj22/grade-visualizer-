print("welcome to AZ company")
print("what is your name ")
a = input("enter your name")
b = int(input("enter your age"))


class Person:
    def __init__(self, name, age):
        self.name = a
        self.age = b

    def myfunc(self):
        print("Hello my name is " + self.name , "\n i am" , self.age ,"years old")


p1=Person("a",b)
p1.myfunc()
