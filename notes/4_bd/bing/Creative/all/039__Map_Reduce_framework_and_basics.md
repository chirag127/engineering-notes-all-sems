#### Map Reduce framework and basics

- Map Reduce is a programming model and an associated implementation for processing and generating large data sets with a parallel, distributed algorithm on a cluster.
- The model is inspired by the map and reduce functions commonly used in functional programming, although their purpose in the Map Reduce framework is not the same as in their original forms.
- The key idea is to split the input data set into independent chunks that are processed by the map tasks in a completely parallel manner. The framework sorts the outputs of the maps, which are then input to the reduce tasks. Typically both the input and the output of the job are stored in a file system. The framework takes care of scheduling tasks, monitoring them and re-executing the failed tasks.
- The Map Reduce framework consists of a single master JobTracker and one slave TaskTracker per cluster-node. The master is responsible for scheduling the jobs' component tasks on the slaves, monitoring them and re-executing the failed tasks. The slaves execute the tasks as directed by the master.
- The Map Reduce framework operates exclusively on <key, value> pairs, that is, the framework views the input to the job as a set of <key, value> pairs and produces a set of <key, value> pairs as the output of the job, conceivably of different types.
- The Map Reduce framework consists of two types of tasks: map and reduce.
  - The map task takes a set of <key, value> pairs, processes each pair, and generates zero or more output pairs. The input and output types of the map can be (and often are) different from each other.
  - The reduce task takes all the pairs with the same key as input and merges them together using the reduce function specified by the user. The output of the reduce is zero or more pairs with the same key type as the input but usually with a different value type.
- The Map Reduce framework guarantees that the input to every reducer is sorted by key. The process by which the system performs the sort and transfers the map outputs to the reducers as inputs is known as the shuffle.
- The number of map tasks and reduce tasks for each job is usually specified by the user. The number of map tasks is usually driven by the total size of the inputs, that is, the total number of blocks of the input files. The number of reduce tasks is usually a small multiple of the number of available nodes, although it can be set to one to avoid the reduce step.
- A simple example of Map Reduce is the word count problem, where the input is a set of documents and the output is a list of words and their frequencies in the documents. The map function emits a <word, 1> pair for each word occurrence in the document. The reduce function sums up the values for each word and emits a <word, total count> pair.
- A possible pseudocode for the word count problem is:

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

- A possible ascii diagram for the word count problem is:

```
Input file 1: "This is a test"
Input file 2: "Another test"

Map tasks:

map(file1, "This is a test") -> ("This", 1), ("is", 1), ("a", 1), ("test", 1)
map(file2, "Another test") -> ("Another", 1), ("test", 1)

Shuffle:

("This", 1) -> reduce task 1
("is", 1) -> reduce task 2
("a", 1) -> reduce task 3
("test", 1) -> reduce task 4
("Another", 1) -> reduce task 1
("test", 1) -> reduce task 4

Reduce tasks:

reduce("This", [1]) -> ("This", 1)
reduce("is", [1]) -> ("is", 1)
reduce("a", [1]) -> ("a", 1)
reduce("test", [1, 1]) -> ("test", 2)
reduce("Another", [1]) -> ("Another", 1)

Output:

("This", 1)
("is", 1)
("a", 1)
("test", 2)
("Another", 1)
```

- Some advantages of Map Reduce are:
  - It is simple and