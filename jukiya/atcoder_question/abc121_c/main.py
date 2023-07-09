N, M = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N)]

AB = sorted(AB, key=lambda x: x[0])
num = 0
ans = 0
for i in range(N):
    #全て購入しても超えていないなら
    if M > num + AB[i][1]:
        ans += AB[i][0] * AB[i][1]
        num += AB[i][1]
    else:
        #超えているのなら->残り購入数を追加
        ans += AB[i][0] * (M - num)
        print(ans)
        break