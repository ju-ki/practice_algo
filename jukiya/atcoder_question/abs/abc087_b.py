A = int(input())
B = int(input())
C = int(input())
X = int(input())
coins = [500, 100, 50]
counter = 0

if X < 500:
    for b in range(B+1):
        for c in range(C+1):
            total = coins[1] * b + coins[2] * c
            if total == X:
                counter += 1
elif X < 100:
    counter += 1
else:
    for a in range(A+1):
        for b in range(B+1):
            for c in range(C+1):
                total = coins[0] * a + coins[1] * b + coins[2] * c
                if total == X:
                    counter += 1

print(counter)
