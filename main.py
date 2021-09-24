import os,pprint

file_name = 'recipes.txt'
os_separator = os.path.sep
path_to_file = 'files' + os_separator + file_name

def get_shop_list_by_dishes(dishes, person_count):
    with open(path_to_file, 'r', encoding="utf-8") as document:
        result = {}
        for doc_line in document:
            dish_name = doc_line.strip()
            if dish_name in dishes:        
                amount_ingredients = int(document.readline())
        
                for ingredient in range(amount_ingredients):
                    ingredient_name, quantity, measure = document.readline().split('|')
                    find_ingredient = ingredient_name.strip()

                    if find_ingredient in result:
                        result[find_ingredient]['quantity'] += int(quantity.strip())
                    else:
                        result[find_ingredient] = {'measure': measure.strip(), 'quantity': int(quantity.strip())}

                document.readline()
            
        for key in result.keys():
            result[key]['quantity'] *= int(person_count)

        return result


recipes_book = get_shop_list_by_dishes(['Фахитос', 'Утка по-пекински', 'Омлет'], 3)
pprint.pprint(recipes_book)
