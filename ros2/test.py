import numpy as np
def get_distance(p1, p2):
        return float(np.sqrt(np.square(
            p1[1]-p2[1])+np.square(p1[0]-p2[0])))

max_dist=get_distance([3.5,3.5],[-3.5,-3.5])


def normilize(value,max,min):
          return (value-min)/(max-min)



print(max_dist)