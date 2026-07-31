# MapReduce

MapReduce is a framework for processing parallelizable problems across large datasets using a large number of computers (nodes), collectively referred to as a cluster or a grid. It is based on the idea of dividing the input data into smaller chunks, applying a map function to each chunk in parallel, and then combining the results using a reduce function.

Some key features of MapReduce are:

- It is scalable, fault-tolerant, and distributed.
- It abstracts the details of data distribution, load balancing, and network communication from the programmer.
- It supports a variety of data formats, such as text, binary, and structured data.
- It can be implemented using various languages, such as Java, Python, and C++.

## MapReduce Framework

A MapReduce framework (or system) is usually composed of three operations (or steps) :

- **Map**: each worker node applies the map function to the local data, and writes the output to a temporary storage. A master node ensures that only one copy of the redundant input data is processed.
- **Shuffle**: the worker nodes redistribute the data based on the output keys (produced by the map function), such that all data belonging to one key is located on the same worker node.
- **Reduce**: the worker nodes now process each group of output data, per key, in parallel. The reduce function is applied to each group, and the output is written to the final storage.

The following diagram illustrates the MapReduce framework:

![MapReduce framework](https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Mapreduce_wordcount.svg/1200px-Mapreduce_wordcount.svg.png)

## MapReduce Example

A common example of MapReduce is the word count problem, where the goal is to count the frequency of each word in a large text corpus. The map function takes a line of text as input, and emits a key-value pair for each word, where the key is the word and the value is 1. The reduce function takes a key and a list of values as input, and sums up the values to get the total count for each word.

The following pseudo-code shows the map and reduce functions for the word count problem:

```
map(line):
  for word in line.split():
    emit(word, 1)

reduce(key, values):
  sum = 0
  for value in values:
    sum += value
  emit(key, sum)
```

The following table shows an example of the input and output of the map and reduce functions:

| Input | Map Output | Shuffle Output | Reduce Output |
| ----- | ---------- | -------------- | ------------- |
| Hello world | (Hello, 1), (world, 1) | (Hello, [1]), (world, [1]) | (Hello, 1), (world, 1) |
| Hello Hadoop | (Hello, 1), (Hadoop, 1) | (Hello, [1, 1]), (Hadoop, [1]) | (Hello, 2), (Hadoop, 1) |
| Hadoop world | (Hadoop, 1), (world, 1) | (Hadoop, [1, 1]), (world, [1, 1]) | (Hadoop, 2), (world, 2) |