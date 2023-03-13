#### Stages and Tasks in Spark

- Spark is a distributed computing framework that can process large-scale data in parallel using clusters of machines.
- Spark divides the data into partitions, which are logical chunks of data that can be processed by different executors (workers) in parallel.
- Spark also divides the computation into stages, which are groups of tasks that perform the same operation on different partitions of data.
- A task is a unit of work that is sent to an executor by the driver (master) to process a partition of data and produce an output.
- A stage consists of one or more tasks that have the same shuffle dependency, which means they depend on the same set of partitions from the previous stage or the original data source.
- A shuffle dependency occurs when the data needs to be redistributed across the cluster, such as when performing a join, groupBy, reduceByKey, or sortBy operation.
- A shuffle dependency can be narrow or wide, depending on how many partitions of the parent RDD are used by each partition of the child RDD.
- A narrow dependency means that each partition of the child RDD depends on at most one partition of the parent RDD, such as when performing a map, filter, or union operation.
- A wide dependency means that each partition of the child RDD depends on multiple partitions of the parent RDD, such as when performing a join, groupBy, reduceByKey, or sortBy operation.
- Spark tries to minimize the number of shuffles and the amount of data shuffled, as they are expensive operations that involve network communication and disk I/O.
- Spark creates a DAG (directed acyclic graph) of stages based on the RDD transformations and actions in the application code, and optimizes the DAG by applying various rules, such as pipelining, coalescing, and caching.
- Pipelining means that Spark combines multiple narrow transformations into a single stage, and executes them in memory without writing intermediate data to disk.
- Coalescing means that Spark reduces the number of partitions of an RDD by combining adjacent partitions, which can reduce the shuffle cost and the memory usage.
- Caching means that Spark can persist an RDD in memory or on disk, and reuse it in subsequent stages without recomputing it.
- Spark executes the DAG of stages in a lazy manner, which means that it only computes the RDDs when an action is triggered, such as count, collect, save, or show.
- Spark also supports dynamic allocation of executors, which means that it can scale up or down the number of executors based on the workload and the available resources.
- Spark provides a web UI that can show the details of the stages, tasks, executors, and RDDs in the application, as well as the metrics, logs, and events.

Here is an example of a Spark application that reads a text file, counts the number of words in each line, and saves the result as a CSV file.

```python
# Import SparkSession
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("WordCount").getOrCreate()

# Read a text file as an RDD
rdd = spark.sparkContext.textFile("input.txt")

# Split each line into words and count the number of words
rdd = rdd.map(lambda line: line.split()) \
         .map(lambda words: (len(words), 1)) \
         .reduceByKey(lambda x, y: x + y)

# Convert the RDD to a DataFrame
df = rdd.toDF(["word_count", "line_count"])

# Save the DataFrame as a CSV file
df.write.csv("output.csv")

# Stop the SparkSession
spark.stop()
```

The DAG of stages for this application is shown below:

```
    input.txt
       |
       |  map
       |  map
       |  reduceByKey
       v
    (word_count, line_count)
       |
       |  toDF
       v
    DataFrame
       |
       |  write.csv
       v
    output.csv
```

There are two stages in this DAG:

- Stage 1: This stage has a narrow dependency, as each partition of the input RDD depends on one partition of the text file. It performs the map, map, and reduceByKey transformations on the input RDD, and produces an output RDD with the word count and line count for each partition.
- Stage 2: This stage has a wide dependency, as each partition of the output RDD depends on multiple partitions of the input RDD. It performs the toDF and write.csv actions on the output RDD, and saves the result as a CSV file.

Each stage consists of one or more tasks, depending on the number of partitions of the RDDs involved. For example, if the input RDD has