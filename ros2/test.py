import numpy as np
import math
def get_distance(p1, p2):
        return float(np.sqrt(np.square(
            p1[1]-p2[1])+np.square(p1[0]-p2[0])))



distance = np.abs(3/9.6873629022557-0.10322726732650331)
print(distance)