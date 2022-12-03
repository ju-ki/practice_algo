"""
https://algo-method.com/tasks/524

### 問題文
ヒープソートは、与えられたいくつかの要素を、
所定の順序にしたがって並び替えるソートアルゴリズムです。
ヒープソートには次の特徴があります (要素の個数を $N$ とします)。
- ヒープと呼ばれるデータ構造を利用し、最大値から順に決定する
- 与えられた配列以外の記憶領域が不要 (in-place であるといいます)
- 最良、最悪、平均計算量はすべて $O(N \log N)$
以下に示すアルゴリズムは、
サイズ $N$ の配列 $A$ を昇順に並び替えるヒープソートの動作を表したものです。
ただし、次の条件を条件 $X_k$ と呼ぶこととします。
```Statement
すべての頂点 $i (0 \leq i \leq k-1)$ について次の条件が成り立つ。
・ $A[2i+1]$ が存在するならば、 $A[i] \geq A[2i+1]$
・ $A[2i+2]$ が存在するならば、 $A[i] \geq A[2i+2]$
```
----
1. 条件 $X_N$ を満たすように配列をソートする。(参考: [Q5-7. ヒープソートの準備](https://algo-method.com/tasks/518))
2. $i = N-1, N-2, \cdots, 1$ について次の操作を行う。
   1. $A[0]$ と $A[i]$ の要素を入れ替える。
   2. 条件 $X_i$ を満たすように配列をソートする。
3. 配列 $A$ の値を出力する。
---
このアルゴリズムを実装し、 **$i = M$ の操作が終了した時点での 配列 $A$ の様子と、 最終的な配列 $A$ の様子を出力してください**。
なお、手順 2-2.は配列の $i-1$ 番目の要素までに対して、[ヒープソートの準備](https://algo-method.com/tasks/518) 2-2.の内側の処理を $k=0$ のみについて行うことで実現できます。
これは、配列 $A$ はこの時点で条件 $X_i$ を $i \neq 0$ 以外の場合は満たしていることから説明できます。(余力があれば考えてみてください。)
### 入力
入力は次の形式から与えられます。
```IOExample
$N M$
$A_0 A_1 \cdots A_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $2$ 以上 $10^5$ 以下の整数
- $M$ は $1$ 以上 $N-1$ 以下の整数
- $A_i$ は $1$ 以上 $10^9$ 以下の整数 $(0 \leq i \leq N-1)$
### 出力
最初の行には「$i = M$ の操作が終了した時点での 配列 $A$ の様子」を、
次の行には「最終的な配列 $A$ の様子」をそれぞれ空白区切りで出力してください。
"""
debug = True
if debug:
    N, M = 6, 4
    A = [1, 4, 2, 8, 5, 7]
else:
    N, M = map(int, input().split())
    A = list(map(int, input().split()))


def align_element(v, start_pos, end_pos):
    k = start_pos
    while True:
        left = v[2*k+1] if 2*k+1 < end_pos else 0
        right = v[2*k+2] if 2*k+2 < end_pos else 0
        if left == 0 and right == 0:
            break
        elif v[k] >= left and v[k] >= right:
            break
        elif left >= right:
            v[k], v[2*k+1] = v[2*k+1], v[k]
            k = 2*k+1
        else:
            v[k], v[2*k+2] = v[2*k+2], v[k]
            k = 2*k+2


def build_heap(v):
    for x in range(len(v)//2-1, -1, -1):
        align_element(v, x, len(v))


def delete_node(v, end_pos):
    v[0], v[end_pos] = v[end_pos], v[0]
    align_element(v, 0, end_pos)


if __name__ == "__main__":
    build_heap(A)
    for num_i in range(N-1, 0, -1):
        delete_node(A, num_i)
        if num_i == M:
            print(*A)

    print(*A)
