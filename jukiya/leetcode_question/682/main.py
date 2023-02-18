import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        game_list = []
        for op in operations:
            if op == "C":
                game_list.pop()
            elif op == "D":
                game_list.append(game_list[-1] * 2)
            elif op == "+":
                s1 = game_list[-1]
                s2 = game_list[-2]
                game_list.append(s1 + s2)
            else:
                game_list.append(int(op))
        return sum(game_list)
