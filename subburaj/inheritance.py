class phone:
    def _init_(self,ram,rom,os,fcamcounts,bcamcounts):
        self.ram = ram
        self.rom = rom
        self.fcamcounts = fcamcounts
        self.bcamcounts = bcamcounts
        self.os = os
    def printspecs(self):
        print("Mobile Phone Ram = ",self.ram,"\nRom = ",self.rom,"\nfcamcounts =",self.fcamcounts,"\nbcamcounts =",self.bcamcounts,"\nos =",self.os)






class redmi(phone):
    pass

redmi1=redmi(4, 128, 11, 2, 4)

redmi1.printspecs(self)
