import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        N = 0
        if low % 2 == 0 and high % 2 == 0:
            N = (high - low) // 2
        elif low % 2 == 1 and high % 2 == 1:
            N = (high - low) // 2 + 1
        else:
            N = (high - low) // 2 + 1
        return N