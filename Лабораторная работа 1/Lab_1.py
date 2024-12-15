# TODO Написать 3 класса с документацией и аннотацией типов


class CupModel: # Модель кружки
    def __init__(self, material: str, volume: int):

        self.material = material # материал кружки
        self.volume = volume # Объем кружки
        self.color = "000000"
        self.drink = None
    def set_color(self) -> None: # Задание цвета кружки
        ...
    def fill_drink(self) -> None: # Задание наполнения кружки
        ...



class Houseplant: # Домашнее растение
    def __init__(self, shade_tolerance: bool, watering_time: str):
        self.shade_tolerance = shade_tolerance # Теневыносливость
        self.watering_time = watering_time # Время пролива
    def change_shade_tolerance(self) -> None: # Изменить параметр теневыносливости
        ...
    def set_watering_time(self) -> None: # Задать время полива
        ...


import doctest
class PillShedule: # Расписание приема таблеток
    def __init__(self, pill_time: str, pills: [str]):
        self.pill_time = pill_time # Время приема таблеток
        self.pills = pills # Список таблеток
    def switch_time(self) -> None: # Сменить время приема
        ...
    def edit_pills(self) -> None: # Изменить лист таблеток
        ...
if __name__ == "__main__":
    doctest.testmod()

