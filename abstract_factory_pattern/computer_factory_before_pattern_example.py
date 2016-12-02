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


def create_cpu(vendor):
    if vendor == VENDOR.SAMSUNG:
        return SamsungCPU()
    elif vendor == VENDOR.LG:
        return LGCPU()


def create_memory(vendor):
    if vendor == VENDOR.SAMSUNG:
        return SamsungMemory()
    elif vendor == VENDOR.LG:
        return LGMemory()


def create_mainboard(vendor):
    if vendor == VENDOR.SAMSUNG:
        return SamsungMainBoard()
    elif vendor == VENDOR.LG:
        return LGMainBoard()


def create_power(vendor):
    if vendor == VENDOR.SAMSUNG:
        return SamsungPower()
    elif vendor == VENDOR.LG:
        return LGPower()


def create_case(vendor):
    if vendor == VENDOR.SAMSUNG:
        return SamsungCase()
    elif vendor == VENDOR.LG:
        return LGCase()


def create_hard_disk(vendor):
    if vendor == VENDOR.SAMSUNG:
        return SamsungHardDisk()
    elif vendor == VENDOR.LG:
        return LGHardDisk()


if __name__ == "__main__":

    computer = Computer()
    cpu1 = SamsungCPU()
    cpu2 = SamsungCPU()
    cpu3 = SamsungCPU()
    cpu4 = SamsungCPU()
    memory = SamsungMemory()
    main_board = SamsungMainBoard()
    power = SamsungPower()
    case = SamsungCase()
    hard_disk = SamsungHardDisk()

    computer.append_cpu(cpu1)
    computer.append_cpu(cpu2)
    computer.append_cpu(cpu3)
    computer.append_cpu(cpu4)
    computer.memory = memory
    computer.main_board = main_board
    computer.power = power
    computer.case = case
    computer.hard_disk = hard_disk

    """
    만약 LG 컴퓨터로 바꾸라고 하면 위메 모든 코드를 수정해야 한다.
    그래서 다음과 같이 수정했다고 가정해보자.
    """

    computer2 = Computer()
    vendor = VENDOR.SAMSUNG
    cpu1 = create_cpu(vendor)
    cpu2 = create_cpu(vendor)
    cpu3 = create_cpu(vendor)
    cpu4 = create_cpu(vendor)
    memory = create_memory(vendor)
    main_board = create_mainboard(vendor)
    power = create_power(vendor)
    case = create_case(vendor)
    hard_disk = create_hard_disk(vendor)

    computer2.append_cpu(cpu1)
    computer2.append_cpu(cpu2)
    computer2.append_cpu(cpu3)
    computer2.append_cpu(cpu4)
    computer2.memory = memory
    computer2.main_board = main_board
    computer2.power = power
    computer2.case = case
    computer2.hard_disk = hard_disk

    """
    이제 LG 컴퓨터로 바꾸러면 vendor만 바꾸면 된다.
    그런데 Apple 컴퓨터를 생성해야 한다는 오더를 받았다고 하자.
    그러면 create_ 관련 함수들을 모두 수정해야 한다.
    이를 abstract factory pattern 으로 수정해보자.
    """


