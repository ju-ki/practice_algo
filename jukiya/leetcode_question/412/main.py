import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output_list = []
        for num_n in range(1, n+1):
            if num_n % 3 == 0 and num_n % 5 == 0:
                output_list.append("FizzBuzz")
            elif num_n % 3 == 0:
                output_list.append("Fizz")
            elif num_n % 5 == 0:
                output_list.append("Buzz")
            else:
                output_list.append(str(num_n))
        return output_list