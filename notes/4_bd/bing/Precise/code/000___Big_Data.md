# Big Data

Here is an example of code that can be used for Big Data processing:

```python
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

conf = SparkConf().setAppName("BigData")
sc = SparkContext.getOrCreate(conf)

spark = SparkSession.builder.appName("BigData").getOrCreate()

data = spark.read.format("csv").option("header", "true").load("data.csv")

data.show()
```
