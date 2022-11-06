"""
https://algo-method.com/tasks/1029

### 問題文
あなたの手元には $N$ 本のひもがあり、それぞれの長さは $L_0, L_1, \dots, L_{N-1}$ です。
あなたは欲しい長さのひもをすぐに取り出せるように、ひもを長さで検索できるプログラムを作成することにしました。
次の $Q$ 個の質問に答えるプログラムを作成してください。
```Statement
各質問では、見つけたいひもの長さの下限と上限を表す整数 $A, B$ ($A \leq B$) が指定されます。
「長さが $A$ 以上 $B$ 以下であるようなひもの本数」を答えてください。
```
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$L_0 L_1 \ldots L_{N-1}$
$Q$
$A_0 B_0$
$A_1 B_1$
$\vdots$
$A_{Q-1} B_{Q-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $10^{5}$ 以下の整数
- $L_i$ は $1$ 以上 $10^{5}$ 以下の整数 $(0 \leq i \leq N-1)$
- $Q$ は $1$ 以上 $10^{5}$ 以下の整数
- $A_i, B_i$ は $1$ 以上 $10^{5}$ 以下の整数 $(0 \leq i \leq Q-1)$
- $A_i \le B_i$ $(0 \leq i \leq Q-1)$
### 出力
答えを出力してください。
"""

N = int(input())
L = list(map(int, input().split()))
Q = int(input())

string_count_list = [0] * (10**5+1)

for num_l in L:
    string_count_list[num_l] += 1

acc_list = [0] * (10**5+1)

for idx, val in enumerate(string_count_list):
    if idx == 0:
        acc_list[idx] = val
    else:
        acc_list[idx] = acc_list[idx-1] + val
        
for _ in range(Q):
    A, B = map(int, input().split())
    print(acc_list[B] - acc_list[A-1])
