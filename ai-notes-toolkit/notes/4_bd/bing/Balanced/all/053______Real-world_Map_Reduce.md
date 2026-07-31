#### Real-world Map Reduce

- Map Reduce is a programming model and an associated implementation for processing and generating large data sets with a parallel, distributed algorithm on a cluster.
- The model is inspired by the map and reduce functions commonly used in functional programming, although their purpose in the Map Reduce framework is not the same as their original forms.
- The key contributions of the Map Reduce framework are not the actual map and reduce functions, but the scalability and fault-tolerance achieved for a variety of applications by optimizing the execution engine once.
- As such, a single Map Reduce program written in Java can be run unmodified on clusters of thousands of machines.
- The basic idea of Map Reduce is to split the input data into independent chunks that are processed by the map functions in a completely parallel manner.
- The framework sorts the outputs of the maps, which are then input to the reduce functions.
- Typically both the input and the output of the job are stored in a distributed file system.
- The framework takes care of scheduling tasks, monitoring them and re-executes the failed tasks.
- The Map Reduce framework consists of a single master JobTracker and one slave TaskTracker per cluster-node.
- The master is responsible for scheduling the jobs' component tasks on the slaves, monitoring them and re-executing the failed tasks.
- The slaves execute the tasks as directed by the master.
- The application is divided into two parts: the map function and the reduce function.
- The map function takes an input pair and produces a set of intermediate key/value pairs.
- The Map Reduce library groups together all intermediate values associated with the same intermediate key I and passes them to the reduce function.
- The reduce function accepts an intermediate key I and a set of values for that key. It merges together these values to form a possibly smaller set of values.
- Typically just zero or one output value is produced per reduce invocation.
- The intermediate values are supplied to the user's reduce function via an iterator. This allows us to handle lists of values that are too large to fit in memory.
- A simple example of Map Reduce is counting the number of occurrences of each word in a large collection of documents.
- The map function emits each word plus an associated count of occurrences, while the reduce function sums together all counts emitted for a particular word.
- The following is a pseudo-code example of the map and reduce functions for this application:

```
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

- Some advantages of Map Reduce are:
  - It is simple and easy to use for a wide range of applications.
  - It is scalable and fault-tolerant, as it can handle large data sets and failures of machines or tasks.
  - It is flexible and extensible, as it allows users to define their own custom data types, partitioning functions, combiners, etc.
  - It is efficient and optimized, as it performs local computation and reduces network traffic by using a distributed file system.
- Some disadvantages of Map Reduce are:
  - It is not suitable for applications that require complex data structures or algorithms, such as graphs, matrices, etc.
  - It is not efficient for applications that require frequent communication or synchronization between tasks, such as iterative algorithms, online queries, etc.
  - It is not expressive enough for applications that require higher-level abstractions, such as SQL, streaming, etc.
- Some examples of real-world applications that use Map Reduce are:
  - Web indexing: generating an inverted index from a large collection of web pages.
  - PageRank: computing the importance of web pages based on the link structure.
  - Machine learning: training and testing classifiers, clustering, etc.
  - Data mining: finding frequent itemsets, association rules, etc.
  - Text processing: word count, sentiment analysis, etc.
  - Image processing: face detection, feature extraction, etc.
  - Bioinformatics: genome sequencing, alignment, etc.