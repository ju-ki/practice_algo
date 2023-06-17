N, A, B = map(int, input().split())


# あまりに注目
def calc_sum_digits(n):
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10
        n //= 10
    return sum_digits


total = 0

for i in range(1, N + 1):
    if A <= calc_sum_digits(i) <= B:
        total += i

print(total)