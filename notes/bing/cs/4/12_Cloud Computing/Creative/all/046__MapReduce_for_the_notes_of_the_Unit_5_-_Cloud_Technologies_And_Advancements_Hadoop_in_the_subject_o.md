### MapReduce for the notes of the Unit 5 - Cloud Technologies And Advancements Hadoop in the subject of Cloud Computing

- MapReduce is a programming paradigm that enables massive scalability across hundreds or thousands of servers in a Hadoop cluster .
- MapReduce is the processing component and the heart of Apache Hadoop .
- MapReduce makes it possible to process large-scale data sets using multiple machines in the cluster, each with its own storage  .
- MapReduce consists of two separate and distinct tasks: Map and Reduce.
  - Map: The map function takes an input pair and produces a set of intermediate key/value pairs. The input and output types of the map can be (and often are) different from each other .
  - Reduce: The reduce function accepts an intermediate key and a set of values for that key. It merges together these values to form a possibly smaller set of values. The input types of the reduce can be different from the output type .
- MapReduce programs are written in various languages, such as Java, Ruby, Python, and C++.
- MapReduce works by splitting the input data into independent chunks that are processed by the map tasks in parallel. The framework sorts the outputs of the maps, which are then input to the reduce tasks. The framework takes care of scheduling tasks, monitoring them and re-executes the failed tasks .
- MapReduce can be used for various applications, such as word count, web log analysis, inverted index, join, matrix multiplication, etc .
- MapReduce has some advantages, such as:
  - It is simple and easy to use for programmers who do not have distributed systems expertise .
  - It is fault-tolerant and resilient to failures of nodes, tasks, or network .
  - It is scalable and can handle petabytes of data across thousands of nodes .
  - It is flexible and can handle structured, semi-structured, or unstructured data .
- MapReduce also has some disadvantages, such as:
  - It is not suitable for interactive or real-time queries, as it has high latency and overhead.
  - It is not efficient for complex data processing, such as graphs, iterative algorithms, or join operations.
  - It is not compatible with traditional SQL databases or tools, and requires a separate layer of abstraction, such as Hive or Pig.

A possible mnemonic to remember the steps of MapReduce is:

**M**any **M**achines **M**unch **D**ata, **S**ort **D**ata, **R**educe **D**ata.

A possible ascii diagram to illustrate the MapReduce process is:

```
Input data -> | Map | -> Intermediate key/value pairs -> | Sort | -> Key and list of values -> | Reduce | -> Output data
```