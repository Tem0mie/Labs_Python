import doctest


class TShirt:
    def __init__(self, size: str, material: str, colour: str):
        """
        Создание и подготовка к работе объекта "Футболка"

        :param size: Размер футболки
        :param material: Материал футболки
        :param colour: Цвет футболки

        Примеры:
        >>> tshirt = TShirt("M", "Шёлк", "Белый") # инициализация экземпляра класса
        """
        if not isinstance(size, str):
            raise TypeError("Размер нужно указать буквой (S, M, L и т.д.)")
        self.size = size
        self.material = material
        self.colour = colour

    def changesize(self, size: str) -> None:
        """
        Функция которая позволяет изменить размер футболки

        :param size: Размер футболки
        :return: Новый размер футболки

        Примеры:
        >>> tshirt = TShirt("M", "Шёлк", "Белый")
        >>> tshirt.changesize("L")
        """
        if not isinstance(size, str):
            raise TypeError("Размер нужно указать буквой (S, M, L и т.д.)")
        ...

    def changematerial(self, material: str) -> None:
        """
        Функция которая позволяет изменить материал футболки

        :param material: Материал футболки
        :return: Новый материал

        Примеры:
        >>> tshirt = TShirt("M", "Шёлк", "Белый")
        >>> tshirt.changematerial("Хлопок")
        """
        ...

    def changecolour(self, colour: str) -> None:
        """
        Функция которая позволяет изменить цвет футболки

        :param colour: Цвет футболки
        :return: Новый цвет

        Примеры:
        >>> tshirt = TShirt("M", "Шёлк", "Белый")
        >>> tshirt.changecolour("Жёлтый")
        """
        ...

    if __name__ == "__main__":
        doctest.testmod()



class Smartphone:
    def __init__(self, coast: float, memory: float):
        """
        Создание и подготовка к работе объекта "Телефона"

        :param coast: Цена телефона
        :param memory: Накопительная память телефона, GB

        Примеры:
        >>> smartphone = Smartphone(13000, 128) # инициализация экземпеляра класса
        """
        if not isinstance(coast, (int, float)):
            raise TypeError("Цена телефона должна быть типа int или float")
        if coast < 0:
            raise ValueError("Цена телефона должна быть положительным числом")
        self.coast = coast

        if not isinstance(memory, (int, float)):
            raise TypeError("Память телефона должна быть типа int или float")
        if memory < 0:
            raise ValueError("Память телефона должна содержать положительное число")
        self.memory = memory

    def raise_coast(self, coast: float) -> None:
        """
        Функция которая увеличивает цену телефона

        :param coast: Цена телефона
        :return: Новая цена

        Примеры:
        >>> smartphone = Smartphone(13000, 128)
        >>> smartphone.raise_coast(25000)
        """
        if not isinstance(coast, (int, float)):
            raise TypeError("Цена телефона должна быть типа int или float")
        if coast < 0:
            raise ValueError("Цена телефона должна быть положительным числом")
        ...

    def change_memory(self, memory: float) -> None:
        """
        Функция которая изменяет память телефона

        :param memory: Память телефона
        :return: Новая память

        Примеры:
        >>> smartphone = Smartphone(13000, 128)
        >>> smartphone.change_memory(64)
        """
        if not isinstance(memory, (int, float)):
            raise TypeError("Память телефона должна быть типа int или float")
        if memory < 0:
            raise ValueError("Память телефона должна содержать положительное число")
        ...

    if __name__ == "__main__":
        doctest.testmod()



class Box:
    def __init__(self, size: str, items: float):
        """
        Создание и подготовка к работе объекта "Коробка"

        :param size: Размер коробки
        :param items: Количество предметов в коробке

        Примеры:
        >>> box = Box("Большая", 5) # инициализация экземпляра класса
        """
        if not isinstance(size, str):
            raise TypeError("Размер коробки должен быть типа str")
        self.size = size

        if not isinstance(items, (int, float)):
            raise TypeError("Количество предметов в коробке должно быть типа int или float")
        if items < 0:
            raise ValueError("Количество предметов в коробке должно быть положительным")
        self.items = items

    def change_size(self, size: str) -> None:
        """
        Функция которая изменяет размер коробки

        :param size: Размер коробки
        :return: Новый размер

        Примеры:
        >>> box = Box("Большая", 5)
        >>> box.change_size("Маленькая")
        """
        if not isinstance(size, str):
            raise TypeError("Размер коробки должен быть типа str")
        ...

    def is_empty(self, items: float) -> bool:
        """
        Функция которая проверяет пустая ли коробка

        :param items: Количество предметов в коробке
        :return: Является ли коробка пуста

        Примеры:
        >>> box = Box("Большая", 5)
        >>> box.is_empty()
        """
        if not isinstance(items, (int, float)):
            raise TypeError("Количество предметов в коробке должно быть типа int или float")
        if items < 0:
            raise ValueError("Количество предметов в коробке должно быть положительным")
        self.items = items
        ...

    if __name__ == "__main__":
        doctest.testmod()