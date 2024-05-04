# NumPy is a Python library used for working with arrays.
# python list - slow, numpy - 50x faster (b/c NumPy arrays are stored at one continuous place
# in memory unlike lists, so processes can access and manipulate them very efficiently.(locality of reference ))
# The array object in NumPy is called ndarray

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)  # [1 2 3 4 5]

#check numpy version
print(np.__version__)