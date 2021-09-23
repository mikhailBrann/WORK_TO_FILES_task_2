import os,pprint

file_name = 'recipes.txt'
os_separator = os.path.sep
path_to_file = 'files' + os_separator + file_name

def reading_file(read_file):
    with open(read_file, 'r', encoding="utf-8") as document:
        result = {}
        for doc_line in document:
            dish_name = doc_line.strip()
            amount_ingredients = int(document.readline())
            ingredients_list = []

            for ingredient in range(amount_ingredients):
                ingredient_name, quantity, measure = document.readline().split('|')
                ingredients_list.append({'ingredient_name': ingredient_name.strip(), 'quantity': int(quantity.strip()), 'measure': measure.strip()})

            result[dish_name] = ingredients_list
            document.readline()

        return result


recipes_book = reading_file(path_to_file)
pprint.pprint(recipes_book)
