class Hero():
    def __init__(self, name, lvl, HP):
        self.name = name
        self.lvl = lvl
        self.HP = HP
    def introduce(self):
        return f"привет меня зовут {self.name}"
    
    def is_adult(self):
        if self.lvl >= 10:
            return True
        else:
            return False
        
hero1 = Hero("Артур", 5, 100)
print(hero1.introduce())
hero2 = Hero("Ланселот", 12, 150)
hero3 = Hero("Мерлин", 9, 80)

print(hero1.name, "is adult?", hero1.is_adult())
print(hero2.name, "is adult?", hero2.is_adult())
print(hero3.name, "is adult?", hero3.is_adult())
