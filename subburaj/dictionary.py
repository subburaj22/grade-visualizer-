a=int(input("choose any one mobile phone\n1-print moto specs \n2-print vivo specs\n3-print oppo specs\n4-print apple specs\n5-print poco specs\n6-print 1+ specs\n7-print redmi specs\n8-print realme specs"))

moto  = {
        "brand":"moto",
        "model": "G6",
        "year": "2020",
        "RAM": "6GB",
        "ROM": "128GB",
        "processor": "android",
        "colour": "black"
}


vivo  ={
        "brand": "vivo",
        "model": "y91i",
        "year": "2019",
        "RAM": "3GB",
        "ROM": "32GB",
        "processor": "android 2.0",
        "colour": "black"
}


oppo  ={
        "brand": "oppo",
        "model": "K10",
        "year": "2018",
        "RAM": "6GB",
        "ROM": "128GB",
        "processor": "android 1.0",
        "colour": "white"
}

apple ={
        "brand": "apple",
        "model": "iphone 11",
        "year": "2019",
        "RAM": "8GB",
        "ROM": "128GB",
        "processor": "A13 bioconic chip",
        "colour": "gold"
}

poco  ={
        "brand": "poco",
        "model": "X3",
        "year": "2021",
        "RAM": "6GB",
        "ROM": "64GB",
        "processor": "snap dragon 732G",
        "colour": "cobalt blue"
}


oneplus ={
        "brand": "1+",
        "model": "CE2",
        "year": "2020",
        "RAM": "6GB",
        "ROM": "64GB",
        "processor": "octa core 2.2GHZ",
        "colour": "blue tide"
}


redmi  ={
        "brand": "redmi",
        "model": "10",
        "year": "2015",
        "RAM": "6GB",
        "ROM": "128GB",
        "processor": "snap dragon 680G",
        "colour": "pacific blue"
}

realme  ={
        "brand": "realme",
        "model": "C31",
        "year": "2020",
        "RAM": "4GB",
        "ROM": "64GB",
        "processor": "unisoc T612",
        "colour": "light silver"
}
if a==1:
        print(moto)

elif a==2:
        print(vivo)

elif a==3:
        print(oppo)

elif a==4:
        print(apple)
elif a==5:
        print(poco)
elif a==6:
        print(oneplus)
elif a==7:
        print(redmi)
elif a==8:
        print(realme)
else :
        print("invalid input")