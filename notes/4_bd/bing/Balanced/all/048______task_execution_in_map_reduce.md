#### Task execution in map reduce

- MapReduce is a programming model designed to process large amounts of data in parallel by dividing the job into several independent local tasks.
- Running the independent tasks locally reduces the network usage drastically.
- The complete execution process is controlled by two types of entities: a JobTracker and multiple TaskTrackers.
- The JobTracker acts like a master, responsible for scheduling, monitoring and coordinating the execution of the submitted job.
- The TaskTrackers act like slaves, each of them performing the map or reduce tasks assigned by the JobTracker.
- The map tasks take the input data and apply a user-defined function to each record, producing a set of intermediate key-value pairs.
- The reduce tasks take the intermediate key-value pairs and apply another user-defined function to aggregate them by key, producing the final output.
- The framework sorts the outputs of the maps, which are then input to the reduce tasks.
- Typically both the input and the output of the job are stored in a file-system, such as HDFS.
- The framework takes care of scheduling tasks, monitoring them and re-executing the failed tasks.

A simplified diagram of the task execution process is shown below:

```
    +-----------+    +-----------+    +-----------+
    | Input     |    | Map       |    | Reduce    |    | Output    |
    | Split 1   +--->+ Task 1    +--->+ Task 1    +--->+ Part 1    |
    +-----------+    +-----------+    +-----------+    +-----------+
    | Input     |    | Map       |    | Reduce    |    | Output    |
    | Split 2   +--->+ Task 2    +--->+ Task 2    +--->+ Part 2    |
    +-----------+    +-----------+    +-----------+    +-----------+
    | Input     |    | Map       |    | Reduce    |    | Output    |
    | Split 3   +--->+ Task 3    +--->+ Task 3    +--->+ Part 3    |
    +-----------+    +-----------+    +-----------+    +-----------+
```

Some advantages of using MapReduce are:

- It can handle large-scale data processing efficiently and reliably.
- It can exploit the parallelism and locality of the data.
- It can abstract the complexity of distributed computing from the user.
- It can be applied to a variety of problems, such as word count, inverted index, page rank, etc.

Some disadvantages of using MapReduce are:

- It may not be suitable for iterative or interactive applications, as it requires reading and writing data from the file-system for each job.
- It may not be optimal for complex data processing, such as joins, aggregations, etc., as it requires multiple map and reduce phases and intermediate data shuffling.
- It may not support advanced features, such as transactions, indexing, etc., as it is mainly a batch processing framework.

A mnemonic to remember the steps of MapReduce is:

- **M**ap: apply a function to each record
- **S**huffle: sort and group the intermediate key-value pairs
- **R**educe: aggregate the values by key
- **W**rite: store the final output to the file-system

A learning trick to understand the concept of MapReduce is to think of an analogy with a real-world scenario, such as counting the number of words in a book. For example:

- The book is divided into chapters, which are the input splits.
- Each chapter is assigned to a person, who is the map task.
- The person reads the chapter and writes down each word and its frequency on a piece of paper, which is the intermediate key-value pair.
- The pieces of paper are sorted and grouped by word, which is the shuffle phase.
- Another person collects the pieces of paper and sums up the frequencies for each word, which is the reduce task.
- The person writes down the final word count on another piece of paper, which is the output part.