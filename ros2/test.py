import numpy as np
import time
import  itertools 
import random
a=[0.8,0.0,-0.8]



c=[list(p) for p in itertools.product(a, repeat=2)]

perm_list = list(itertools.combinations(c, 6))
print(len(perm_list))

goals=[]

while len(goals)!=200:
    s=random.choice(perm_list)
    if(s not in goals):
        goals.append(list(s))


#print(goals)

def get_distance( p1, p2):
        return float(np.sqrt(np.square(
            p1[1]-p2[1])+np.square(p1[0]-p2[0])))


print(get_distance([5.0,5.0],[-5.0,-5.0]))