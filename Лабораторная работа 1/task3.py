list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
number_players = len(list_players)
middle = number_players // 2
first_team = list_players[:middle]
second_team = list_players[middle]
print(first_team)
print(second_team)
