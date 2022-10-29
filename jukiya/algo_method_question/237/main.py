N = int(input())
counter = 0


def get_palindrome_flag(text: str) -> bool:
    same_flag = True
    li_str_i = list(text)
    for str_j, rev_str_j in zip(li_str_i, reversed(li_str_i)):
        if str_j != rev_str_j:
            same_flag = False
            break
    return same_flag

for _ in range(N):
    text = input()
    if get_palindrome_flag(text=text):
        counter += 1
print(counter)