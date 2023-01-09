import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans.append(nums[num])
        return ans