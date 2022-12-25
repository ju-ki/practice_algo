import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num > 0:
            counter += 1
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
        return counter