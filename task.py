class Insect:
    """Документация на класс. Класс описывает сферическое насекомое в вакууме."""
    def __init__(self, name: str, number_of_legs: int):
        """Инициализация экземпляра класса.

        :param name: Название насекомого.
        :param number_of_legs: Количество ног насекомого.
        Методы сделаны непубличными, поскольку предназначены для использования только внутри класса."""
        self._name = name
        self._number_of_legs = number_of_legs
        
    @property
    def name(self) -> str:
        """Метод возвращает название насекомого."""
        return self._name
        
    @property
    def number_of_legs(self) -> int:
        """Метод возвращает количество ног насекомого."""
        return self._number_of_legs
        
    @property
    def sound(self) -> str:
        """Метод возвращает звук насекомого, по умолчанию звуков не издаёт."""
        return "..."
    # магические методы
    def __str__(self) -> str:
        return f"the insect is {self.name}, it has an ungodly amount of legs: {self.number_of_legs}"
    def __repr__(self) -> str:
        return f"insect(name={self.name!r}, number_of_legs={self.number_of_legs!r})"


class Mosquito(insect):
    """Класс, представляющий комара"""
    def __init__(self, species: str):
        """Инициализация комара определённого вида

        :param species: Вид насекомого.
        Метод сделан непубличным, поскольку предназначен для использования только внутри класса."""
        super().__init__("mosquito", 6)
        self._species = species
        
    @property
    def species(self):
        """Метод возвращает вид комара."""
        return self._species
    def sound(self) -> str:
        """Переопределённый метод возвращает писк комара."""
        return "BZZZZ"
    # магические методы
    def __str__(self) -> str:
        return f"this mosquito's species is {self.species}, it has an ungodly amount of legs: {self.number_of_legs}"
    def __repr__(self) -> str:
        return f"mosquito(species={self.species!r})"
