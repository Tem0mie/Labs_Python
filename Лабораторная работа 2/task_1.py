money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month = 0
while money_capital >= 0:
    money_capital -= (spend +(spend * increase)) - salary
    month += 1
    spend += spend * increase
print("Количество месяцев, которое можно протянуть без долгов:", month)
