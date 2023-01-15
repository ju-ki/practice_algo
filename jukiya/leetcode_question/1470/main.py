import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        for num_i in range(n):
            output.append(nums[num_i])
            output.append(nums[num_i + n])
        return output