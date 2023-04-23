S = list(input())
S = list(S)
N = len(S)
flag = True

b_list = [i for i, s in enumerate(S) if s == "B"]

if b_list[0] % 2 == b_list[1] % 2:
    flag = False

prev_r = -1
counter_r = 0

for i, s in enumerate(S):
    if s == "R":
        prev_r = i
        counter_r += 1
    if s == "K" and prev_r == -1:
        flag = False
    if s == "K" and counter_r == 2:
        flag = False
print("Yes") if flag else print("No")
