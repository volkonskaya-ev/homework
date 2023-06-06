# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код

with open('test_file/task_3.txt') as task_3:
    list_price = task_3.read().split('\n')
    sum_price = 0
    list_sum_price = []
    for item in list_price:
        if item != '':
            sum_price = sum_price + int(item)
        else:
            list_sum_price.append(sum_price)
            sum_price = 0
list_sum_price.sort()
three_most_expensive_purchases = sum(list_sum_price[-3:])