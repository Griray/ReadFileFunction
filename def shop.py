cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
}

dishes = ["Омлет"]
person_count = int(input("Сколько человек будет кушать? "))

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    if dish in cook_book:
      for ingredient in cook_book[dish]:
        ingredient_name, quantity, measure = ingredient.values()
        if ingredient_name in shop_list:
          shop_list[ingredient_name]['quantity'] += person_count * quantity
        else:
          shop_list[ingredient_name] = {'quantity': quantity * person_count, 'measure': measure}
  print(shop_list)

get_shop_list_by_dishes(dishes, person_count)
