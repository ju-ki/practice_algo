N = int(input())
A = list(map(int, input().split()))
Q = int(input())

A.sort()
# ChatGPTに少し修正してもらった
for _ in range(Q):
    B = int(input())
    #B[-1]でもいい気がしたけど
    answer = float('inf')
    left, right = 0, len(A)-1
    while right > left:
        medium = (left + right) // 2
        if B > A[medium]:
            answer = min(answer, abs(B  - A[medium]))
            left = medium + 1
        elif B < A[medium]:
            answer = min(answer, abs(B - A[medium]))
            right = medium - 1
        else:
            answer = 0
            break
    # 恐らくここがなかったためWAになった?
    answer = min(answer, abs(B - A[left]))
    print(answer)