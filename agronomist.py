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
        self.endurance -=1


    def fertilizes(self):
       print(f"{self.name} удобряет огород")
       self.endurance -= 1


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


