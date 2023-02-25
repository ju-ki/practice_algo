import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


# 全体の1/4しか考慮できていないっぽい
# しかも x in collection使用しているからO(N**2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer_list = []
        for num_x in range(len(nums)):
            if nums[num_x] > 0:
                break
            left, right = num_x + 1, len(nums) - 1
            while left < right:
                if nums[num_x] + nums[left] + nums[right] == 0:
                    if [nums[num_x], nums[left], nums[right]] not in answer_list:
                        answer_list.append(
                            [nums[num_x], nums[left], nums[right]])
                    break
                if nums[num_x] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[num_x] + nums[left] + nums[right] > 0:
                    right -= 1
        return answer_list

    # breakをleft+=1-->TLE
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer_list = []
        for num_x in range(len(nums)):
            left, right = num_x + 1, len(nums) - 1
            while left < right:
                if nums[num_x] + nums[left] + nums[right] == 0:
                    if [nums[num_x], nums[left], nums[right]] not in answer_list:
                        answer_list.append(
                            [nums[num_x], nums[left], nums[right]])
                    left += 1
                elif nums[num_x] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[num_x] + nums[left] + nums[right] > 0:
                    right -= 1
        return answer_list
    # ぎりぎりTLEにならない

    def threeSum3(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer_list = []
        for num_x in range(len(nums)):
            if nums[num_x] > 0:
                break
            left, right = num_x + 1, len(nums) - 1
            while left < right:
                if nums[num_x] + nums[left] + nums[right] == 0:
                    if [nums[num_x], nums[left], nums[right]] not in answer_list:
                        answer_list.append(
                            [nums[num_x], nums[left], nums[right]])
                    left += 1
                elif nums[num_x] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[num_x] + nums[left] + nums[right] > 0:
                    right -= 1
        return answer_list

    def threeSum4(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer_list = []
        for num_x in range(len(nums)):
            if nums[num_x] > 0:
                break
            left, right = num_x + 1, len(nums) - 1
            while left < right:
                if nums[num_x] + nums[left] + nums[right] == 0:
                    # 遅い原因if x in collectionだった
                    answer_list.append([nums[num_x], nums[left], nums[right]])
                    left += 1
                elif nums[num_x] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[num_x] + nums[left] + nums[right] > 0:
                    right -= 1
        return answer_list


if __name__ == "__main__":
    s = Solution()
    nums = [0, 0, 0, 0]
    print(s.threeSum(nums))
