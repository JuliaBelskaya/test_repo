from random import randint
from itertools import groupby
 
l = [randint(1,10) for _ in range(100)]
s = ''
for i in range(1,len(l)):
    if l[i-1] < l[i]: 
        s += '+'
    else: s += '-'

g = groupby(s)
out = [k for k,v in g if k == '+']
print('result:',len(out))
        
