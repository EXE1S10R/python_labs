string = input()
first_index = min([i for i in range(len(string)) if string[i] == string[i].upper() and string[i].isalpha()])
second_index = min([i for i in range(1, len(string)) if string[i-1].isdigit() and string[i].isalpha() and i > first_index])
step = second_index - first_index

print(''.join([string[i] for i in range(first_index, len(string), step)]).split('.')[0])
