# TODO Напишите функцию find_common_participants

def find_common_participants(group1: str, group2: str, sep=','):
    parts_first_group = group1.split(sep)
    parts_second_group = group2.split(sep)
    common = set(parts_first_group).intersection(set(parts_second_group))
    return sorted(list(common))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

find_common_participants(participants_first_group, participants_second_group, sep='|')
