# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, splitter=','):
    common = list(set(first_group.split(splitter)).intersection(second_group.split(splitter)))
    common.sort()
    return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))