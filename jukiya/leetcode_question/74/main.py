import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        while right >= left:
            medium = (right + left) // 2
            medium_matrix = matrix[medium]
            left2, right2 = 0, len(medium_matrix) - 1
            while right2 >= left2:
                medium2 = (right2 + left2) // 2
                if medium_matrix[left2] > target:
                    right -= 1
                    break
                elif medium_matrix[right2] < target:
                    left += 1
                    break
                elif medium_matrix[medium2] < target:
                    left2 = medium2 + 1
                elif medium_matrix[medium2] > target:
                    right2 = medium2 - 1
                elif medium_matrix[medium2] == target:
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    matrix = [[3]]
    target = 3
    print(s.searchMatrix(matrix=matrix, target=target))