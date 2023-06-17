A, B = map(int, input().split())
A_list = [A + B, A - B, A * B]
print(max(A_list))