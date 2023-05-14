import numpy as np
import time
import  itertools 
import random
a=[-1.0,0.0,1.0]



c=[list(p) for p in itertools.product(a, repeat=2)]

perm_list = list(itertools.combinations(c, 5))
print(len(perm_list))

goals=[]

while len(goals)!=126:
    s=random.choice(perm_list)
    if(s not in goals):
        goals.append(list(s))


print(goals[0])