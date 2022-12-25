import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum_accounts_list = []
        for num_i in range(len(accounts)):
            sum_accounts_list.append(sum(accounts[num_i]))
        max_wealth = max(sum_accounts_list)
        return max_wealth