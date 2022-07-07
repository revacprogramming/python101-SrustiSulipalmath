# Regular Expressions
# https://www.py4e.com/lessons/regex

import re
pattern = r'.'
pattern_regex = re.compile(pattern)
result = pattern_regex.findall(para)
print(result)
