"""
Модуль 2 Python Advanced, Урок №7. Рекурсія та метакласи, Вправа 6


Задача 6: Підрахунок глибини вкладених списків

Напишіть рекурсивну функцію, яка підраховує глибину вкладеності списків.

(приклад виводу у теорії)

Задача 6. Підрахунок глибини вкладених списків
Опис завдання: Напишіть рекурсивну функцію, яка підраховує глибину
вкладеності списків.
Приклад виводу:
print(depth([1, [2, [3, [4, [5]]]]])) # 5
"""


def depth(nested_lists: list):
    """
    рекурсивна функція, яка підраховує глибину вкладеності списків.
    :param nested_lists:
    :return: int
    """
    str_param = str(nested_lists)
    if '[' not in str_param:
        return 0
    else:
        index = str_param.find('[')
        if index != -1:
            str_param = str_param[:index] + str_param[index + 1:]

        s = depth(str_param) + 1
        return s


print(depth([1, [2, [3, [4, [5]]]]]))
