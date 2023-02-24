import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, val in enumerate(nums):
            # dictの x in collectionはAverage(1)
            if val in hashmap:
                return [hashmap[val], i]
            hashmap[target-val] = i


if __name__ == "__main__":
    nums = [3, 3, 6, 5]
    target = 6
    s = Solution()
    print(s.twoSum(nums, target))