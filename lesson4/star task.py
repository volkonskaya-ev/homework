# Задача со ЗВЁЗДОЧКОЙ. Решать НЕ обязательно.
# Программа получает на вход натуральное число num.
# Программа должна вывести другое натуральное число, удовлетворяющее условиям:
# Новое число должно отличаться от данного ровно одной цифрой
# Новое число должно столько же знаков как исходное
# Новое число должно делиться на 3
# Новое число должно быть максимально возможным из всех таких чисел
# Например (Ввод --> Вывод) :
#
# 379 --> 879
# 15 --> 75
# 4974 --> 7974

def max_division_by_3(num):
    # Здесь нужно написать код
    schetchik_razryadov = 1
    while num // 10**schetchik_razryadov > 0:
        schetchik_razryadov = schetchik_razryadov + 1
    new_num = num
    while schetchik_razryadov > 0:
        new_num = num // 10**schetchik_razryadov * 10**schetchik_razryadov + \
                  num % 10**(schetchik_razryadov - 1) + \
                  9 * 10 ** (schetchik_razryadov - 1)
        while (new_num % 3 != 0) and new_num > num:
            new_num = new_num - 10 ** (schetchik_razryadov - 1)
        if new_num > num:
            break
        schetchik_razryadov = schetchik_razryadov - 1
    return new_num

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    379, 810, 981, 4974, 996, 9000, 15, 0, 9881, 9984, 9876543210, 98795432109879543210
]

test_data = [
    879, 870, 987, 7974, 999, 9900, 75, 9, 9981, 9987, 9879543210, 98798432109879543210
]


for i, d in enumerate(data):
    assert max_division_by_3(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
