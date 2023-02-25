import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


# Iで使用したコードも動くっぽい
# ソートされている場合Idxが+=1に意味があることを考慮する必要がある
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, val in enumerate(numbers):
            if val in hashmap:
                return [hashmap[val]+1, i+1]
            hashmap[target-val] = i

    # two-pointerを使用した解答
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
