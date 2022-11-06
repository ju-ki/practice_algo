"""
https://algo-method.com/tasks/1028

### 問題文
あなたはある施設の来場者数データを持っています。
このデータは日 $0$ から 日 ${N-1}$ までの $N$ 日分のデータからなっています。
日 $i$ の来場者数は $X_{i}$ 人と記録されています。
あなたはこのデータを利用して、繁忙期を求めるプログラムを作成することにしました。
具体的には、連続した $D$ 日間のうち、最も来場者数が多かった期間を求めるプログラムを作成してください。
ただし、答えが複数考えられる場合は最も現在に近い日を答えてください。
### 入力
入力は次の形式で与えられます。
```IOExample
$N D$
$X_0 X_1 \ldots X_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $10^5$ 以下の整数
- $D$ は $1$ 以上 $N$ 以下の整数
- $X_i$ は $1$ 以上 $10^4$ 以下の整数 $(0 \leq i \leq N-1)$
### 出力
答えを次の形式で出力してください。
ただし、 $S, T$ はそれぞれ期間の開始日と期間の終了日です。
```IOExample
$S$~$T$
```
"""

N, D = map(int, input().split())
X = list(map(int, input().split()))
acc_list = [0] * (N+1)

for idx, val in enumerate(X):
    acc_list[idx+1] = acc_list[idx] + val


max_attendance = 0
max_attendance_date = 0
for num_d in range(N-D+1):
    attendance_count = acc_list[num_d+D] - acc_list[num_d]
    if attendance_count >= max_attendance:
        max_attendance = attendance_count
        max_attendance_date = num_d


max_end = max_attendance_date + D - 1
print(f"{max_attendance_date}~{max_end}")