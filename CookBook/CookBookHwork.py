import os
from pprint import pprint

shop_list_by_dishes = {}
order_list = ['Омлет', 'Фахитос']


# Функция формирования словаря из текстового файла
def create_cookbook(file):
    with open(file, encoding='utf-8') as text:
        cook_book = {}
        for line in text.read().split('\n\n'):
            name, _, *args = line.split('\n')
            new_cook_book = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                new_cook_book.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = new_cook_book
    return cook_book

# Функция создания списка покупок на указанное количество людей
def get_shop_list_by_dishes(dishes, person_count, cook_book):
    for dish in dishes:
        for ingredient in cook_book.get(dish):
            if ingredient.get('ingredient_name') in shop_list_by_dishes.keys():
                added_quantity = {'quantity': ingredient.get('quantity') * person_count +
                                              shop_list_by_dishes[ingredient.get('ingredient_name')]['quantity']}
                shop_list_by_dishes[ingredient.get('ingredient_name')].update(added_quantity)
            else:
                shop_list_by_dishes[ingredient.get('ingredient_name')] = \
                    {'measure': ingredient.get('measure'), 'quantity': ingredient.get('quantity') * person_count}
    return shop_list_by_dishes




pprint(get_shop_list_by_dishes(order_list, int(input('Введите количество персон: ').strip()),\
                               create_cookbook('recipes.txt')))