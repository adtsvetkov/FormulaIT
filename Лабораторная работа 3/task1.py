# TODO Напишите функцию для поиска индекса товара
def get_index(my_list: list[str], item: str):
    try:
        found_index = my_list.index(item)
    except ValueError:
        found_index = None
    return found_index


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = get_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
