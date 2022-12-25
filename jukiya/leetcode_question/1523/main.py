import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


#シンプルにfor分で回したらtime limit
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odd_counter = 0
        if low % 2 == 0 and high % 2 == 0:
            odd_counter = (high - low) // 2
        else:
            odd_counter = (high - low) // 2 + 1
        return odd_counter