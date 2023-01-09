import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


class Solution:
    def sortSentence(self, s: str) -> str:
        sentence_list = []
        for word in list(s.split(" ")):
            print(word)
            new_word = word[:-1]
            num = int(word[-1])
            sentence_list.append([num, new_word])
        sentence_list.sort(key=lambda x: x[0])
        output_text = ""
        for (num, word) in sentence_list:
            if num != 1:
                output_text += " " + word
            else:
                output_text += word
        return output_text


if __name__ == "__main__":
    s = "is2 sentence4 This1 a3"
    solution = Solution()
    print(solution.sortSentence(s=s))