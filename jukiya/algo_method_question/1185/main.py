"""
https://algo-method.com/tasks/1185

### 問題文
$N$ 進法表記された整数 $S$ が与えられます。
$S$ を $10$ 進法表記に変換して出力するプログラムを作成してください。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$S$
```
また、入力される値は次の制約を満たします。
- $N$ は $2$ 以上 $9$ 以下の整数
- $S$ は $N$ 進法表記された整数
- $S$ の値は $0$ 以上 $10^{18}$ 以下
### 出力
答えを出力してください。
"""

N = int(input())
S = int(input())
answer = 0

for num_i in range(len(str(S))):
    answer += int(str(S)[num_i]) * (N ** (len(str(S)) - num_i - 1))
print(answer)
