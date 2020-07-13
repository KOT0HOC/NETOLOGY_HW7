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
                # temp_dict = {}
                ingridient = file_work.readline().rstrip().lower()
                component = ingridient.split('|')
                temp_dict = {'ingredient_name': component[0], 'quantity': component[1], 'measure': component[2]}
                list_of_ingridient.append(temp_dict)  # добавляем словарь в список
            cook_book[dish_name] = list_of_ingridient  # записываем в словарь cook_dict наш рецепт
            file_work.readline()
    return cook_book


def get_shop_list_by_dishes(cook_book, dish_name, person_count):
    checklist = {}
    #dish_name = cook_book.keys()
    for dish in dish_name:
        if dish in cook_book:
            ingredients = cook_book[dish]
            #print(ingredients[1])
            for amount in ingredients:
                quantity_count = int(amount['quantity']) * person_count
                print(quantity_count)
                temp_dict = {'quantity': quantity_count}
        cook_book.update(temp_dict)
        #ingredients.update(temp_dict)
        print(temp_dict)
        #checklist[dish_name] = {ingredients:quantity_count}
        #print(checklist)
        #print(cook_book[dish_name][1]['quantity'])
    #print(dish_name)
        print(cook_book[dish])


def main():
    cook_book = create_dict_from_file('recipes.txt')
    result = get_shop_list_by_dishes(cook_book, ['Омлет'], 2)
    print(result)
main()
