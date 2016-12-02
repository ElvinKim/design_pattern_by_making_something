import abc


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


class DualCoreComputerDirector:

    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        self._builder.set_cpu()
        self._builder.set_cpu()
        self._builder.set_main_board()
        self._builder.set_power()
        self._builder.set_memory()
        self._builder.set_hard_disk()
        self._builder.set_case()


class QuadCoreComputerDirector:

    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        self._builder.set_cpu()
        self._builder.set_cpu()
        self._builder.set_cpu()
        self._builder.set_cpu()
        self._builder.set_main_board()
        self._builder.set_power()
        self._builder.set_memory()
        self._builder.set_hard_disk()
        self._builder.set_case()


class Builder(abc.ABC):
    @abc.abstractmethod
    def set_cpu(self):
        pass

    @abc.abstractmethod
    def set_memory(self):
        pass

    @abc.abstractmethod
    def set_main_board(self):
        pass

    @abc.abstractmethod
    def set_hard_disk(self):
        pass

    @abc.abstractmethod
    def set_power(self):
        pass

    @abc.abstractmethod
    def set_case(self):
        pass


class SamsungBuilder(Builder):

    def __init__(self):
        self._computer = Computer()

    def set_cpu(self):
        self._computer.append_cpu(SamsungCPU())

    def set_memory(self):
        self._computer.memory = SamsungMemory()

    def set_main_board(self):
        self._computer.main_board = SamsungMainBoard()

    def set_hard_disk(self):
        self._computer.hard_disk = SamsungHardDisk()

    def set_power(self):
        self._computer.power = SamsungPower()

    def set_case(self):
        self._computer.case = SamsungCase()

    def get_computer(self):
        return self._computer


class LGBuilder(Builder):

    def __init__(self):
        self._computer = Computer()

    def set_cpu(self):
        self._computer.append_cpu(LGCPU())

    def set_memory(self):
        self._computer.memory = LGMemory()

    def set_main_board(self):
        self._computer.main_board = LGMainBoard()

    def set_hard_disk(self):
        self._computer.hard_disk = LGHardDisk()

    def set_power(self):
        self._computer.power = LGPower()

    def set_case(self):
        self._computer.case = LGCase()

    def get_computer(self):
        return self._computer


if __name__ == "__main__":
    samsung_computer_builder = SamsungBuilder()
    lg_computer_builder = LGBuilder()

    dual_core_computer_director = DualCoreComputerDirector(samsung_computer_builder)
    dual_core_computer_director.construct()

    quad_core_computer_director = QuadCoreComputerDirector(lg_computer_builder)
    quad_core_computer_director.construct()

    samsung_computer = samsung_computer_builder.get_computer()
    lg_computer = lg_computer_builder.get_computer()

    print(samsung_computer.cpu)
    print(lg_computer.cpu)
