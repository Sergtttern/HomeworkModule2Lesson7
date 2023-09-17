"""
Модуль 2 Python Advanced, Урок №7. Рекурсія та метакласи, Вправа 3

Задача 3: Реверс рядка

Напишіть рекурсивну функцію, яка перевертає вхідний рядок.
(приклад виводу у теорії)

Задача 3. Реверс рядка
Опис завдання: Напишіть рекурсивну функцію, яка перевертає вхідний рядок.
Приклад виводу:
print(reverse_string("Hello")) # olleH
"""


def reverse_string(str_param):
    """
    рекурсивна функція, яка перевертає вхідний рядок.
    :param str_param:
    :return: str
    """

    if (len(str_param) == 1):
        return str_param[0]
    else:
        s = str_param[len(str_param) - 1] + reverse_string(str_param[:len(str_param) - 1])
        return s


print(reverse_string("Hello"))
