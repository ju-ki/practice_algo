import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


# numericを見落としてた+正規表現内に空白はNG
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        pattern = r"[a-z0-9]*"
        s = list("".join(re.findall(pattern=pattern, string=s)))
        original_s = s.copy()
        start, end = 0, len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return s == original_s

    # 個人的にかなり好きな解答
    def isPalindrome2(self, s: str) -> bool:
        forward_s = [c for c in s.lower() if c.isalnum()]
        backward_s = forward_s[::-1]
        return forward_s == backward_s


if __name__ == "__main__":
    s = Solution()
    text = "A man, a plan, a canal: Panama"
    print(s.isPalindrome(s=text))
    print(s.isPalindrome2(s=text))
