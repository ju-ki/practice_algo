import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(list(set(nums)))