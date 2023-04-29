N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

n, m = 0, 0
counter = 0

n_list, m_list = [], []

for _ in range(N + M):
    if n >= N:
        m += 1
        counter += 1
        m_list.append(counter)
    elif m >= M:
        n += 1
        counter += 1
        n_list.append(counter)

    elif A[n] > B[m]:
        m += 1
        counter += 1
        m_list.append(counter)
    elif B[m] > A[n]:
        n += 1
        counter += 1
        n_list.append(counter)

print(*n_list)
print(*m_list)