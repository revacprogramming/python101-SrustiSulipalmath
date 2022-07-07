# Regular Expressions
# https://www.py4e.com/lessons/regex

#import re
#pattern_regex = re.compile(pattern)
#result = pattern_regex.findall(para)
#print(result)

import re
hand=open('file12.txt')
lst=[]
for line in hand:
    line = line.rstrip()
    x = re.findall('([0-9]+)', line)
    int_x=list(map(int,x))
    lst.extend(int_x)

total=sum(lst)
print('Total:',total)
