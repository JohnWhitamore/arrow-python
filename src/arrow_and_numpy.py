import pyarrow as pa
import numpy as np

"""
Arrow and NumPy work together seamlessly.
"""


# NumPy array
np_array = np.array([10, 20, 30], dtype=np.int32)

# Convert to Arrow array
arrow_arr = pa.array(np_array)
print("Arrow Array:", arrow_arr)