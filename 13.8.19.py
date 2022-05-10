tickets = int(input("Введите количество билетов: "))
summa = 0
for ticket in range(tickets):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        continue
    elif 18 >= age < 25:
        summa += 990
    elif age >= 25:
        summa += 1390
if tickets >= 3:
    summa -= (summa / 100 * 10)
print("Сумма к оплате", int(summa), "руб.")
