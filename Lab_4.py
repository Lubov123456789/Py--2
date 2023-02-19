from typing import Union


"""
МАССА ОДНОГО ПАССАЖИРА ТС   
"""
MASS_OF_1_PASSAGER = 70


class Vehicels:
    def __init__(self, mass: Union[int, float], speed: Union[int, float], num_of_passagers: int):
        """
        Инициализируем транспортное средство
        :param mass: подрессоренная масса тс
        :param speed: скорость тс
        :param num_of_passagers: количество пассажиров в тс
        """
        self._speed = speed
        self._num_of_passagers = num_of_passagers
        self._mass = mass


    """
    Все property'ы и setter'ы для инкапсуляции и валидации
    """
    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, new_mass):
        if not isinstance(new_mass, Union[float, int]):
            raise TypeError
        elif 0 > new_mass:
            raise ValueError
        self._mass = new_mass

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed_amount):
        if not isinstance(speed_amount, Union[int, float]):
            raise TypeError
        elif speed_amount < 0:
            raise ValueError

    @property
    def num_of_passagers(self):
        return self._num_of_passagers

    @num_of_passagers.setter
    def num_of_passagers(self, amount):
        if not isinstance(amount, int):
            raise TypeError
        elif 0 > amount:
            raise ValueError

    def __str__(self):
        return f"Скорость {self._speed}." \
               f" Количество пассажиров {self._num_of_passagers}" \
               f"Масса {self._mass}"

    def __repr__(self):
        return f"{self.__class__.__name__}(speed={self._speed!r}," \
               f" num_of_passagers={self._num_of_passagers!r}" \
               f"mass={self._mass!r})"

    def full_mass(self) -> Union[int, float]:
        """
        Нахождение полной массы тс включая пассажиров
        :return:
        """
        self._mass = self._mass + self._num_of_passagers * MASS_OF_1_PASSAGER
        return self._mass


class Car(Vehicels):
    def __init__(self, name: str, engine: str, mass: Union[int, float],
                 speed: Union[int, float], num_of_passagers: int):
        super().__init__(mass, speed, num_of_passagers)
        self._name = name
        self._engine = engine

    # readonly for name and engine
    @property
    def name(self) -> str:
        return self._name

    @property
    def engine(self) -> str:
        return self._engine


    def __repr__(self):
        """
        перегружаем, так как появились новые значения
        
        """
        return f"{self.__class__.__name__}(speed={self._speed!r}," \
               f" num_of_passagers={self._num_of_passagers!r}" \
               f"mass={self._mass!r}" \
               f"name = {self._name!r}" \
               f"engine = {self._engine!r})"

if __name__ == "__main__":
    # Write your solution here
    buggatti = Car('Veiron', 'v16', 1000, 400, 2)
    print(buggatti)
    print(buggatti.full_mass())
    pass
