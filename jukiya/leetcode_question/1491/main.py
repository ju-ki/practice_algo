import re
import math
from copy import deepcopy
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from typing import List, Union, Optional, Any


#問題文ちゃんと読んで
class Solution:
    def average(self, salary: List[int]) -> float:
        total_salary = 0
        max_salary, min_salary = max(salary), min(salary)
        salary.remove(max_salary)
        salary.remove(min_salary)
        employee_count = len(salary)
        for num_salary in salary:
            total_salary += num_salary
        average_salary = total_salary / employee_count
        return average_salary