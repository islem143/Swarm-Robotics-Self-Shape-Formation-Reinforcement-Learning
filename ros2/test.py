import numpy as np
import time
import  itertools 
import random
a=[1.0,0.0,2.0]



c=[list(p) for p in itertools.product(a, repeat=2)]

perm_list = list(itertools.combinations(c,4))
print(len(perm_list))
#print(perm_list)

goals=perm_list[0:126]
print(len(goals))
print(goals)
# while len(goals)!=200:
#     s=random.choice(perm_list)
#     if(s not in goals):
#         goals.append(list(s))




def get_distance( p1, p2):
        return float(np.sqrt(np.square(
            p1[1]-p2[1])+np.square(p1[0]-p2[0])))

print(get_distance([3.0,3.0],[-3.0,-3.0]))