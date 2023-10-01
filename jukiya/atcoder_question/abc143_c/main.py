N = int(input())
S = input()


def rle(s):
    l = 0
    ans = []
    counter = 0
    while l < N:
        r = l + 1
        while r < N and S[l] == S[r]:
            r += 1
        counter += 1
        l = r
    return counter


print(rle(S))