"""
https://algo-method.com/tasks/367

### 問題文
アルルは今年銀行に $N$ 円を預けています。
銀行に預けたお金は、利子がついて $1$ 年ごとに $X$ 倍になります。利子がついたあとの金額は整数でない可能性もあります。
アルルは**今年も含めて $1$ 年ごとに**、追加で $1$ 円ずつ預けます。
預金額が $5$ 年後に $M$ 円になるような $X$ を求めて出力してください。
なお、アルルは $5$ 年後にも $1$ 円を預けるものとします。
また、出力値の絶対誤差 (想定解と出力の差の絶対値) は $0.01$ まで許されます。
### 入力
入力は次の形式から与えられます。
```IOExample
$N M$
```
また、入力される値は次の制約を満たします。
- $N$ は $0$ 以上 $10000$ 以下の整数
- $M$ は $N+6$ 以上 $100000$ 以下の整数
### 出力
答えを出力してください。絶対誤差は $0.01$ まで許されます。
"""

N, M = map(int, input().split())


def calculate(x:int, n: int) -> float:
    ans = n + 1
    for _ in range(5):
        ans = 1 + ans * x
    return ans


left, right = 0, 100

while (right - left > 1e-4):
    mid = (right + left) / 2
    if (calculate(x=mid, n=N) < M):
        left = mid
    else:
        right = mid

answer = left
print(answer)