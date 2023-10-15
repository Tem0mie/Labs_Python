list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

index = len(list_players) // 2

first_team = list_players[:index]
second_team = list_players[index:]

print(first_team)
print(second_team)
