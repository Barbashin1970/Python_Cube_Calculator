# Функция для вычисления периметра куба. ------
def calc_cube_perimeter(side):
    return side * 12


# Функция для вычисления площади куба.
def calc_cube_area(side):
    one_face = side * side
    cube_area = one_face * 6
    return cube_area


# Основная функция, которая принимает длину ребра куба и количество кубиков
def calc_cube(side, amount):
    # Вызываем функцию, рассчитывающую периметр
    # и передаём в неё размер куба side  и количество кубиков - amount
    one_cube_perimeter = calc_cube_perimeter(side)
    full_length = one_cube_perimeter * amount

    # Вызываем функцию, рассчитывающую площадь стекла
    # и передаём в неё размер куба и количество кубиков
    one_cube_area = calc_cube_area(side)
    full_area = one_cube_area * amount

    print('Для', amount, 'кубов понадобится палок (м):', full_length, 'и стекла (кв.м):', full_area)


# В результате остался лишь один вызов "основной" функции,
# а она уже вызовет две вспомогательные
calc_cube(2, 4)
calc_cube(0.5, 26)
calc_cube(0.61, 6)

