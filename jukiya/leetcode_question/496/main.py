import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any

# 問題文勘違いしていた(隣だと思ってた)
# algo式のstackのスパン問題が理解できていないと解けなさそう


# 一応O(nums1.length+nums2.length)
class MyWrongSolution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        max_nums2 = max(nums2)
        num2_bucket = [-1] * (max_nums2 + 1)
        for i in range(len(nums2)):
            num2 = nums2[i]
            if i + 1 < len(nums2):
                num2_bucket[num2] = nums2[i+1]

        num_list = []
        for num1 in nums1:
            if num1 < num2_bucket[num1]:
                num_list.append(num2_bucket[num1])
            else:
                num_list.append(-1)
        return num_list


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        stack = []
        mapping = {}

        # num2間で大小関係をみる
        for n in nums2:
            print(f"*****{n}******")
            while stack and n > stack[-1]:
                mapping[stack.pop()] = n
            stack.append(n)
            print(stack)
            print(mapping)

        while stack:
            mapping[stack.pop()] = -1

        for n in nums1:
            res.append(mapping[n])

        return res


if __name__ == "__main__":
    nums1 = [1, 3, 5, 2, 4]
    nums2 = [6, 5, 4, 3, 2, 1, 7]
    s = Solution()
    print(s.nextGreaterElement(nums1, nums2))
