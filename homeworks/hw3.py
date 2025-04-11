# 1)  Задание - ( ООП - Инкапсуляция ):
#       - Внутри папки hw создать файл hw3.py       - Внутрь файла main.py создать класс Hero ( Добавьте атрибуты на свое усмотрение и методы attack, protection, rest)       - В класс Hero добавьте приватный атрибут с названием __random_int 
#       - Внутри  __random_int используйте модуль random который будет рандомно генерировать 1,2 или 3
#       - Создйте метод get_random_int 2)  Задание - ( ООП - Абстракция ):
#       - Внутри класса Hero создайте абстрактные методы unique_attack, unique_scream и action
#       - В файле hw3.py создайте дочерный класс Jester наследуя класс Hero
#       - В абстрактных методах unique_attack и unique_scream пропишите любую логику на свое усмотрение       - В абстрактном методе action нужно будет обратиться к методу get_random_int  и в зависимости от содержания метода  нужно будет прописать следующую логику:
#     Если будет 1 то вызывается родительский метод attack
#     Иначе если будет 2 то вызывается родительский метод protection
#     Иначе если будет 3 то вызывается родительский метод rest
# 3) Задание GIT       - Удалите файл .idea 
#       - Создайте файл .gitignore
#       - В файл  .gitignore добавте следующии директории .venv, venv, pycache, .idea
#       - Создайте комит “HW: Did hw3”
#       - Отправьте пуш на ваш репозиторий и прикрепите ссылку к вашему ДЗ
from main import Hero

class Jester(Hero):
    def unique_attack(self):
        print(f"{self.name} наносит хаотичный удар смехом!")

    def unique_scream(self):
        print(f"{self.name} кричит: Ха-ха-ха, ты проиграл!")

    def action(self):
        rand = self.get_random_int()
        if rand == 1:
            self.attack()
        elif rand == 2:
            self.protection()
        elif rand == 3:
            self.rest()

j = Jester("Шут", 100)
j.unique_attack()
j.unique_scream()
j.action()
