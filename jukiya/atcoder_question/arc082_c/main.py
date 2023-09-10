from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

numDict = defaultdict(int)

for i in range(N):
    numDict[A[i]] += 1

counter = 0
for idx, num in numDict.items():
    if idx == num:
        continue
    #値を足すことはできないことを考慮できていなかった
    counter += min(abs(idx - num), num)
    #こっちがあっている
    # if idx > num:  # 数字の値が出現回数より大きい場合
    #     counter += num
    # else:  # 数字の値が出現回数以下の場合
    #     counter += num - idx
print(counter)