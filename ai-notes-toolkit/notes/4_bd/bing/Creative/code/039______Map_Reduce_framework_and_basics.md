#### Map Reduce framework and basics

Map Reduce is a programming model and an associated implementation for processing and generating large data sets. Users specify a map function that processes a key/value pair to generate a set of intermediate key/value pairs, and a reduce function that merges all intermediate values associated with the same intermediate key. Programs written in this functional style are automatically parallelized and executed on a large cluster of commodity machines. The run-time system takes care of the details of partitioning the input data, scheduling the program's execution across a set of machines, handling machine failures, and managing the required inter-machine communication. This allows programmers without any experience with parallel and distributed systems to easily utilize the resources of a large distributed system.

Here is a simple example of a Map Reduce program in Python that counts the number of occurrences of each word in a text file.

```python
# map function
def map(key, value):
  # key: document name
  # value: document contents
  for word in value.split():
    emit(word, 1)

# reduce function
def reduce(key, values):
  # key: a word
  # values: a list of counts
  result = 0
  for count in values:
    result += count
  emit(key, result)
```

The map function emits each word plus an associated count of occurrences (1). The reduce function sums together all counts emitted for a particular word. The output of the program is a list of (word, count) pairs.