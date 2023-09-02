K, S = map(int, input().split())
#pypy3だと通るがpythonだと通らない
counter = 0

for x in range(S + 1):
    for y in range(S + 1 - x):
        z = S - (x + y)
        if x > K or y > K or z > K:
            continue
        if x + y + z == S:
            counter += 1
print(counter)