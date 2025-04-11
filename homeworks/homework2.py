class Heroes():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    
    def action(self):
        print(f"{self.name} готов к действию!")

    def attack(self):
        print(f"{self.name} наносит обычную атаку!")

class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            if self.precision >= 0.5:
                print(f"{self.name} точно попадает в цель! Осталось стрел: {self.arrows}")
            else:
                print(f"{self.name} промахивается. Осталось стрел: {self.arrows}")
        else:
            print(f"{self.name} не может атаковать — нет стрел!")

    def rest(self):
        self.arrows += 5
        print(f"{self.name} отдыхает и пополняет стрелы. Теперь стрел: {self.arrows}")

    def status(self):
        print(f"Имя: {self.name}, HP: {self.hp}, Стрелы: {self.arrows}, Точность: {self.precision}")


archer1 = Archer("Леголас", 100, 3, 0.8)
archer1.action()
archer1.attack()
archer1.attack()
archer1.rest()
archer1.status()
