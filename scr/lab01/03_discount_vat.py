price = float(input('Цена товара: ').replace(',', '.'))
discount = float(input('Скидка в %: ').replace(',', '.'))
vat = float(input('ДНС в %: ').replace(',', '.'))

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f'База после скидки: {base:.2f} ₽')
print(f'НДС: {vat_amount:.2f} ₽')
print(f'Итого к оплате: {total:.2f} ₽')
