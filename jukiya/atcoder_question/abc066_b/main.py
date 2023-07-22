s = list(input())
# ちょっとよくわかってない
for i in range(len(s) - 1):
    s.pop(-1)
    l = len(s)

    if l % 2 == 1:
        continue

    if s[:int(l / 2)] == s[int(l / 2) * -1:]:
        print(l)
        break