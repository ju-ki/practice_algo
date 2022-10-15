# N 個の 1 以上 9 以下の整数 A
# 0,A 1,…,A N−1が与えられます。
# N 個の整数の中に一番多く出てくる数字を求めるプログラムを作成してください。 ただし、答えは一つに定まることが保証されているものとします。

N = int(input())
A = list(map(int, input().split()))
count_list = [0] * 10

for num in A:
    if num >= 1 and num <= 9:
        count_list[num-1] += 1
max_idx = count_list.index(max(count_list))
print(max_idx+1)
