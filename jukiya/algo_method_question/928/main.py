"""
https://algo-method.com/tasks/928

### 問題文
カメのアルルは今日 $N$ 個の授業を受けようとしています。
現在は時刻 $0$ で、授業 $i$ は時刻 $L_i$ に始まり、時刻 $R_i$ に終わります。
授業間の移動時間は $0$ であるとして良いですが、授業に遅れて入室することや、早めに退出することはできません。
アルルは $N$ 個の授業すべてを受けられるでしょうか。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$L_0$ $R_0$
$L_1$ $R_1$
$\vdots$
$L_{N-1}$ $R_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 ${10}^5$ 以下の整数
- $L_i, R_i$ は $1$ 以上 ${10}^9$ 以下の整数 $(0 \leq i \leq N-1)$
- $L_i \le R_i$ $(0 \leq i \leq N-1)$
### 出力
答えを出力してください。
アルルが $N$ 個の授業全てを受けられるなら `Yes` を、そうでないなら `No` を出力してください。
"""

N = int(input())
pair = [tuple(map(int, input().split())) for _ in range(N)]

pair.sort()

flag = True

for num_i in range(1, N):
    last_tuple = pair[num_i - 1]
    current_tuple = pair[num_i]
    if last_tuple[1] > current_tuple[0]:
        flag = False
        break
if flag:
    print("Yes")
else:
    print("No")