"""Kundalik uchun qilingan dastur"""

class Talaba():
    def __init__(self, name, last_name, tyil):
        self.name = name
        self.last_name = last_name
        self.tyil = tyil
        self.bosqich = 1
    
    def tanishtir(self):
        print(f"{self.name} {self.last_name} {self.tyil} da tug'ilgan. {self.bosqich} kursda o'qiydi")
        
    def fullname(self):
        print(f"{self.name} {self.last_name}")
        
    def get_name(self):
        return self.name
    
    def get_last_name(self):
        return self.last_name
    
    def set_bosqich(self, yangi_bosqich):
        self.bosqich = yangi_bosqich
        
    def update_bosqich(self):
        self.bosqich += 1

class Fan():
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
        
    def add_student(self, talaba):
            self.talabalar.append(talaba)
            self.talabalar_soni += 1
    
    def get_students(self):
        return [x.fullname() for x in self.talabalar]
            
    def get_students_num(self):
        return self.talabalar_soni


while True:
    savol = input("O'quvchilarni qo'shasizmi?: ")
    if savol == "n":
        break
    else:
        talaba_name = str(input("name: "))
        talaba_last_name = str(input("last_name: "))
        tyil = input("Tugilgan yil")
        yangi_talaba = Talaba(talaba_name, talaba_last_name, tyil)
matem.add_student(yangi_talaba)
matem.talabalar_soni
print(matem.get_students())


baholangan_talabalar = {}
talabalar = matem.talabalar
while talabalar:
    tolib = talabalar.pop()
    baho = input(f"{tolib.get_name()}ning bahosini kiriting: ")
    print(f"{tolib.get_name()} baholandi")
    baholangan_talabalar[tolib.get_name()] = int(baho)
print(talabalar)