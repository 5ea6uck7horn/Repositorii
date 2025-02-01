from task_1 import Beetle, Car_headlights, Soda # Импортируем классы

if __name__ == "__main__":
    # Инстанцирование
    beetle = Beetle("Майский жук", 2.0)
    car_headlights = Car_headlights(5, 2)
    soda = Soda("Лимон", 500)

    # Проверка Beetle.init
    try:
        beetle_error = Beetle("", 2.0)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        beetle_error = Beetle("Майский жук", -2.0)
    except ValueError:
        print('Ошибка: неправильные данные')

    # Проверка Car_headlights.init
    try:
        car_headlights_error = Car_headlights(11, 2)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        car_headlights_error = Car_headlights(5, 0)
    except ValueError:
         print('Ошибка: неправильные данные')

    # Проверка Car_headlights.turn_on
    try:
        car_headlights.turn_on("2")
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        car_headlights.turn_on(-2)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        car_headlights.turn_on(7)
    except ValueError:
        print('Ошибка: неправильные данные')

    # Проверка Soda.drink
    try:
        soda.drink(600)
    except ValueError:
        print('Ошибка: неправильные данные')
