import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = ["".join(sorted(s)) for s in strs]
        anagram_dict = {}
        for i, sort_str in enumerate(sorted_list):
            if sort_str not in anagram_dict.keys():
                anagram_dict[sort_str] = []
            anagram_dict[sort_str].append(strs[i])

        answer_list = []
        for i, val in anagram_dict.items():
            answer_list.append(val)
        return answer_list


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    print(s.groupAnagrams(strs))
