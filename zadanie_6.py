product = []
while input("Хотите добавить товар? Введите да / нет: ") == 'да':
    number = int(input("Введите номер продукта:"))
    signs = {}
    while input("Хотите добавить параметры продукта? Введите да / нет:") == 'да':
        signs_key = input("Введите продукт: ")
        signs_value: str = input("Введите значение продукта:")
        signs[signs_key] = signs_value
    product.append(tuple([number, signs]))
print(product)
analitics = {}
for good in product:
    for signs_key, signs_value in good[1].items():
        if signs_key in analitics:
            analitics[signs_key].append(signs_value)
        else:
            analitics[signs_key] = [signs_value]
print(analitics)
