"""
https://algo-method.com/tasks/1187

### 問題文
$2$ 進法表記された $N$ 桁の整数 $S$ が与えられます。
ただし、$S$ をちょうど $N$ 桁で表示するために、$S$ の先頭の桁が $0$ 埋めされている可能性があります。
また、$N$ は $4$ の倍数です。
$S$ をちょうど $N/4$ 桁の $16$ 進法表記に変換して出力するプログラムを作成してください。
必要な場合は先頭の桁を $0$ 埋めして、ちょうど $N/4$ 桁で表示してください。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$S$
```
また、入力される値は次の制約を満たします。
- $N$ は $16,32,64,256$ のどれか
- $S$ は $N$ 桁の $2$ 進法表記された整数
- $S$ の先頭の桁は $0$ 埋めされている可能性がある
### 出力
答えを出力してください。
"""


N = int(input())
S = input()


def ten_to_sixteen(val):
    def to_sixteen(val):
        if val < 10:
            return str(val)
        elif val == 10:
            return "A"
        elif val == 11:
            return "B"
        elif val == 12:
            return "C"
        elif val == 13:
            return "D"
        elif val == 14:
            return "E"
        elif val == 15:
            return "F"
    ans = []
    if val == 0:
        return "0"
    else:
        while val > 0:
            ans.append(str(val % 16))
            val //= 16
        ans.reverse()
        sixteen = int("".join(ans))
        return to_sixteen(sixteen)



answer = []

for num_i in range(0, N, 4):
    val = S[num_i:num_i+4]
    ten_num = 0
    for num_j in range(len(val)):
        ten_num += int(str(val)[num_j]) * (2 ** (len(str(val)) - num_j - 1))
    answer.append(ten_to_sixteen(ten_num))
print("".join(answer))