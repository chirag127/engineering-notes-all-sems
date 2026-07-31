### Unit 3 - Map Reduce

MapReduce is a programming model used for processing large datasets across a large number of nodes. It is designed to perform distributed and parallel computations using large datasets. Here is how MapReduce works:

1. **Map**: The first step in the MapReduce algorithm is the Map task. This task takes a set of data and converts it into another set of data, where individual elements are broken down into tuples (key-value pairs). The input datasets are usually split and then processed independently by the Map tasks in a completely parallel manner.

2. **Shuffle and Sort**: After the Map task is completed, the output is sorted and input to reduce tasks.

3. **Reduce**: The second important task in the MapReduce algorithm is the Reduce task. This task takes the output from the Map task and combines the data tuples into a smaller set of tuples.

MapReduce can be used to perform a wide range of data processing tasks, including data filtering, data sorting, and data aggregation. It is a powerful tool for processing large datasets and is widely used in the field of Big Data.