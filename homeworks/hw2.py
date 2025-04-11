# Домашнее задание по теме \\\"Наследование и полиморфизм\\\"
 
# Декопозиция проекта:   - В своем проекте создайте две директории         * HomeWorks        * Lessons   - В Lessons создайте файлы lessoon1.py lesson2.py ( Можете не заполнять эти файлы данными просто пустые файлы. )
# Наследование:   - В директории HomeWorks создайте файл hw2.py   - В файле hw2.py создайте родительский класс Heroes.   - В классе Heroes создайте следующие методы и атрибуты:       
# * name - атрибут       * hp - атрибут       * action - метод ( что будет делать этот метод на ваше усмотрение )       * attack - метод ( что будет делать этот метод на ваше усмотрение )
#    - В этом же файле hw2.py создайте дочерний класс Archer, который наследуется от Heroes.
# Полиморфизм:   - В классе Archer должны быть свои: Атрибуты arrows (количество стрел) и precision (точность).
#   - Измение метод attack, который теперь будет уменьшает количество стрел на 1 и выводит сообщение об успешной или неудачной атаке в зависимости от точности.
#   - Добавьте новый метод rest, который добавляет 5 стрел и выводит сообщение о пополнении стрел.
#   - Добавьте новый метод status, который возвращает информацию о текущем состоянии персонажа (имя, здоровье и любые уникальные атрибуты для подклассов).
#   - Создайте экземпляр класса и вызовите его методы
 
# 4. Git:
#       - Создайте комит “HW: Did hw2”
#       - Отправьте пуш на ваш репозиторий и прикрепите ссылку к вашему ДЗ 
class Heroes:
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
        return f"Имя: {self.name}, HP: {self.hp}, Стрелы: {self.arrows}, Точность: {self.precision}"


archer1 = Archer("Леголас", 100, 3, 0.8)
archer1.action()
archer1.attack()
archer1.attack()
archer1.rest()
print(archer1.status())
