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

for dish, ingredients in cook_book.items():
    print(dish)
    for ingredient in ingredients:
        print(ingredient)
    print()