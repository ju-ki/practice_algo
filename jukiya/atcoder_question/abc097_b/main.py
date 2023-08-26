X = int(input())
max_num = 1

for b in range(1, X + 1):
    if b == 1:  # bが1の場合、べき乗は常に1なのでスキップ
        continue

    p = 2
    power = b**p
    while power <= X:
        max_num = max(max_num, power)
        p += 1
        power = b**p

print(max_num)