#### Scaling out with Hadoop

Hadoop is an open-source software framework for distributed storage and processing of large datasets. It is designed to scale out from a single server to thousands of machines, each offering local computation and storage. Here is an example of how to scale out with Hadoop:

```python
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("ScaleOut").setMaster("local")
sc = SparkContext.getOrCreate(conf)

data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data)

result = distData.reduce(lambda a, b: a + b)
print(result)
```

This code creates a SparkConf object and sets the application name and master URL. The master URL is set to "local" to run the application locally. The SparkContext is then created using the configuration. The data is then parallelized using the `parallelize` method, which distributes the data across the cluster. The `reduce` method is then used to aggregate the data and compute the result. The result is then printed to the console.
