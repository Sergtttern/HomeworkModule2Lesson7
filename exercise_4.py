"""
Модуль 2 Python Advanced, Урок №7. Рекурсія та метакласи, Вправа 4

Задача 4: Контроль створення класу

Створіть метаклас, який викидає помилку при спробі створити клас з атрибутами, що починаються
з '__' (два нижніх підкреслення)
(приклад виводу у теорії)

Задача 4. Контроль створення класу
Опис завдання: Створіть метаклас, який викидає помилку при спробі створити
клас з атрибутами, що починаються з '__' (два нижніх підкреслення).
Приклад виводу:
class MyPrivateClass(metaclass=NoDunderAttributes):
__secret_attribute = 10 # Raises error: 'Cannot have attribute names starting with "__"'
"""


class NoDunderAttributes(type):
    """
    метаклас, який викидає помилку при спробі створити клас з атрибутами, що починаються
    з '__' (два нижніх підкреслення)
    """
    def __new__(cls, name, bases, attrs):
        for attr_name in attrs:
            if attr_name != '__module__' and attr_name != '__qualname__':
                attr_name = attr_name.replace(f'_{name}', '')

            if attr_name.startswith('__') and attr_name != '__module__' and attr_name != '__qualname__':
                raise TypeError("Cannot have attribute names starting with '__'")
        super().__new__(cls, name, bases, attrs)


class MyPrivateClass(metaclass=NoDunderAttributes):
    __secret_attribute = 10
