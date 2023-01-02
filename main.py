price = 0
tickets = int(input('Введите кол-во билетов: '))
for i in range(tickets):
    i += 1
    age_for_ticket = int(input(f'Введите возраст для {i} билета: '))
    if age_for_ticket < 18:
            print('Билет бесплатный')
    elif 18 <= age_for_ticket < 25:
            price += 990
            print('Стоимость билета - 990 руб.')
    else:
            price += 1390
            print('Стоимость билета - 1390 руб.')

if tickets > 3:
    price = price - ((all_price / 100) * 10)
    print(f'Сумма к оплате - {price} руб. (скидка 10%)!')
else:
    print(f'Сумма к оплате - {price} руб.')