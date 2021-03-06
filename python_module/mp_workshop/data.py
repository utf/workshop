import os

import numpy as np

from monty.serialization import loadfn

data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data_files")
atomic_weights = loadfn(os.path.join(data_dir, "atomic_weights.json"))
atomic_numbers = loadfn(os.path.join(data_dir, "atomic_numbers.json"))
with open(os.path.join(data_dir, "words")) as f:
    words = [line for line in f]

crystals = loadfn(os.path.join(data_dir, "crystals.json"))
inflammation = np.loadtxt(os.path.join(data_dir, "inflammation-01.csv"), delimiter=",")
