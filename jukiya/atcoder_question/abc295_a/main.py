N = int(input())
W = map(str, input().split())

target = {"and", "not", "that", "the", "you"}
flag = False
for w in W:
    if w in target:
        flag = True
        break
print("Yes") if flag else print("No")