N = int(input())
D = [int(input()) for _ in range(N)]
D = list(set(D))
counter = 1
bottom = max(D)
D.remove(bottom)
flag = True

while flag and len(D) > 0:
    max_d = max(D)
    if max_d < bottom:
        bottom = max_d
        D.remove(bottom)
        counter += 1
    else:
        flag = False
print(counter)
