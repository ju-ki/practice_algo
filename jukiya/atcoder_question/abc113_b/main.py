N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

HA = [[i + 1, abs(A - (T - H[i] * 0.006))] for i in range(N)]
HA.sort(key=lambda s: s[1])

print(HA[0][0])