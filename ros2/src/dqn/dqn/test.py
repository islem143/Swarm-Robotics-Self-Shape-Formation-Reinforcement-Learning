
import os 

import pickle

def load_pickle(path):
        with open(path, 'rb') as file:
            return pickle.load(file)
        


dir_path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(dir_path, "models-robot-2/my-model-320.obj")
replay_memory = load_pickle(path)
print(replay_memory[0])

