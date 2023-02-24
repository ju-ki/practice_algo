import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] == nums[j] and i < j:
                    counter += 1
        return counter