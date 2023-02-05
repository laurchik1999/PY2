# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union

class Laptop:
    def __init__(self, memory_ram: int, display_size: Union[int, float]):
        if not isinstance(memory_ram, int):
            raise TypeError("Объем памяти должен быть типа int")
        if memory_ram <= 0:
            raise ValueError("Объем памяти должен быть положительным числом")
        self.memory_ram = memory_ram

        if not isinstance(display_size, (int, float)):
            raise TypeError("Размер дисплея должен быть типа int или float")
        if display_size <= 0:
            raise ValueError("Размер дисплея должен быть положительным числом")
        self.display_size = display_size

    def turn_on(self):
        ... #включить ноутбук

    def turn_off(self):
        ... #выключить ноутбук


class Cat:
    def __init__(self, age: int, number_of_beds: int):
        if not isinstance(age, int):
            raise TypeError("Возраст кота должен быть типа int")
        if age <= 0:
            raise ValueError("Возраст кота должен быть положительным числом")
        self.age = age

        if not isinstance(number_of_beds, int):
            raise TypeError("Количество спальных мест должно быть типа int")
        if number_of_beds <= 0:
            raise ValueError("Количество спальных мест должно быть положительным числом")
        self.number_of_beds = number_of_beds

    def looking_for_a_cat(self):
        ... #ищем кота

    def stroking_the_cat(self):
        ... #гладим кота


class Airplane:
    def __init__(self, max_number_of_passengers: int, number_of_passengers: int):
        if not isinstance(max_number_of_passengers, int):
            raise TypeError("Максимальное число пассажиров должно быть типа int")
        if max_number_of_passengers <= 0:
            raise ValueError("Максимальное число пассажиров должно быть положительным числом")
        self.max_number_of_passengers = max_number_of_passengers

        if not isinstance(number_of_passengers, int):
            raise TypeError("Число пассажиров должно быть типа int")
        if number_of_passengers <= 0:
            raise ValueError("Число пассажиров должно быть положительным числом")
        if number_of_passengers > max_number_of_passengers:
            raise ValueError("Число пассажиров не должно быть больше, чем максимальное число пассажиров")
        self.number_of_passengers = number_of_passengers

    def combination_pass(self):
        ... #рассаживаем пассажиров в салоне

    def everything_is_fine(self):
        ... #все пассажиры на своих местах, можно лететь


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    pass
