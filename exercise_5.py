"""
Модуль 2 Python Advanced, Урок №7. Рекурсія та метакласи, Вправа 5

Задача 5: Назви класів у CamelCase

Створіть метаклас, який переконується, що назва класу задана у форматі CamelCase.
 Перевірки на те що перший символ заглавний вистачить.
(приклад виводу у теорії)

Задача 5. Назви класів у CamelCase
Опис завдання: Створіть метаклас, який переконується, що назва класу задана у
форматі CamelCase. Перевірки на те що перший символ заглавний вистачить.
Приклад виводу:
class notCamelCase(metaclass=CamelCase):
pass # Raises error: 'Class name not in CamelCase'
"""


class CamelCase(type):
    """
    метаклас, який переконується, що назва класу задана у форматі CamelCase.перевірка лише першої літери)
    """
    def __new__(cls, name, bases, attrs):
        print(name)
        if name[0].islower():
            raise TypeError("Class name not in CamelCase")
        super().__new__(cls, name, bases, attrs)


class notCamelCase(metaclass=CamelCase):
    pass
