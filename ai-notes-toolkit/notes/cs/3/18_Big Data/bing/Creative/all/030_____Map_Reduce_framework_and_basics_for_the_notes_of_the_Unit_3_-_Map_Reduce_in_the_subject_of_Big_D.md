# Map Reduce Framework and Basics

Map Reduce is a programming model and an associated implementation for processing and generating large data sets with a parallel, distributed algorithm on a cluster.

## Basic Concepts

- A Map Reduce program is composed of a **map** function, which performs filtering and sorting, and a **reduce** function, which performs a summary operation.
- The input and output of both functions are key-value pairs of arbitrary types.
- The Map Reduce framework automatically parallelizes the computation across multiple machines and handles the details of partitioning the input data, scheduling the program's execution, and coping with machine failures.
- The framework also provides a library of common mappers, reducers, and partitioners for convenience.

## Execution Overview

- The Map Reduce framework operates on <key, value> pairs, where the key and value types may be specified by the user.
- The framework takes an input set of <key, value> pairs and produces an output set of <key, value> pairs.
- The user specifies the map and reduce functions, and optionally the combiner and partitioner functions.
- The execution of a Map Reduce program proceeds as follows:

  - The framework splits the input data into **M** pieces of typically 64 MB each and assigns one map task to each piece. Each map task reads the input data and applies the user-defined map function to each <key, value> pair, producing a set of intermediate <key, value> pairs. The intermediate pairs are buffered in memory and periodically written to local disk, partitioned into **R** regions by a user-defined partitioning function. The locations of these buffered pairs on the local disk are passed to the master, which is responsible for scheduling the reduce tasks.
  - The master assigns one reduce task to each partition, and notifies the worker nodes of the locations of the intermediate pairs for that partition. Each reduce task reads the intermediate pairs from the local disks of the map workers and sorts them by the intermediate keys. The sorting is needed because the framework groups together all intermediate pairs with the same key and passes them to the user's reduce function. The user-defined reduce function then accepts an intermediate key and a set of values for that key, and merges the values to form a smaller set of values. Typically, zero or one output value is produced per reduce invocation. The intermediate values are supplied to the user's reduce function via an iterator. This allows the framework to handle lists of values that are too large to fit in memory.
  - The output of the reduce function is appended to a final output file for the corresponding partition. After all map and reduce tasks have completed, the output of the reduce tasks is available as the output of the program.

## Example: Word Count

- A simple example of a Map Reduce program is counting the number of occurrences of each word in a large collection of documents.
- The map function emits each word plus an associated count of occurrences (usually 1). The reduce function sums together all counts emitted for a particular word.
- The pseudo-code for the map and reduce functions are as follows:

  ```python
  map(String key, String value):
    // key: document name
    // value: document contents
    for each word w in value:
      emit (w, 1)

  reduce(String key, Iterator values):
    // key: a word
    // values: a list of counts
    int result = 0
    for each v in values:
      result += v
    emit (key, result)
  ```

- The combiner function is the same as the reduce function in this case, since it can combine the counts for each word locally and emit the partial sums to the reduce tasks.
- The partitioner function can use a simple hash function to distribute the intermediate pairs among the reduce tasks.