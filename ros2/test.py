from tensorflow import keras
import tensorflow as tf
def loss_actor(y):
    return -tf.math.reduce_mean(y)
custom_objects = {"custom_loss_actor": loss_actor}
keras.utils.get_custom_objects().update(custom_objects)
# Load the model from the h5 file
model = keras.models.load_model('my-model-850-actor.h5')

# Print the summary of the model
model.summary()