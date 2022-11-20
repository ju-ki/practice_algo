"""
https://algo-method.com/tasks/443

### 問題文
乱択クイックソートは、与えられたいくつかの要素を、
所定の順序にしたがって並び替えるソートアルゴリズムです。
乱択クイックソートには次の特徴があります (要素の個数を $N$ とします)。
- クイックソートをもとにしたアルゴリズムである
- アルゴリズムの一部に乱数を用いた無作為性を導入している (乱択)
- 最悪期待計算量は $O(N \log N)$ となり、クイックソートの最悪計算量の $O(N^2)$ から改善される
以下に示すアルゴリズムは、
サイズ $N$ の配列 $A$ を昇順に並び替える乱択クイックソートの動作を表したものです。
----
**$0$ 以上 $N-1$ 以下の整数 $X$ を無作為に選び**、 $A[X]$ を軸としてソートを行う。
1. 空の配列 $L, R$ を用意し、次の操作を $i=0, 1, \cdots, N-1$ について行う。
   1. $i = X$ ならば何も行わない。
   2. $i \neq X$ かつ $A[i] \lt A[X]$ ならば $A[i]$ を $L$ の末尾に追加する。
   3. $i \neq X$ かつ $A[i] \gt A[X]$ ならば $A[i]$ を $R$ の末尾に追加する。
   4. $i \neq X$ かつ $A[i] = A[X]$ ならば $A[i]$ を $L, R$ のどちらかの末尾にランダムに追加する。
2. $L, R$ を乱択クイックソートを用いて再帰的にソートする。空配列の場合は何も行わない。
3. ($L$ の要素), $A[X]$, ($R$ の要素) をこの順につなげてできる配列を出力する。
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

import random

N = int(input())
A = list(map(int, input().split()))


def quick_sort(V):
    if len(V) == 0:
        return []
    X = random.randrange(len(V))
    R, L = [], []
    for num_i in range(len(V)):
        if num_i == X:
            continue
        if V[num_i] == V[X]:
            if random.randrange(2):
                R.append(V[num_i])
            else:
                L.append(V[num_i])
        elif V[num_i] > V[X]:
            R.append(V[num_i])
        else:
            L.append(V[num_i])
    L = quick_sort(L)
    R = quick_sort(R)

    L.append(V[X])
    L.extend(R)
    return L

A = quick_sort(A)
print(*A)