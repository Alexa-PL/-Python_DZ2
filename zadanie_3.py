number = int(input("Введите номер месяца: "))
if number <= 12 and number >= 1:
    month_dict = {1: 'Январь',
                  2: 'Февраль',
                  3: 'Март',
                  4: 'Апрель',
                  5: 'Май',
                  6: 'Июнь',
                  7: 'Июль',
                  8: 'Август',
                  9: 'Сентяборь',
                  10: 'Октяборь',
                  11: 'Нояборь',
                  12: 'Декаборь'}
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == number-1:
            print(f"Месяц из списка {month_list[i]}")
            break
    print(f"Месяц из списка dict {month_dict[number]}")
else:
    print("Вы сделали ошибку!")