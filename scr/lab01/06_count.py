N = int(input())
data = [list(map(str, input().split())) for i in range(N)]
ofline = len([student for student in data if student[-1] == 'True'])
online = N - ofline

print(ofline, online)