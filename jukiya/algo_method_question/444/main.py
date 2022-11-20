"""
https://algo-method.com/tasks/444

### 問題文
マージソートは、与えられたいくつかの要素を、
所定の順序にしたがって並び替えるソートアルゴリズムです。
マージソートには次の特徴があります (要素の個数を $N$ とします)。
- 部分問題を再帰的に解くアルゴリズムである (分割統治法)
- 等しい順序の要素は順序関係が保存される (安定ソート)
- 最良、最悪、平均計算量はすべて $O(N \log N)$
以下に示すアルゴリズムは、
サイズ $N$ の配列 $A$ を昇順に並び替えるマージソートの動作を表したものです。
----
配列を左右に分割してソートを行う。
$X = \lfloor \frac{N}{2} \rfloor$ とおく。
1. $A[0], A[1], \cdots, A[X-1]$ をこの順に配列 $L$ に格納する。
2. $A[X], A[X+1], \cdots, A[N-1]$ をこの順に配列 $R$ に格納する。
2. $L, R$ を再帰的にソートする。要素数が $1$ 以下の場合は何も行わない。
3. $R$ を逆順に並び替え、 $L$ の最後尾に結合する。
4. 空配列 $B$ を用意し、 $L$ が空になるまで以下を繰り返し行う。
   1. $L$ の先頭の要素を $e_{first}$ 、末尾の要素を $e_{last}$ おく。
   2. $e_{first} \leq e_{last}$ ならば $e_{first}$ の値を $B$ の末尾に追加し、 $e_{first}$ を削除する。
   2. $e_{first} \gt e_{last}$ ならば $e_{last}$ の値を $B$ の末尾に追加し、 $e_{last}$ を削除する。
5. 配列 $B$ の値を出力する。
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
N = int(input())
A = list(map(int, input().split()))


def merge_sort(V):
    X = len(V) // 2
    L, R = [], []
    for num_i in range(len(V)):
        if num_i < X:
            L.append(V[num_i])
        else:
            R.append(V[num_i])
    if len(L) > 1:
        L = merge_sort(L)
    if len(R) > 1:
        R = merge_sort(R)
    R = [r for r in reversed(R)]
    L.extend(R)
    B = []
    while len(L) != 0:
        if L[0] < L[-1]:
            B.append(L[0])
            L.pop(0)
        else:
            B.append(L[-1])
            L.pop()
    return B

A = merge_sort(A)
print(*A)