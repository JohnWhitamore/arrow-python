import pyarrow as pa

# Arrow array of integers
sales_data = pa.array([1, 2, 3, None, 5], type=pa.int32())
print("Arrow Array:", sales_data)
print("Array Type:", sales_data.type)

# Wrap the data in a Table
# ... a table is a collection of arrays
# ... each array is identified by its column name e.g. "sales_data"
table = pa.table({'sales_data': sales_data})
print("\nArrow Table:")
print(table)

# Inspect the table schema
print("\nSchema:")
print(table.schema)