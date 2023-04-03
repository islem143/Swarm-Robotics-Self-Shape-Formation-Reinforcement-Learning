import numpy as np
import tensorflow as tf
arr=[1,2,3]

for index in tf.range(2):
    print(arr[index])
y = tf.map_fn(lambda x_i: x_i + 1, tf.constant([1, 2, 3]))
print(y)