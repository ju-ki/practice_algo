import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_word_counter = 0
        for sentence in sentences:
            max_word_counter = max(max_word_counter, len(sentence.split()))
        return max_word_counter