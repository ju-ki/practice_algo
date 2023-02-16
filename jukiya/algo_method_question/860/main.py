"""
https://algo-method.com/tasks/860

### 問題文
$N$ 個の整数 $A_0, A_1, \dots, A_{N-1}$ が与えられます。
これらの整数のうち、最も個数が多いものを答えてください。
複数個ある場合は、そのうち **最小** のものを答えてください。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$A_0 A_1 \ldots A_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $2 \times 10^{5}$ 以下の整数
- $A_i$ は $0$ 以上 $5 \times 10^{5}$ 以下の整数 $(0 \leq i \leq N-1)$
### 出力
答えを出力してください。
"""

N = int(input())
A = list(map(int, input().split()))
max_A = max(A)
count_list = [0] * (max_A + 1)

for a in A:
    count_list[a] += 1

min_mode = count_list.index(max(count_list))
print(min_mode)
