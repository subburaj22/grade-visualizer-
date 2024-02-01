class phone:
    def __init__(self,ram,rom,os,fcamcounts,bcamcounts):
        self.ram = ram
        self.rom = rom
        self.fcamcounts = fcamcounts
        self.bcamcounts = bcamcounts
        self.os = os
    def printspecs(self):
        print("Mobile Phone Ram = ",self.ram,"\nRom = ",self.rom,"\nfcamcounts =",self.fcamcounts,"\nbcamcounts =",self.bcamcounts,"\nos =",self.os )

p1 = phone(4,128,11,2,4)
p1.printspecs()

class redmi(phone):
    pass

redmi1 = redmi(4,128,11,2,4)
redmi1.printspecs()


class redmi12(phone):
    pass

redmi11 = redmi12(8,526,13,15,20)
redmi11.printspecs()


class iphone(phone):
    pass

iphone11 =iphone (8,526,15,20,25)
iphone11.printspecs()