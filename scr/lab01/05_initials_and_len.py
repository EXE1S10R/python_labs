data = input("ФИО: ").split()

print(f"Инициалы: {''.join([i[0].upper() for i in data])}.")
print(f"Длинна (символов): {len(' '.join(data))}")
