S = list(input())
T = list(input())
flag = False

for i in range(len(S)):
    t = S.pop(0)
    S.append(t)
    if ''.join(S) == ''.join(T):
        flag = True
        break
print('Yes') if flag else print('No')