import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output_list = []
        num_length = len(nums)
        for i in range(num_length):
            output_list.append(sum(nums[:i+1]))
            
        return output_list
