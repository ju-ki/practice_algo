N = int(input())
S = list(input())
flag = True

for i in range(N - 1):
    if S[i] == "M" and S[i + 1] == "M":
        flag = False
        break
    if S[i] == "F" and S[i + 1] == "F":
        flag = False
        break
print("Yes") if flag else print("No")