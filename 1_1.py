import doctest

class Beetle:
    """
    Класс, описывающий жука.

    :param species (str): Вид жука.
    :param size (float): Размер жука в сантиметрах.

    Примеры:
    >>> beetle = Beetle("Хлебный жук", 1.5)
    """
    def __init__(self, species: str, size: float):
        if not species or not isinstance(species, str):
            raise ValueError("Вид жука должен быть непустой строкой")
        if size <= 0:
            raise ValueError("Жучий размер должен быть положительным числом")

        self.species = species
        self.size = size

    def crawl(self) -> str:
        """Оповещение о движении жука.
        :return: Сообщение о движении жука.

        Примеры:
        >>> beetle = Beetle("Долгоносик", 2.5)
        >>> beetle.crawl()
        'Долгоносик ползёт!'
        """
        return f'{self.species} ползёт!'

    def eat(self, food: str) -> str:
        """Оповещение о поедании жуком пищи.
        :return: Сообщение о питании жука.

        Примеры:
        >>> beetle = Beetle("Жужелица", 4.0)
        >>> beetle.eat("гусеницу")
        'Жужелица ест гусеницу.'
        """
        return f'{self.species} ест {food}.'

class Car_headlights:
    """
    Класс, описывающий автомобильные фары.

    :param glow_intensity (int): Интенсивность свечения (1–10).
    :param num_of_headlights (int): Количество горящих фар (1-8).

    Примеры:
    >>> car_headlights = Car_headlights(8, 2)
    """
    def __init__(self, glow_intensity: int, num_of_headlights: int):
        if not (1 <= glow_intensity <= 10) or not isinstance(glow_intensity, int):
            raise ValueError("Интенсивность свечения должна быть целым числом в диапазоне 1–10")
        if not (1 <= num_of_headlights <= 8) or not isinstance(num_of_headlights, int):
            raise ValueError("Количество горящих фар должно быть целым числом в диапазоне 1–8")

        self.glow_intensity = glow_intensity
        self.num_of_headlights = num_of_headlights

    def are_glowing(self) -> bool:
        """Проверка того, включены ли фары.
        :return: светятся ли фары.

        Примеры:
        >>> car_headlights = Car_headlights(8, 2)
        >>> car_headlights.are_glowing()
        True
        """
        return self.num_of_headlights > 0

    def turn_on(self, headlights: int) -> None:
        """Включение дополнительных фар.
        :param headlights: Количество включаемых фар.

        Примеры:
        >>> car_headlights = Car_headlights(8, 2)
        >>> car_headlights.turn_on(2)
        >>> car_headlights.num_of_headlights
        4
        """
        if not isinstance(headlights, int):
            raise TypeError("Количество включаемых фар должно быть типа int")
        if headlights < 0:
            raise ValueError("Количество включаемых фар должно быть положительным числом")
        if headlights > (8 - self.num_of_headlights):
            raise ValueError("Нельзя включить больше фар, чем есть на машине")
        self.num_of_headlights += headlights

class Soda:
    """Класс, описывающий содовые.

    :param taste (str): Вкус содовой.
    :param amount (float): Объём содовой в банке, в миллилитрах.

    Примеры:
    >>> soda = Soda("Клубничная", 330)
    """
    def __init__(self, taste: str, amount: float = 330):
        self.taste = taste
        self.amount = amount

    def buy(self) -> str:
        """Уведомление о покупке содовой.
        :return: Сообщение о покупке содовой.

        Примеры:
        >>> soda = Soda("Черника")
        >>> soda.buy()
        'Я купил соду со вкусом Черника, объёмом 330 мл.'
        """
        return f'Я купил соду со вкусом {self.taste}, объёмом {self.amount} мл.'

    def drink(self, estimated_soda: float) -> None:
        """Питьё содовой.
        :param estimated_soda: Объем отпиваемой содовой.

        Примеры:
        >>> soda = Soda("Черника", 250)
        >>> soda.drink(100)
        >>> soda.amount
        150
        """
        if estimated_soda > self.amount:
            raise ValueError("Нельзя выпить больше, чем есть в банке.")
        self.amount -= estimated_soda

if __name__ == "__main__":
    doctest.testmod()

