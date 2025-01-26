from tkinter.font import names


class Agronomist():
    def __init__(self,name,endurance):
        self.name = name
        self.endurance = endurance

    def plant(self):
        print(f"{self.name} сажает огород")
        self.endurance -=2

    def watering(self):
        print(f"{self.name} поливает огород")
        self.endurance -=4


    def fertilizes(self):
       print(f"{self.name} удобряет огород")
       self.endurance -= 2


    def weeding(self):
       print(f"{self.name} пропалывает огород")
       self.endurance -= 3


    def sleep(self):
       print(f"{self.name} спит")
       self.endurance += 4


    def eat(self):
        print(f"{self.name} кушает")
        self.endurance += 3

    def info(self):
        print(f"имя агронома - {self.name}")
        print(f"выносливость агронома - {self.endurance}")

agronom = Agronomist("Петр",10)
agronom.plant()
agronom.info()

agr1 = Agronomist( name="Степан", endurance= 75)
agr2 = Agronomist( name="Гриша", endurance= 88)

print(agr1. name)
print(agr1. endurance)
print(agr2. name)
print(agr2. endurance)

agr1.sleep()
agr1.eat()
agr1.plant()
agr1.watering()
agr1.fertilizes()
agr1.weeding()
agr1.info()

agr2.sleep()
agr2.eat()
agr2.plant()
agr2.watering()
agr2.fertilizes()
agr2.weeding()
agr2.info()


