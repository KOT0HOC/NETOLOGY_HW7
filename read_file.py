from pprint import pprint

def create_dict_from_file(file_name):
    """Функция чтения файла + создание словаря нужного формата"""
    cook_book = {}
    with open(file_name, encoding='utf8') as file_work:
        for line in file_work:
            dish_name = line.rstrip()
            line.lower().strip()
            counter = int(file_work.readline())
            list_of_ingridient = []
            for i in range(counter):
                ingridient = file_work.readline().rstrip().lower()
                component = ingridient.split('|')
                temp_dict = {'ingredient_name': component[0], 'quantity': component[1], 'measure': component[2]}
                list_of_ingridient.append(temp_dict)  # добавляем словарь в список
            cook_book[dish_name] = list_of_ingridient  # записываем в словарь cook_dict наш рецепт
            file_work.readline()
    return cook_book


def get_shop_list_by_dishes(cook_book, dish_name, person_count):
    checklist = {}
    for dish in dish_name:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for amount in ingredients:
                ingredient = amount['ingredient_name']
                quantity_count = int(amount['quantity']) * person_count
                measure = amount['measure']
                if ingredient in checklist:
                    checklist[ingredient]['quantity_count'] += quantity_count
                else:
                    checklist[ingredient] = {
                        'quantity_count': quantity_count,
                        'measure': measure
                    }
    return checklist


def main():
    cook_book = create_dict_from_file('recipes.txt')
    result = get_shop_list_by_dishes(cook_book, ['Запеченный картофель', 'Омлет'], 2)
    pprint(result)


main()
