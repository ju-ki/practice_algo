"""
https://algo-method.com/tasks/929

### 問題文
あるクラスには $N$ 人の生徒がいます。
各生徒の出席番号は $0, 1, \dots, N-1$ です。
出席番号が $i$ である生徒のことを、生徒 $i$ と呼ぶことにします。
生徒 $i$ の名前は $S_i$ で、身長は $h_i$ です。
この生徒たちが次の条件を満たすように一列に並びました (いわゆる背の順です)。
```IOExample
どの生徒 $i$ についても、生徒 $i$ の前にいる生徒は、次のいずれかの条件を満たす
・生徒 $i$ よりも、身長が小さい
・生徒 $i$ と身長が等しく、出席番号が小さい
```
一列に並んだ状態において、
生徒 $X$ の $1$ つ前にいる生徒と $1$ つ後ろにいる生徒の名前を答えてください。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$ $X$
$S_0$ $h_0$
$S_1$ $h_1$
$\vdots$
$S_{N-1}$ $h_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $1000$ 以下の整数
- $X$ は $0$ 以上 $N - 1$ 以下の整数
- $S_i$ は半角英小文字からなる長さ $1$ 以上 $10$ 以下の文字列 $(0 \leq i \leq N-1)$
- $h_i$ は $100$ 以上 $200$ 以下の整数 $(0 \leq i \leq N-1)$
- 一列に並んだとき、出席番号 $X$ の生徒の前後には必ず人がいる
### 出力
答えを $2$ 行で出力してください。
最初の行には出席番号 $X$ の前にいる生徒の名前を、次の行には後ろにいる生徒の名前を出力してください。
"""

N, X = map(int, input().split())
student_data = []
# 名前を数字に変更
for num_i in range(N):
    name, height = map(str, input().split())
    student_data.append([num_i, name, int(height)])

student_data.sort(key=lambda x: (x[2], x[0]))

for num_i, student in enumerate(student_data):
    if student[0] == X:
        print(f'{student_data[num_i-1][1]}')
        print(f'{student_data[num_i+1][1]}')
        break