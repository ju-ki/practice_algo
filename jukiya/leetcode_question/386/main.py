import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


# 最初の自分の答えと違うのはsortのkeyがxじゃなくてx[0]にしてたこと(比較対象を0文字目に限定してしまったことが原因)
# N=150の場合 1, 10, 11, ...., 19 100, 101...だと思ってた
# 一文字目が同じなら二文字目を比較する
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        lexicographical_list = []
        for i in range(1, n+1):
            lexicographical_list.append(str(i))
        lexicographical_list.sort(key=lambda x: x)
        lexicographical_list = [int(i) for i in lexicographical_list]
        return lexicographical_list


if __name__ == "__main__":
    # この仕様今知った笑
    # s1 = "1"
    # s2 = "10"
    # s3 = "150"
    # s4 = "2"
    # print(s1 < s2):True
    # print(s1 < s3):True
    # print(s1 < s4):True
    # print(s3 < s4):True
    s = Solution()
    print(s.lexicalOrder(150))
