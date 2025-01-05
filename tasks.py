from pprint import pprint
import os

def read_cookbook():
    cook_book = {}
    with open('recipes.txt', 'r', encoding='utf-8') as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break
            ingredients_count = int(f.readline().strip())
            ingredients = []
            for _ in range(ingredients_count):
                line = f.readline().strip()
                ingredient_name, quantity, measure = line.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            cook_book[dish_name] = ingredients
            f.readline()
    return cook_book

pprint(read_cookbook())
print()
print()

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_cookbook()
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count

                if name not in shop_list:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
                else:
                    shop_list[name]['quantity'] += quantity
        else:
            print(f"Блюдо '{dish}' не найдено в кулинарной книге")

    return shop_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


def merge_files(folder_path, result_file):
    files_data = []

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.readlines()
                files_data.append((file_name, len(content), content))
    files_data.sort(key=lambda x: x[1])
    with open(result_file, 'w', encoding='utf-8') as result:
        for file_name, line_count, content in files_data:
            result.write(f"Имя файла: {file_name}\n")
            result.write(f"Количество строк: {line_count}\n")
            result.writelines(content)
            result.write("\n")

merge_files('task_3', 'result.txt')