"""
https://algo-method.com/tasks/857

### 問題文
$N$ 人の生徒がそれぞれテストで $A_0, A_1, \dots, A_{N-1}$ 点を獲得しました。
なおテストの点数は $0$ 点以上 $100000$ 点以下の整数値です。
この生徒について次の $Q$ 回のクエリが与えられます。
各クエリでは $0$ 以上 $100000$ 以下の整数 $x$ が与えられますので、
$x$ 点を獲得した生徒が何人いたかを答えてください。
### 入力
入力は次の形式で与えられます。$x_i$ は $i$ 番目のクエリを表します。
```IOExample
$N$
$A_0 A_1 \ldots A_{N-1}$
$Q$
$x_0$
$x_1$
$\vdots$
$x_{Q-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $2 \times 10^{5}$ 以下の整数
- $Q$ は $1$ 以上 $10^5$ 以下の整数
- $A_i$ は $0$ 以上 $10^{5}$ 以下の整数 $(0 \leq i \leq N-1)$
- $x_i$ は $0$ 以上 $10^5$ 以下の整数
### 出力
答えを出力してください。
"""

# 流石にTLE
# 予めリストを作っておく
N = int(input())
A = list(map(int, input().split()))
max_A = max(A)

# シンプルパターン(TLE)
# A.sort()
# medium = len(A) // 2
# Q = int(input())
# answer = 0
# for _ in range(Q):
#     x = int(input())
#     if x >= medium:
#         answer = A[medium-1:].count(x)
#     else:
#         answer = A[:medium+1].count(x)
#     print(answer)

group_list = [0] * (max_A + 1)

for a in A:
    group_list[a] += 1

Q = int(input())
answer = 0
for _ in range(Q):
    x = int(input())
    answer = group_list[x]
    print(answer)