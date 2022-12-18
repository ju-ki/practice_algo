"""
https://algo-method.com/tasks/360

### 問題文
$50$ 円玉, $10$円玉, $5$ 円玉, $1$円玉がそれぞれ $A_0$, $A_1$, $A_2$, $A_3$ 枚あります。
これらを用いて $X$ 円を支払うとき、最小で何枚の硬貨が必要ですか。
ただし、支払い方は少なくとも $1$ つ存在することが保証されています。
### 入力
入力は次の形式から与えられます。
```IOExample
$X$
$A_0$ $A_1$ $A_2$ $A_3$
```
また、入力される値は次の制約を満たします。
- $X$ は $1$ 以上 $1000$ 以下の整数
- $A_0, A_1, A_2, A_3$ は $1$ 以上 $100$ 以下の整数
### 出力
答えを出力してください。
"""

X = int(input())
A = list(map(int, input().split()))
coins = [50, 10, 5, 1]
ans = 0

for num_i in range(4):
    add = X // coins[num_i]
    add = min(add, A[num_i])
    X -= coins[num_i] * add
    ans += add
print(ans)