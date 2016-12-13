import abc


class Weapon(object):

    def __init__(self):
        pass

    @abc.abstractmethod
    def attack(self):
        pass


class Flamethrower(Weapon):

    def attack(self):
        print("Flamethrower")


class MachineGun(Weapon):

    def attack(self):
        print("Machine Gun")


class Rifle(Weapon):

    def attack(self):
        print("Rifle")


class Unit(object):

    def __init__(self, weapon):
        self._weapon = weapon

    def attack(self):
        self._weapon.attack()


class Marine(Unit):

    def double_attack(self):
        self.attack()
        self.attack()


class Firebat(Unit):

    def double_attack(self):
        self.attack()
        self.attack()


class Ghost(Unit):

    def cloaking(self):
        print("ghost cloaking")


if __name__ == "__main__":

    marine = Marine(MachineGun())
    marine.attack()

    firebat = Firebat(Flamethrower())
    firebat.double_attack()

    ghost = Ghost(Rifle())
    ghost.attack()
    ghost.cloaking()



