import numpy as np
arr = np.array([1, 2, 3, 4])
y=arr.view()
y[0]=43
print(arr)
print(y)