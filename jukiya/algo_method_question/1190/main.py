"""
https://algo-method.com/tasks/1190

### 問題文
$2$ 進法表記された $N$ 桁の整数 $S$ と $T$ が与えられます。
ただし、$S$ や $T$ をちょうど $N$ 桁で表示するために、先頭の桁が $0$ 埋めされている可能性があります。
$S \times T$ を計算し、$2$ 進法表記で出力するプログラムを作成してください。
ただし、$S \times T$ の桁数が $N$ 桁を超えた場合は、下位 $N$ 桁を出力し、桁数が $N$ 桁未満の場合は、 $0$ 埋めして $N$ 桁で出力してください。
![image](https://algo-method-public-production.s3.ap-northeast-1.amazonaws.com/images%2Fb561a3cf-06a9-41ff-9143-391c3fe4d674%2Ffigure_single_1+%282%29.jpg)
<details><summary>ヒント</summary><div>
掛け算の筆算と同じ計算をエミュレートしてみましょう。
答えとなる長さ $N$ 桁の配列を準備して、$N$ 桁 $\times$ $1$ 桁の結果をずらしながら足していきます。
最後に繰り上がりの処理を行います。
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
S = input()
T = input()
divide_list = []
counter = 0

Ti = list(str(int(T)))
Ni = len(Ti)
Ti.reverse()


def bit_add(X, Y, N):
    X = list(X)
    Y = list(Y)
    carry_num = 0
    answer = []
    X.reverse()
    Y.reverse()

    for num_i in range(N):
        num = int(X[num_i]) + int(Y[num_i]) + carry_num
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
    return "".join(answer)


for num_i in range(Ni):
    num_T = int(Ti[num_i])
    if num_T == 0:
        counter += 1
        continue
    divide_result = []
    for s in S:
        divide_result.append(str(int(s) * num_T))
    for _ in range(counter):
        divide_result.append("0")
    divide_list.append("".join(divide_result))
    counter += 1


#かける方が全部0のパターンを想定できていなかった
if len(divide_list) > 0:
    max_divide_length = len(max(divide_list, key=len))
    divide_list = [divide.zfill(max_divide_length) for divide in divide_list]
    result = divide_list[0]

    for num_i in range(len(divide_list) - 1):
        result = bit_add(result, divide_list[num_i+1], max_divide_length)

    print(result[max_divide_length-N+1:])
else:
    print("0" * N)