"""
https://algo-method.com/tasks/224

### 問題文
整数 $A$ と $B$ の最大公約数を出力するプログラムを作成してください。
ただし次の条件を満たすとき「 $X$ は $A$ と $B$ の最大公約数である」と言います。
**条件**：$X$ は $A$ も $B$ も割り切る $1$ 以上の整数の中で最大のものである
### 入力
入力は次の形式で与えられます。
```IOExample
$A$ $B$
```
また、入力される値は次の制約を満たします。
- $A, B$ は $1$ 以上 $100$ 以下の整数
### 出力
答えを出力してください。
"""
A, B = map(int, input().split())

ans = 0

for num in range(1, min(A, B) + 1):
    if A % num == 0 and B % num == 0:
        ans = num
print(ans)