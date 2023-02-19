"""
https://algo-method.com/tasks/870

### 問題文
今回は英小文字からなる文字列 $S$ に対して次のようなハッシュ関数 $h(S)$ を考えます。
ここでは $B = 30$、$M = 1000003$ とします ($B, M$ の定め方には任意性があります)。
なおこのハッシュ関数は、しばしば**ローリングハッシュ**と呼ばれます。
----
文字列 $S$ の $i$ 番目の文字 $S_i$ (英小文字) に対して、
'a'〜'z' をそれぞれ $1$〜$26$ に対応させたものを $c_i$ とします。そして
$\displaystyle h(S) = \sum_{i = 0}^{|S|-1} c_{|S|-1-i} B^i$ を $M$ で割ったあまり
とします。つまり $\left( c_0, c_1, \ldots, c_{|S|-1} \right)$ を $B$ 進数の整数とみなし、それを $M$ で割ったあまりとします。
なお $|S|$ は文字列 $S$ の長さを表します。
----
$N$ 個の文字列 $S_{0}, S_{1}, \dots, S_{N-1}$ が与えられますので、
($B = 30$、$M = 1000003$ とした) 上記のローリングハッシュによってそれぞれのハッシュ値を計算し、
最も多く登場するハッシュ値について、その登場回数を答えてください。
この答えが $1$ より大きい場合、ハッシュの衝突が発生していると言えます。
なお、方針によっては計算途中の数値が 32bit 整数型に収まらない可能性があることに注意してください。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$S_0 S_1 \ldots S_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $10^{5}$ 以下の整数
- $S_i$ は英小文字のみからなる長さ $10$ 以下の文字列 $(0 \leq i \leq N-1)$
- $S_0, S_1, \dots, S_{N-1}$ はすべて互いに相異なる
### 出力
答えを出力してください。
"""


def str_to_num(s):
    ret = ord(s) - 96
    return ret


def hash30(txt):
    total = 0
    for i in range(len((txt))):
        s = txt[-1-i]
        s = str_to_num(s)
        total += s * (30 ** i)
    return total


def rolling_hash(S):
    total = 0
    for i in range(len(S)):
        s = S[-1-i]
        s = hash30(s)
        total += s * (30 ** i)
    ret = total % 1000003
    return ret


N = int(input())
S = list(input().split())

counter_list = [0] * (1000003)

for s in S:
    s = rolling_hash(s)
    counter_list[s] += 1

answer = max(counter_list)
print(answer)
