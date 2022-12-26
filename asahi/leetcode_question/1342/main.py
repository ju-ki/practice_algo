import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


class Solution:
    def numberOfSteps(self, num: int) -> int:
        number = 0
        while num > 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num -= 1
            number += 1
        return number