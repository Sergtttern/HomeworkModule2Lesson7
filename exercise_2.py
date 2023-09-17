"""
Модуль 2 Python Advanced, Урок №7. Рекурсія та метакласи, Вправа 2

Задача 2: Запис у журнал при створенні класу

Створіть метаклас, який записує в консоль повідомлення, коли створюється новий клас.
(приклад виводу у теорії)

Задача 2. Запис у журнал при створенні класу
Опис завдання: Створіть метаклас, який записує в консоль повідомлення, коли
створюється новий клас.
Приклад виводу:
class MyClass(metaclass=LoggingMeta):
pass # Prints: 'Class "MyClass" has been created'

"""


class LoggingMeta(type):
    """
    метаклас, який записує в консоль повідомлення, коли створюється новий клас.
    """
    def __new__(cls, *args, **kwargs):
        print('Class "MyClass" has been created')
        return super().__new__(cls, *args, **kwargs)


class MyClass(metaclass=LoggingMeta):
    pass
