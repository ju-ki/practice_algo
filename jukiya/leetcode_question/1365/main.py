import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


# O(n**2)だけは避けた
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_list = sorted(nums)
        counter_dict = {}
        for i in range(len(sorted_list)):
            if sorted_list[i] not in counter_dict:
                counter_dict[sorted_list[i]] = len(sorted_list[:i])
        answer_list = []
        for val in nums:
            answer_list.append(counter_dict[val])
        return answer_list