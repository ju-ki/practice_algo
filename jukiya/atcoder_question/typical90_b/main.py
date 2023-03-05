N = int(input())

# このやり方だと順番が違う見たい(解答自体は間違ってないと思う)->制約に辞書順にと書いているからダメっぽい
def check_parentheses(M):
    dep = 0
    for i in range(len(M)):
        if M[i] == "(":
            dep += 1
        if M[i] == ")":
            dep -= 1
        if dep < 0:
            return False
    if dep ==0:
        return True
    return False


for i in range(2 ** N):
    answer = []
    for j in reversed(range(N)):
        # 左シフト
        if ((i & (1 << j)) == 0):
            answer.append("(")
        else:
            answer.append(")")
    if check_parentheses(answer):
        answer = "".join(answer)
        print(answer)