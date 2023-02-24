import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_str = {'(': ')', '[': ']', '{': '}'}
        for i in s:
            if i in dict_str:
                stack.append(dict_str[i])
            elif len(stack) > 0 and i == stack[-1]:
                stack.pop()
            else:
                return False

        return len(stack) == 0