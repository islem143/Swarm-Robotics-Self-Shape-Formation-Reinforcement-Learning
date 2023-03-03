import json
import pickle
from tensorflow import keras
import os


class Utils:
    @staticmethod
    def save_json(path, data):
        with open(path, "w+") as out:
            data = json.dumps(data)
            out.write(data)

    @staticmethod
    def save_pickle(path, data):
        with open(path, "wb+") as file:
            pickle.dump(data, file)

    @staticmethod
    def load_json(path, type):

        with open(path) as outfile:
            param = json.load(outfile)

            return param.get(type)

    @staticmethod
    def load_pickle(path):

        with open(path, 'rb') as file:
            return pickle.load(file)

    @staticmethod
    def save_model(model, path):
        model.save(path)

    @staticmethod
    def load_model(model, path):
        model.set_weights(keras.models.load_model(path).get_weights())
        return model
