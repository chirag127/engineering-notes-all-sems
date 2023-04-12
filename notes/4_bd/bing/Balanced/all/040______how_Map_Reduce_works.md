#### How Map Reduce works

- Map Reduce is a programming model and an associated implementation for processing and generating large data sets with a parallel, distributed algorithm on a cluster.
- The model is inspired by the map and reduce functions commonly used in functional programming, although their purpose in the Map Reduce framework is not the same as their original forms.
- The key idea is to split the input data into independent chunks that are processed by the map tasks in a completely parallel manner. The framework sorts the outputs of the maps, which are then input to the reduce tasks. Typically both the input and the output of the job are stored in a file-system. The framework takes care of scheduling tasks, monitoring them and re-executes the failed tasks.
- The Map Reduce framework consists of a single master JobTracker and one slave TaskTracker per cluster-node. The master is responsible for scheduling the jobs' component tasks on the slaves, monitoring them and re-executing the failed tasks. The slaves execute the tasks as directed by the master.
- The Map Reduce framework operates exclusively on <key, value> pairs, that is, the framework views the input to the job as a set of <key, value> pairs and produces a set of <key, value> pairs as the output of the job, conceivably of different types.
- The Map Reduce framework consists of two phases: Map and Reduce. Each phase has key-value pairs as input and output, the types of which may be chosen by the programmer. The programmer also specifies two functions: the map function and the reduce function.
- Map: The master node takes the input, divides it into smaller sub-problems, and distributes them to worker nodes. A worker node may do this again in turn, leading to a multi-level tree structure. The worker node processes the smaller problem, and passes the answer back to its master node.
- Reduce: The master node then collects the answers to all the sub-problems and combines them in some way to form the output – the answer to the problem it was originally trying to solve.
- The following is a simple example of Map Reduce, where the input is a set of documents and the output is the number of times each word occurs in the documents.

```
map(String key, String value):
  // key: document name
  // value: document contents
  for each word w in value:
    emit(w, 1)

reduce(String key, Iterator values):
  // key: a word
  // values: a list of counts
  int result = 0
  for each v in values:
    result += v
  emit(key, result)
```

- The map function emits each word plus an associated count of occurrences (1). The reduce function sums together all counts emitted for a particular word. The output is a list of <word, total count> pairs.
- The following is a possible ASCII diagram of the Map Reduce process for the word count example.

```
Input: <doc1, "This is a sample document">, <doc2, "Another document with some words">

Map phase:

doc1 -> map -> <This, 1>, <is, 1>, <a, 1>, <sample, 1>, <document, 1>
doc2 -> map -> <Another, 1>, <document, 1>, <with, 1>, <some, 1>, <words, 1>

Shuffle and sort phase:

<This, 1> -> reduce
<is, 1> -> reduce
<a, 1> -> reduce
<sample, 1> -> reduce
<document, 1>, <document, 1> -> reduce
<Another, 1> -> reduce
<with, 1> -> reduce
<some, 1> -> reduce
<words, 1> -> reduce

Reduce phase:

<This, 1> -> reduce -> <This, 1>
<is, 1> -> reduce -> <is, 1>
<a, 1> -> reduce -> <a, 1>
<sample, 1> -> reduce -> <sample, 1>
<document, 1>, <document, 1> -> reduce -> <document, 2>
<Another, 1> -> reduce -> <Another, 1>
<with, 1> -> reduce -> <with, 1>
<some, 1> -> reduce -> <some, 1>
<words, 1> -> reduce -> <words, 1>

Output: <This, 1>, <is, 1>, <a, 1>, <sample, 1>, <document, 2>, <Another, 1>, <with,

```
