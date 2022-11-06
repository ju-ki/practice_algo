"""
https://algo-method.com/tasks/1027

### 問題文
ある路線には $N$ 個の駅があります。
すべての駅は一直線に並んでおり、始点から順に $0$ から $N-1$ までの番号が振られています。
また、駅 $i$ から 駅 $i+1$ までの距離は $d_i$ であることがわかっています $(0 \leq i \leq N-2)$。
次の $Q$ 個の質問に答えてください。
```Statement
各質問では、$2$ つの駅 $l, r$ ($l \lt r$) が指定されます。
駅 $l$ から駅 $r$ までの距離を求めてください。
```
### 入力
入力は次の形式で与えられます。ただし、$l_i, r_i$ は $i$ 回目の質問内容を表します。
```IOExample
$N$
$d_0 d_1 \ldots d_{N-2}$
$Q$
$l_0 r_0$
$l_1 r_1$
$\vdots$
$l_{Q-1} r_{Q-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $2$ 以上 $10^5$ 以下の整数
- $d_i$ は $1$ 以上 $100$ 以下の整数 $(0 \leq i \leq N-2)$
- $Q$ は $1$ 以上 $10^5$ 以下の整数
- $l_i, r_i$ は $0$ 以上 $N-1$ 以下の整数 $(0 \leq i \leq Q-1)$
- $l_i \lt r_i$ $(0 \leq i \leq Q-1)$
### 出力
答えを $Q$ 行で出力してください。
$i$ 行目には、 $i$ 番目の質問の答えを出力してください。
"""

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
acc_list = [0] * (N+1)

for idx, val in enumerate(A):
    acc_list[idx+1] = acc_list[idx] + val

for _ in range(Q):
    l, r = map(int, input().split())
    Sl = acc_list[l]
    Sr = acc_list[r]
    print(Sr - Sl)