import tensorflow as tf

actions=[1,2,0,3,5,0]
masks = tf.one_hot(actions, 5)
print(masks)