# Задание 1: Создание класса Hero   1) Создайте класс Hero с атрибутами:
#      * name — имя.      * lvl — уровень.      
# * HP — количество жизни.   
# 2) Добавьте метод introduce, который выводит информацию о герое в формате: \\\"Привет, меня зовут <Имя>, мой lvl <уровень> , мое HP <HP>\\\".
#   3) Создайте экземпляр класса Hero и вызовите метод introduce.
# Задание 2: Методы класса   1) В классе Hero добавьте метод is_adult, который проверяет, является ли герой уровнем выше 10. Если уровень больше или равен 10, метод должен возвращать True, иначе — False.
#   2) Создайте несколько экземпляров класса Hero с разными уровнями и вызовите метод is_adult для каждого.  Задание 3: Репозиторий GItHub.   1) Создать репозиторий OOP-52-2
#   2) Привязать ваше домашнее задание к репозиторию OOP-52-2   3) сделать комит и залить ваше ДЗ на ваш репозиторий OOP-52-2
#   4) Прикрепить ссылку на ваше ДЗ
class Hero:
    def __init__(self, name, lvl, HP):
        self.name = name
        self.lvl = lvl
        self.HP = HP

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой lvl {self.lvl}, мое HP {self.HP}")

    def is_adult(self):
        return self.lvl >= 10

hero1 = Hero("Артур", 5, 100)
hero1.introduce()
hero2 = Hero("Ланселот", 12, 150)
hero3 = Hero("Мерлин", 9, 80)

print(hero1.name, "is adult?", hero1.is_adult())
print(hero2.name, "is adult?", hero2.is_adult())
print(hero3.name, "is adult?", hero3.is_adult())

