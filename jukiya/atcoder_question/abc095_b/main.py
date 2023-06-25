N, X = map(int, input().split())
M = [int(input()) for _ in range(N)]
M.sort()

#総和
counter = len(M)
X -= sum(M)
#最小の値で何回割れるか
counter += X // M[0]

print(counter)
