import pyarrow as pa
import pyarrow.parquet as pq

"""
The beginnings of a realistic workflow
1. Define arrays
2. Define fields
3. Use arrays (data) and fields (schema) to create an Arrow table
4. Write the Arrow table to Parquet for long-term storage
"""

# Define arrays
sales_data = pa.array([1, 2, 3, None, 5])
x_data = pa.array([0.21, 0.35, 1.72, 2.01, 2.53])

# Define fields
sales_field = pa.field("sales_data", pa.int32(), nullable=True)
x_field = pa.field("x_data", pa.float64(), nullable=False)

# Construct a schema and a table
schema = pa.schema([sales_field, x_field])
table = pa.Table.from_arrays([sales_data, x_data], schema=schema)

# Display output
print("\nArrow Table:")
print(table)

print("\nSchema:")
print(table.schema)

# Parquet

# ... write
pq.write_table(table, "sales_data.parquet")

# ... read
loaded_table = pq.read_table("sales_data.parquet")
print("\nParquet table")
print(loaded_table)