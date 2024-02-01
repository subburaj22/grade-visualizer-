def volume():
    g=int(input("enter the litre"))
    print("millilitre =", int(g *1000))
    w=int(input("enter the ml"))
    print("litre =",int(w/1000))

def length():
    a = int(input("choose input\n1- meter\n2-kilometer\n3-centimeter\n4-foot"))
    b = int(input("choose output\n1- meter\n2-kilometer\n3-centimeter\n4-foot "))

    if a == 1 and b == 2:
        c = int(input("enter the meter"))
        print("kilometer =", c / 1000)
    elif a == 1 and b == 3:
        d = int(input("enter the meter"))
        print("centi-meter =", int(d * 100))
    elif a == 1 and b == 4:
        e = int(input("enter the meter"))
        print("foot =", int(e * 3.2808))
    elif a == 2 and b == 1:
        f = int(input("enter the kilometer"))
        print("meter =", f * 1000)
    elif a == 2 and b == 3:
        g = int(input("enter the kilometer"))
        print("centimeter =", g * 100000)
    elif a == 2 and b == 4:
        h = int(input("enter the kilometer"))
        print("foot =", h * 3281)
    elif a == 3 and b == 1:
        i = int(input("enter the centimeter "))
        print("meter =", float(i / 100))
    elif a == 3 and b == 2:
        j = int(input("enter the centimeter"))
        print("kilometer=", float(j / 100000))
    elif a == 3 and b == 4:
        k = int(input("enter the centimeter"))
        print("foot =", float(k / 30.48))
    elif a == 4 and b == 1:
        l = int(input("enter the foot"))
        print("meter =", float(l / 3.281))
    elif a == 4 and b == 2:
        m = int(input("enter the foot"))
        print("kilometer =", float(m / 3281))
    elif a == 4 and b == 3:
        n = int(input("enter the foot"))
        print("centimeter =", float(n / 30.48))
    else:
        print("invalid input")

def time():
    a = int(input("choose input\n1- second\n2-minute\n3-hour\n4-day"))
    b = int(input("choose output\n1- second\n2-minute\n3-hour\n4-day "))

    if a == 1 and b == 2:
        c = int(input("enter the second"))
        print("minute =", float(c / 60))

    elif a == 1 and b == 3:
        d = int(input("enter the second"))
        print("hour =", float(d / 3600))

    elif a == 1 and b == 4:
        e = int(input("enter the second"))
        print("day =", float(e / 86400))

    elif a == 2 and b == 1:
        f = int(input("enter the minute"))
        print("second=", float(f * 60))
    elif a == 2 and b == 3:
        g = int(input("enter the minute"))
        print("hour=", float(g / 60))
    elif a == 2 and b == 4:
        h = int(input("enter the minute"))
        print("day=", float(h / 1440))
    elif a == 3 and b == 1:
        i = int(input("enter the hour"))
        print("second=", i * 3600)
    elif a == 3 and b == 2:
        j = int(input("enter the hour"))
        print("minute=", j * 60)
    elif a == 3 and b == 4:
        k = int(input("enter the hour"))
        print("day=", float(k / 24))
    elif a == 4 and b == 1:
        l = int(input("enter the day"))
        print("second=", l * 86400)
    elif a == 4 and b == 2:
        m = int(input("enter the day"))
        print("minute=", m * 1440)
    elif a == 4 and b == 3:
        n = int(input("enter the day"))
        print("hour=", n * 24)
    else:
        print("invalid input")


print("unit converter")
j=int(input("select any one\n1-volume\n2-length\n3-time"))
if j==1:
    volume()

elif j==2:
    length()

elif j==3:
    time()
else :
    print("invalid input")