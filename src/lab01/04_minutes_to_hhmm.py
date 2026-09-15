minutes = int(input('Минуты: '))

print(f'{(minutes//60)%24}:{minutes%60:02d}')