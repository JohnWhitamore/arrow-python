import pyarrow as pa
import pandas as pd

"""
Arrow and Pandas work together seamlessly.
"""

# Create a Pandas dataframe
df = pd.DataFrame({
    "sales": [1, 2, 3, None, 5],
    "price": [10.0, 20.5, 30.25, 40.0, 50.0]
})

# Convert the dataframe to an Arrow table
table = pa.Table.from_pandas(df)
print("Arrow Table from Pandas:\n", table)

