class Attacker:

    # Функция оружия - атаковать
    def attack(self):
        pass


class Reloader:
    # Перезарядить оружие
    def reload(self):
        pass


class Knife(Attacker):
    # Нож не перезаряжается
    pass


class Pistol(Attacker, Reloader):
    # А пистолет перезаряжается
    pass

