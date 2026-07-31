#### Auditing of Big Data

Here is an example of code for auditing Big Data:

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create a Spark session
spark = SparkSession.builder.appName("BigDataAudit").getOrCreate()

# Load data from HDFS
data = spark.read.format("csv").option("header", "true").load("hdfs://path/to/data.csv")

# Define audit function
def audit_data(data):
    # Count number of rows
    row_count = data.count()
    print(f"Number of rows: {row_count}")

    # Count number of null values in each column
    null_counts = data.select([count(when(isnan(c) | col(c).isNull(), c)).alias(c) for c in data.columns])
    print("Number of null values in each column:")
    null_counts.show()

    # Compute summary statistics for numeric columns
    summary = data.describe()
    print("Summary statistics for numeric columns:")
    summary.show()

# Run audit on data
audit_data(data)
```
