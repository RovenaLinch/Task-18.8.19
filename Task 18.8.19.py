sum_tickets = 0
tickets = int(input("Введите количество билетов: "))
for price in range(tickets):
    age = int(input("Введите возраст: "))
    if age < 18:
        sum_tickets += 0
    elif 18 <= age <= 25:
        sum_tickets += 990
    elif age > 25:
        sum_tickets += 1390
if tickets > 3:
    print("Сумма билетов: ", sum_tickets - (sum_tickets / 100) * 10)
else:
    print("Сумма билетов: ", sum_tickets)
