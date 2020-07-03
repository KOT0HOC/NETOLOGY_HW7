from pprint import pprint

cook_dict = {}
with open('recipes.txt', encoding='utf8') as file_work:
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
        cook_dict[dish_name] = list_of_ingridient  # записываем в словарь cook_dict наш рецепт
        file_work.readline()
pprint(cook_dict)
