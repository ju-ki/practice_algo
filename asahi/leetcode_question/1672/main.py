import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        number = 0
        for i in accounts:
            number = max(number,sum(i))
        return number