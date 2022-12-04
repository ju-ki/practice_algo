"""
https://algo-method.com/tasks/447

### 問題文
バケットソートは、与えられたいくつかの要素を、
所定の順序にしたがって並び替えるソートアルゴリズムです。
バケットソートには次の特徴があります (要素の個数を $N$ 、$A$ の持つ値の種類数を $A_{kind}$ とします)。
- 要素同士の値を比較しないソートである
- 計算量は $O(N + A_{kind})$ である
- $A$ の持つ値の種類数が少なく、値同士の順序関係が既知の場合に有効
以下に示すアルゴリズムは、
サイズ $N$、**要素がすべて $0$ 以上 $\text{X}$ 未満の整数である**配列 $A$ を昇順に並び替えるバケットソートの動作を表したものです。
----
1. 長さ $X$ の配列 $\text{num}$ を用意し、各要素を $0$ で初期化する。
2. $i = 0, 1, \cdots, N-1$ について、$\text{num}[A[i]]$ の値を $1$ 増やす。
   ($\text{num}[i]$ には $A[j] = i$ を満たす整数 $j$ の個数が格納される。)
3. 長さ $X$ の配列 $\text{acc}$ を用意し、各要素を $0$ で初期化する。
4. $i = 0, 1, \cdots, X-1$ について、次のように $\text{acc}[i]$ を更新する。
   ($\text{acc}[i]$ には $A[j] \leq i$ を満たす整数 $j$ の個数が格納される。)
   1. $i = 0$ のとき、 $\text{acc}[i] = \text{num}[i]$
   2. $i \neq 0$ のとき、 $\text{acc}[i] = \text{acc}[i-1] + \text{num}[i]$
5. 長さが $N$ の配列 $B$ を用意する。
6. $i = 0, 1, \cdots, N-1$ について、次のように $B$ を更新する。
   1. $\text{acc}[A[i]]$ の値を $1$ 減らす。
   2. $B[\text{acc}[A[i]]]$ に $A[i]$ の値を代入する。
7. 配列 $B$ の値を返却する。
---
このアルゴリズムを実装し、配列 $A$ をソートした結果を出力してください。
### 入力
入力は次の形式から与えられます。
```IOExample
$N$
$A_0 A_1 \cdots A_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $10^5$ 以下の整数
- $A_i$ は $1$ 以上 $N$ 以下の整数 $(0 \leq i \leq N-1)$
### 出力
答えを $1$ 行で出力してください。
"""


debug = False
if debug:
    N = 5
    A = [2, 1, 3, 4, 1]
else:
    N = int(input())
    A = list(map(int, input().split()))

X = N+1
num = [0] * X


for num_i in range(N):
    num[A[num_i]] += 1

acc = [0] * X

for num_x in range(X):
    if num_x == 0:
        acc[num_x] = num[num_x]
    else:
        acc[num_x] = acc[num_x - 1] + num[num_x]

B = [0] * N

for num_i in range(N):
    acc[A[num_i]] -= 1
    B[acc[A[num_i]]] = A[num_i]

print(*B)

