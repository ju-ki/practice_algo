import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

if __name__ == "__main__":
    #入力の数分だけHello World!と出力する
    from utils.util import TestRunner
    path = os.getcwd()

    tr = TestRunner(path=path, fileName=sys.argv[1], project="test")
    N = int(tr.input())
    for _ in range(N):
        tr.answer("Hello World!")