N = int(input('in_1: '))
data = [list(map(str, input(f'in_{i+2}: ').split())) for i in range(N)]
offline = len([student for student in data if student[-1] == 'True'])
online = N - offline

print(f'out: {offline} {online}')