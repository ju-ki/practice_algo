import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


# monotonic stackが分からなかったので調べました
# https://itnext.io/monotonic-stack-identify-pattern-3da2d491a61e
# 上記のサイトのコードを一部問題用に合わせたら通りました

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n

        for i in range(n):
            base = i
            tmp = temperatures[i]
            print(f"***{tmp}***")
            # 現在の気温と1個前の気温を比較して現在の方が高ければインデックスの差分を答えに加える
            while len(stack) > 0 and tmp > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = base - idx
            # インデックスを保存
            stack.append(i)
        return res


if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    s = Solution()
    print(s.dailyTemperatures(temperatures))
