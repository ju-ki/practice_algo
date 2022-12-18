No = 1
title = "Title"
link = "Link"
get_question:
	mkdir ${No}
	touch ${No}/main.py
	echo import re >> ${No}/main.py
	echo import math >> ${No}/main.py
	echo from copy import deepcopy >> ${No}/main.py
	echo from itertools import product, permutations, combinations >> ${No}/main.py
	echo from collections import Counter, defaultdict >> ${No}/main.py
	echo from typing import List, Union, Optional, Any >> ${No}/main.py
	code ${No}/main.py
create_readme:
	touch README.md
	echo "| number | title                                  | link                                                                  |" >>  README.md
	echo "| ------ | -------------------------------------- | --------------------------------------------------------------------- |" >> README.md
update:
	echo "| ${No}      | ${title}                                 | ${link}                                |" >>  README.md