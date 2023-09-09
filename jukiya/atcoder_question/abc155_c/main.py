from collections import defaultdict

num = defaultdict(int)
N = int(input())

for i in range(N):
    s = input()
    num[s] += 1
sorted_data = sorted(num.items(), key=lambda x: (-x[1], x[0]))
max_num = sorted_data[0][1]
for word, count in sorted_data:
    if count < max_num:
        break
    print(word)
