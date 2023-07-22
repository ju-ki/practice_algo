N = int(input())
S = input()

answer = ''
for letter in S:
    answer += chr(ord('A') + (ord(letter) - ord('A') + N) % 26)

print(answer)