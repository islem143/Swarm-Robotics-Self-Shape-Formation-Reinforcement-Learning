import numpy as np


a=np.array([1,2,3,4,5,6,7,8,9,10])


b=np.concatenate((a[0:2],a[-2:]))
print(np.min(b))