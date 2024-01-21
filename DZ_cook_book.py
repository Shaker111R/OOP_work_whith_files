from pprint import pprint

#Задача №1
def create_cook_book(file_name):
    cook_book = {}

    with open(file_name, 'r', encoding='utf-8') as file:
        while True:
            dish = file.readline().strip()
            if not dish:
                break

            ingr_count = int(file.readline().strip())
            ingredients = []

            for _ in range(ingr_count):
                ingr_info = file.readline().strip().split(' | ')
                ingredient_name = ingr_info[0]
                ingredient_quantity = int(ingr_info[1])
                ingredient_measure = ingr_info[2]

                ingredient = {
                    'ingredient_name': ingredient_name,
                    'quantity': ingredient_quantity,
                    'measure': ingredient_measure
                }

                ingredients.append(ingredient)

            cook_book[dish] = ingredients
            file.readline()

    return cook_book

cook_book = create_cook_book('recipes.txt')

# Задача №2

def get_shop_list_by_dishes(dishes, cook_book, person_count):
    ing_dict = {}

    for key in cook_book.keys ():
        for dish in dishes:
            if key == dish:
                for dictionary in cook_book[key]:
                    ing_name = dictionary['ingredient_name']
                    try:
                        ing_dict[ing_name]['quantity'] += (dictionary['quantity'] * person_count)
                    except:
                        ing_dict[ing_name] = {'measure': dictionary['measure'],
                                              'quantity': dictionary['quantity'] * person_count}
    return ing_dict

print('Задача №1:\n')
pprint(create_cook_book('recipes.txt'))
print('\n')

print('Задача №2:\n')
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], create_cook_book('recipes.txt'), 2))
print('\n')