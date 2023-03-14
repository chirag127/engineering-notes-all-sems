#### How Map Reduce works

- Map Reduce is a programming model and an associated implementation for processing and generating large data sets with a parallel, distributed algorithm on a cluster.
- The model is inspired by the map and reduce functions commonly used in functional programming, although their purpose in the Map Reduce framework is not the same as in their original forms.
- The key idea is to split the input data set into independent chunks that are processed by the map tasks in a completely parallel manner. The framework sorts the outputs of the map tasks, which are then input to the reduce tasks. Typically both the input and the output of the job are stored in a distributed file system. The framework takes care of scheduling tasks, monitoring them and re-executes the failed tasks.
- The Map Reduce framework consists of a single master JobTracker and one slave TaskTracker per cluster-node. The master is responsible for scheduling the jobs' component tasks on the slaves, monitoring them and re-executing the failed tasks. The slaves execute the tasks as directed by the master.
- The Map Reduce framework operates exclusively on <key, value> pairs, that is, the framework views the input to the job as a set of <key, value> pairs and produces a set of <key, value> pairs as the output of the job, conceivably of different types.
- The Map Reduce framework consists of two phases: map and reduce. The map phase takes an input pair and produces a set of intermediate key/value pairs. The Map Reduce framework groups together all intermediate values associated with the same intermediate key I and passes them to the reduce function. The reduce function accepts an intermediate key I and a set of values for that key. It merges together these values to form a possibly smaller set of values. Typically just zero or one output value is produced per reduce invocation. The intermediate values are supplied to the user's reduce function via an iterator. This allows us to handle lists of values that are too large to fit in memory.
- A simple example of Map Reduce is word count, where the input is a set of documents and the output is a list of words and their frequencies. The map function emits a key/value pair for each word in the document, where the key is the word and the value is 1. The reduce function sums up the values for each word and emits a single key/value pair with the word and its frequency.

Here is a pseudocode example of the map and reduce functions for word count:

```python
# map function
def map(document):
  for word in document.split():
    emit(word, 1)

# reduce function
def reduce(word, values):
  sum = 0
  for value in values:
    sum += value
  emit(word, sum)
```

Here is a simple ASCII diagram of the Map Reduce process for word count:

```
Input: document1, document2, document3

Map phase:

document1 -> map -> (hello, 1), (world, 1), (hello, 1)
document2 -> map -> (goodbye, 1), (world, 1)
document3 -> map -> (hello, 1), (goodbye, 1), (goodbye, 1)

Shuffle and sort phase:

(hello, 1), (hello, 1), (hello, 1) -> (hello, [1, 1, 1])
(world, 1), (world, 1) -> (world, [1, 1])
(goodbye, 1), (goodbye, 1), (goodbye, 1) -> (goodbye, [1, 1, 1])

Reduce phase:

(hello, [1, 1, 1]) -> reduce -> (hello, 3)
(world, [1, 1]) -> reduce -> (world, 2)
(goodbye, [1, 1, 1]) -> reduce -> (goodbye, 3)

Output: (hello, 3), (world, 2), (goodbye, 3)
```

Some advantages of Map Reduce are:

- It can handle large-scale data processing in a distributed and fault-tolerant manner.
- It can exploit the locality of data, minimizing the network traffic and improving the performance.
- It can abstract the complexity of parallelization, synchronization, and fault tolerance from the programmers.
- It can be easily scaled up or down by adding or removing nodes from the cluster.

Some disadvantages of Map Reduce are:

- It is not suitable for interactive or real-time applications, as it has high latency and overhead.
- It is not efficient for complex data processing that requires multiple iterations or data-dependent control flow, as it involves a lot of disk I/O and network communication.
- It