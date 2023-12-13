users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
d = {'Общее количество': 0, 'Уникальные посещения': 0}
lenght = len(users)
unique = len(set(users))
d['Общее количество'] = lenght
d['Уникальные посещения'] = unique
print(d)
