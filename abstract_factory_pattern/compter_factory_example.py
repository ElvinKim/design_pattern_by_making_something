import abc
import enum

VENDOR = enum.Enum("VENDOR", "SAMSUNG LG APPLE")


class Case(abc.ABC):
    pass


class SamsungCase(Case):

    def __str__(self):
        return "Samsung Case"


class LGCase(Case):

    def __str__(self):
        return "LG Case"


class Power(abc.ABC):
    pass


class SamsungPower(Power):

    def __str__(self):
        return "Samsung Power"


class LGPower(Power):

    def __str__(self):
        return "LG Power"


class CPU(abc.ABC):
    pass


class SamsungCPU(CPU):

    def __str__(self):
        return "Samsung CPU"


class LGCPU(CPU):

    def __str__(self):
        return "LG CPU"


class Memory(abc.ABC):
    pass


class SamsungMemory(Memory):

    def __str__(self):
        return "Samsung Memory"


class LGMemory(Memory):

    def __str__(self):
        return "LG Memory"


class MainBoard(abc.ABC):
    pass


class SamsungMainBoard(MainBoard):

    def __str__(self):
        return "Samsung MainBoard"


class LGMainBoard(MainBoard):

    def __str__(self):
        return "LG MainBoard"


class HardDisk(abc.ABC):
    pass


class SamsungHardDisk(HardDisk):

    def __str__(self):
        return "Samsung HardDisk"


class LGHardDisk(HardDisk):

    def __str__(self):
        return "LG HardDisk"


class GraphicCard(abc.ABC):
    pass


class SamsungGraphicCard(GraphicCard):

    def __str__(self):
        return "Samsung Graphic Card"


class LGGraphicCard(GraphicCard):

    def __str__(self):
        return "LG Graphic Card"


class Computer:
    def __init__(self):
        self._case = None
        self._power = None
        self._main_board = None
        self._memory = None
        self._hard_disk = None
        self._graphic_card = None
        self._cpu = []

    def append_cpu(self, cpu):
        self._cpu.append(cpu)

    @property
    def cpu(self):
        return self._cpu

    @property
    def case(self):
        return self._case

    @case.setter
    def case(self, case):
        self._case = case

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, power):
        self._power = power

    @property
    def main_board(self):
        return self._main_board

    @main_board.setter
    def main_board(self, main_board):
        self._main_board = main_board

    @property
    def memory(self):
        return self._memory

    @memory.setter
    def memory(self, memory):
        self._memory = memory

    @property
    def hard_disk(self):
        return self._hard_disk

    @hard_disk.setter
    def hard_disk(self, hard_disk):
        self._hard_disk = hard_disk

    @property
    def graphic_card(self):
        self._graphic_card

    @graphic_card.setter
    def graphic_card(self, graphic_card):
        self._graphic_card = graphic_card


class Factory(abc.ABC):

    @abc.abstractmethod
    def create_cpu(self):
        pass

    @abc.abstractmethod
    def create_memory(self):
        pass

    @abc.abstractmethod
    def create_power(self):
        pass

    @abc.abstractmethod
    def create_case(self):
        pass

    @abc.abstractmethod
    def create_hard_disk(self):
        pass

    @abc.abstractmethod
    def create_mainboard(self):
        pass

    @abc.abstractmethod
    def create_graphic_card(self):
        pass


class SamsungComputerFactory(Factory):

    def create_cpu(self):
        return SamsungCPU()

    def create_memory(self):
        return SamsungMemory()

    def create_mainboard(self):
        return SamsungMainBoard()

    def create_case(self):
        return SamsungCase()

    def create_hard_disk(self):
        return SamsungHardDisk()

    def create_power(self):
        return SamsungPower()

    def create_graphic_card(self):
        return SamsungGraphicCard()


class LGComputerFactory(Factory):

    def create_cpu(self):
        return LGCPU()

    def create_memory(self):
        return LGMemory()

    def create_mainboard(self):
        return LGMainBoard()

    def create_case(self):
        return LGCase()

    def create_hard_disk(self):
        return LGHardDisk()

    def create_power(self):
        return LGPower()

    def create_graphic_card(self):
        return LGGraphicCard()


if __name__ == "__main__":
    vendor = VENDOR.LG

    if vendor == VENDOR.SAMSUNG:
        factory = SamsungComputerFactory()
    elif vendor == VENDOR.LG:
        factory = LGComputerFactory()

    computer = Computer()
    cpu1 = factory.create_cpu()
    cpu2 = factory.create_cpu()
    cpu3 = factory.create_cpu()
    cpu4 = factory.create_cpu()
    memory = factory.create_memory()
    main_board = factory.create_mainboard()
    power = factory.create_power()
    case = factory.create_case()
    hard_disk = factory.create_hard_disk()

    computer.append_cpu(cpu1)
    computer.append_cpu(cpu2)
    computer.append_cpu(cpu3)
    computer.append_cpu(cpu4)
    computer.memory = memory
    computer.main_board = main_board
    computer.power = power
    computer.case = case
    computer.hard_disk = hard_disk

    print(computer.cpu)
    print(computer.memory)
    print(computer.main_board)
    print(computer.power)
    print(computer.case)
    print(computer.hard_disk)
