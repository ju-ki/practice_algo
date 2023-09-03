N = int(input())

exist = [0] * N

for i in range(N):
    s = input()
    exist[i] = s

print(len(list(set(exist))))