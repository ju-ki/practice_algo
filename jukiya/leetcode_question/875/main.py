import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        min_banana, max_banana = 1, max(piles)
        answer = max(piles)
        while max_banana >= min_banana:
            medium_banana = (max_banana + min_banana) // 2
            h_counter = 0
            for p in piles:
                h_counter += math.ceil(p / medium_banana)
            if h_counter <= h:
                answer = min(answer, medium_banana)
                max_banana = medium_banana - 1
            else:
                min_banana = medium_banana + 1
        return answer


if __name__ == "__main__":
    s = Solution()
    piles = [3, 6, 7, 11]
    h = 8
    print(s.minEatingSpeed(piles=piles, h=h))
