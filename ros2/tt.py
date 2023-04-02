import numpy as np
import tensorflow as tf
a = np.array([[1,2,5,6]])

# Reshaping the array to an array of arrays with shape (5, 1)
#b = a.reshape((-1, 1))
b=tf.reshape(a,(-1,1))
print(b)