X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
counter = 0

for num_a in A:
    for num_b in B:
        for num_c in C:
            equation = num_a + num_b
            if equation == num_c:
                counter += 1


print(counter)