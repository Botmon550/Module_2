if __name__ == "__main__":
class Animal:
    """
    Документация на класс.
    Класс описывает параметры животного.
    """
    def __init__(self, name: str, specie: str, age: int):
    """
    Параметры:
    name : str - Кличка животного
    specie : str - Вид животного
    age : int - Возраст животного
    """
        self.name = name
        self.species = species
        self.age = age

    def __str__(self) -> str:
        """
        Возвращает строковое представление параметров животоного
        """
        return f"{self.name} ({self.species}), {self.age} лет"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление параметров животного.
        """
        return f"Animal(name={self.name}, species={self.species}, age={self.age})"

    def animal_sound(self) -> str:
        """
        Звук, издаваемый животным.
        Возвращает звук, который издает животное.
        """
        return "Звук"
class Dog(Animal): # Дочерний класс для собак.

    def __init__(self, name: str, age: int, breed: str):
        """
        Параметры:
        name: str - Кличка собаки
        age: int - Возраст собаки
        breed: str - Порода собаки
        """
        super().__init__(name, species="Собака", age=age)
        self.breed = breed

    def __str__(self) -> str:
        """
        Возвращает строковое представление параметров собаки.
        """
        return f"{self.name} ({self.breed}), {self.age} лет"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление параметров солбаки.
        """
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"
    def animal_sound(self) -> str:
        """
        Звук, издаваемый собакой
        Возвращает звук, который издает собака.
        """
        return "Гав"
    def sleep(self, hours: float) -> str:
        """
        Количество часов, которое спит собака
        Возвраащает сообщение о времени сна собаки.
        """
        return f"{self.name} спит {hours} часов."
    pass
