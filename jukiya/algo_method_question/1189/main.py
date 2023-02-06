"""
https://algo-method.com/tasks/1189

### 問題文
$2$ 進法表記された $N$ 桁の整数 $S$ と $T$ が与えられます。
ただし、$S$ や $T$ をちょうど $N$ 桁で表示するために、先頭の桁が $0$ 埋めされている可能性があります。
$S+T$ を計算し、$2$ 進法表記で出力するプログラムを作成してください。
ただし、$S+T$ の桁数が $N$ 桁を超えた場合は、下位 $N$ 桁を出力し、桁数が $N$ 桁未満の場合は、$0$ 埋めして $N$ 桁で出力してください。
![image](https://algo-method-public-production.s3.ap-northeast-1.amazonaws.com/images%2Fe2d83d79-927b-471d-8336-f1e25490cd63%2Ffigure_single_0.jpg)
<details><summary>ヒント</summary><div>
足し算の筆算と同じ計算をエミュレートしてみましょう。
また、ちょうど $N$ 桁で出力する必要がある点に注意してください。
</div></details>
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$S$
$T$
```
また、入力される値は次の制約を満たします。
- $N$ は $8,16,32,64,256$ のどれか
- $S$ は $N$ ビットで表現された符号なし整数
### 出力
答えを出力してください。必ず $N$ 桁で出力してください。
"""

N = int(input())
S = list(input())
T = list(input())
S.reverse()
T.reverse()
carry_num = 0
answer = []

for num_i in range(N):
    num = int(S[num_i]) + int(T[num_i]) + carry_num
    if num == 2:
        answer.append("0")
        carry_num = 1
    elif num == 3:
        answer.append("1")
        carry_num = 1
    else:
        answer.append(str(num))
        carry_num = 0
answer.append(str(carry_num))


answer.reverse()

if len(answer) > N:
    print(''.join(answer[-N:]))
elif len(answer) < N:
    for _ in range(N - len(answer)):
        answer.insert(0, "0")
        print(''.join(answer))
else:
    print(''.join(answer))

