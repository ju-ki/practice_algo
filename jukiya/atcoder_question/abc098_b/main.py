N = int(input())
S = list(input())

max_counter = 0
for i in range(1, len(S)):
    a = set(S[0:i])
    b = set(S[i:])

    counter = 0
    for j in a:
        if j in b:
            counter += 1
    max_counter = max(max_counter, counter)
print(max_counter)