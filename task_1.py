class Products :
    """
    Создание и подготовка к работе класса "Продукты"
    
    :param name: Название продукта
    :param storage_life: Срок годности продукта (в днях)
    
    Примеры:
    >>> product = Products("Арбуз", 90) # инициализация экземпляра класса
    """
    def __init__(self, name: str, storage_life: int):
        self._name = name
        self._storage_life = storage_life

    """Создаём управляемый атрибут name"""
    @property
    def name(self):
        return self._name

    """Создаём управляемый атрибут storage_life"""
    @property
    def storage_life(self):
        return self._storage_life

    """Используем магический метод для вывода информации для пользователя"""
    def __str__(self):
        return f"Продукт {self.name}. Срок годности {self.storage_life}}"

    """Используем магический метод для машинно-ориентированного вывода"""
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, storage_life={self.storage_life!r})"


    class Fruits(Products):
        """
        Создание и подготовка к работе дочернего класса "Фрукты"
            
        Параметры

        :param name: Название продукта
        :param storage_life: Срок годности продукта (в днях)
        :param variety: Сорт продукта

        Примеры:
        >>> product = Apple("Яблоко", 30, "Голден") # инициализация экземпляра класса
        """
        def __init__(self, variety: str):
            super().__init__(name, storage_life)

        if not isinstance(variety, str):
            raise TypeError("'variety' должен быть типа string")
        self.variety = variety
        
        """Создаём управляемый атрибут variety"""
        @property
        def variety(self):
            return self.__variety

        @variety.setter
        """Устанавливает сорт фрукта"""
        def change_variety(self, new_variety: str):
            if not isinstance(variety, str):
                raise TypeError("'new_variety' должен быть типа string")
            self.__variety = new_variety

        """Перегрузка метода repr, т.к. добавляется новый параметр variety"""
        def __repr__(self) -> str:
            return f'{self.__class__.__name__}({self.name!r}, {self.storage_life!r}, {self.variety!r} )'

        """Перегрузка метода str, т.к. добавляется новый параметр variety"""
        def __str__(self):
            return f"Продукт {self.name}. Срок годности {self.storage_life}, Сорт {self.variety}"

    class Dairy(Products):
        """
        Создание и подготовка к работе дочернего класса "Молочные продукты"

        Параметры

        :param name: Название продукта
        :param storage_life: Срок годности продукта (в днях)
        :param fat: Содержание жирности в продукте

        Примеры:
        >>> product = Dairy("Молоко", 7, "3%") # инициализация экземпляра класса
        """
        def __init__(self, fat: str):
            super().__init__(name, storage_life)

            if not isinstance(fat, int):
                raise TypeError("'fat' должен быть типа string")
            self.fat = fat

            """Создаём управляемый атрибут fat"""
            @property
            def fat(self):
                return self.__fat

            @fat.setter
            """Устанавливает жирность продукта"""
            def fat(self, new_fat: str):
                if not isinstance(fat, str):
                    raise TypeError("'fat' должен быть типа string")

            self.__fat = new_fat
            
            """Перегрузка метода repr, т.к. добавляется новый параметр fat"""
            def __repr__(self) -> str:
                return f'{self.__class__.__name__}({self.name!r}, {self.storage_life!r}, {self.fat!r} )'

            """Перегрузка метода str, т.к. добавляется новый параметр fat"""
            def __str__(self):
                return f"Продукт {self.name}. Срок годности {self.storage_life}, Содержание жирности {self.fat}"