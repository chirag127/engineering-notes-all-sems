### Map Reduce

- Map Reduce is a programming model and an associated implementation for processing and generating large data sets with a parallel, distributed algorithm on a cluster.
- The model is inspired by the map and reduce functions commonly used in functional programming, although their purpose in the Map Reduce framework is not the same as in their original forms.
- The key idea is to split the input data set into independent chunks that are processed by the map tasks in a completely parallel manner. The framework sorts the outputs of the maps, which are then input to the reduce tasks. Typically both the input and the output of the job are stored in a file-system. The framework takes care of scheduling tasks, monitoring them and re-executes the failed tasks.
- The Map Reduce model can be applied to many real-world problems, such as web indexing, data mining, machine learning, image processing, etc.
- The advantages of Map Reduce are:
  - It is simple and easy to use, as the programmer only needs to specify the map and reduce functions, and the framework handles the rest.
  - It is scalable and fault-tolerant, as it can run on thousands of nodes and automatically recover from node failures.
  - It is efficient and flexible, as it can exploit the locality of data and optimize the network communication, and it can support various data formats and user-defined functions.
- The disadvantages of Map Reduce are:
  - It is not suitable for interactive or iterative applications, as it incurs high overhead for each job launch and data shuffling.
  - It is not optimal for complex data processing, as it may require multiple Map Reduce jobs to be chained together, which can increase the latency and reduce the performance.
  - It is not expressive enough for some advanced operations, such as joins, aggregations, or graph algorithms, which may require custom solutions or extensions.

- A simple example of Map Reduce is word count, which counts the number of occurrences of each word in a large collection of documents. The map function emits a key-value pair for each word, where the key is the word and the value is 1. The reduce function sums up the values for each word and emits the final count. The pseudo-code for the map and reduce functions is:

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
  for value in values:
    result += value
  emit(key, result)
```

- A possible mnemonic to remember the Map Reduce model is:

  - Map: Munch and Produce
  - Reduce: Reorganize and Emit

- A possible learning trick to understand the Map Reduce model is to use an analogy of a factory. Imagine that the input data set is a pile of raw materials that need to be processed into finished products. The map tasks are like workers who take a piece of raw material and transform it into an intermediate product, such as a part or a component. The reduce tasks are like machines that take the intermediate products and assemble them into the final products, such as a car or a phone. The framework is like the manager who assigns the tasks to the workers and machines, monitors their progress, and handles any problems.