# Сущности должны быть открыты для расширения, но закрыты для изменения

# Расширение за счет наследования
class Weapon:
    # избавляемся от типа оружия в классе
    # type: # str
    damage: int
    dmg_range: int

    def __init__(self, damage, dmg_range):
        self.damage = damage
        self.dmg_range = dmg_range


# Делаем сколько угодно новых оружий (открыт на расширение)
# В код класса оружие не лезем (закрыт на изменерние)
class Sword(Weapon):

    def __init__(self, dmg, dmg_range):
        super().__init__(dmg, dmg_range)


class Crossbow(Weapon):

    def __init__(self, dmg, dmg_range):
        super().__init__(dmg, dmg_range)


sword = Sword(10, 20)
crossbow = Crossbow(30, 45)
print(sword.damage)
print(crossbow.damage)


class Attacker:

    def attack(self, weapon: Weapon):
        print(f"Урон: {weapon.damage}")


char = Attacker()
char.attack(Sword(10, 20))
