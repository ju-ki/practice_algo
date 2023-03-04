import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        answer = 0
        for num_i in range(len(prices)):
            if min_price > prices[num_i]:
                min_price = prices[num_i]
            answer = max(answer, prices[num_i] - min_price)
        return answer


if __name__ == "__main__":
    s = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(s.maxProfit(prices=prices))