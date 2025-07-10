# arrow-python

### What is Apache Arrow?
- columnar in-memory data format designed for high-performance analytics.
- allows zero-copy reads: data can be shared between systems without serialisation overhead.
- used under the hood by Pandas and Polars and also Spark.
- available in Python via PyArrow.

My principal use case for Arrow is sharing data between systems. Contrast:
- Conventional: serialise to csv, json, etc; copy into memory;  parse and reinterpret data types.
- Arrow: in-memory representation that can be shared directly across systems / processes.

### Installation
- `pip install pyarrow`
- `conda install -c conda-forge pyarrow`

 ### data/

 `sales_data.parquet`: a small Parquet file containing sales data created using Arrow.

 ### src/

 `getstarted.py`: defines an array, uses the array to create a table, inspect the table's schema.  
 `arrow_and_numpy.py`: it's incredibly easy to convert Numpy arrays to Arrow arrays. Seamless integration.  
 `arrow_and_pandas.py`: it's also easy to convert a Pandas dataframe into an Arrow table. Also seamless.  
 `arrow_and_parquet.py`: creates an Arrow table and stores it as a Parquet file.  
