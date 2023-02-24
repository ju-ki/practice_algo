import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        #シンプル解答
        # return sum(map(jewels.count, stones))
        stone_list = [0 for _ in range(57)]
        for stone in stones:
            stone = ord(stone)-65
            stone_list[stone] += 1

        counter = 0
        for jewel in jewels:
            jewel = ord(jewel)-65
            counter += stone_list[jewel]
        return counter


if __name__ == "__main__":
    s = Solution()
    jewels = "aA"
    stones = "aAAbbbb"
    print(s.numJewelsInStones(jewels, stones))
