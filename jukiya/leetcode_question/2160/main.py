import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


num = 2932


class Solution:
    def minimumSum(self, num: int) -> int:
        num = [num_i for num_i in list(str(num))]
        num_list = []
        for val in permutations(num, r=4):
            val = list(val)
            for num_i in range(1, 4):
                num_sum = int("".join(val[num_i:])) + int("".join(val[:num_i]))
                num_list.append(num_sum)
        min_num = min(num_list)
        return min_num


# another answer
class Solution2:
    def minimumSum(self, num: int) -> int:
        num = sorted(str(num),reverse=True)
        return int(num[0]) + int(num[1]) + int(num[2])*10 + int(num[3])*10

# 9322であれば -> 9+3+20+20


if __name__ == "__main__":
    solution = Solution()
    answer = solution.minimumSum(num)
    print(answer)