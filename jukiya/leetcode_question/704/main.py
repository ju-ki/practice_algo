import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        answer = -1
        while left <= right:
            medium = (left + right) // 2
            if nums[medium] < target:
                left = medium + 1
            elif nums[medium] > target:
                right = medium -1
            elif nums[medium] == target:
                answer = medium
                return answer
        return answer


if __name__ == "__main__":
    s = Solution()
    nums = [5]
    target = 5
    print(s.search(nums, target))