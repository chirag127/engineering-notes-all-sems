### Map Reduce

- MapReduce is a framework for processing parallelizable problems across large datasets using a large number of computers (nodes), collectively referred to as a cluster or a grid.
- MapReduce is also the name of a programming model or pattern that enables massive scalability across hundreds or thousands of servers in a Hadoop cluster.
- The term "MapReduce" refers to two separate and distinct tasks that Hadoop programs perform:
  - The first is the map job, which takes a set of data and converts it into another set of data, where individual elements are broken down into tuples (key/value pairs).
  - The second is the reduce job, which takes the output from the map job and combines those tuples into a smaller set of tuples.
- The map and reduce functions are written by the user and can be customized to perform different types of processing on the data.
- The MapReduce framework handles the distribution of data and tasks across the nodes, the coordination of the execution, the handling of failures and errors, and the aggregation of the results.
- MapReduce is suitable for processing large volumes of unstructured or semi-structured data, such as text, images, audio, video, log files, etc.
- MapReduce can be used for various applications, such as word count, web indexing, data mining, machine learning, sentiment analysis, etc.

#### Advantages of MapReduce

- MapReduce is scalable, as it can run on thousands of nodes and handle petabytes of data.
- MapReduce is fault-tolerant, as it can recover from node failures and data loss by replicating the data and tasks across the cluster.
- MapReduce is simple, as it abstracts the complexity of distributed computing from the user and provides a high-level interface for writing the map and reduce functions.
- MapReduce is flexible, as it can process any type of data, regardless of its format, structure, or schema.
- MapReduce is efficient, as it minimizes the network traffic by moving the computation to the data, rather than the other way around.

#### Disadvantages of MapReduce

- MapReduce is not suitable for interactive or real-time queries, as it has a high latency due to the batch processing nature.
- MapReduce is not optimal for complex or iterative algorithms, as it requires multiple map and reduce jobs to be chained together, which increases the overhead and reduces the performance.
- MapReduce is not compatible with traditional relational databases or SQL, as it does not support joins, aggregations, or transactions.
- MapReduce is not easy to debug or test, as it involves distributed and parallel execution, which makes it hard to trace the errors and monitor the progress.

#### Example of MapReduce

- Suppose we want to count the number of occurrences of each word in a large text file using MapReduce.
- The input data is the text file, which is split into smaller chunks and distributed across the nodes in the cluster.
- The map function takes each chunk of text and emits a key/value pair for each word, where the key is the word and the value is 1.
- The output of the map function is shuffled and sorted by the key, and then sent to the reduce function.
- The reduce function takes all the key/value pairs for a given word and sums up the values, resulting in a final count for that word.
- The output of the reduce function is the final word count for the entire text file.

#### ASCII Diagram of MapReduce

```
    Input Data
    +-----------------+
    | This is a text  |
    | file that has   |
    | some words in   |
    | it.             |
    +-----------------+

    Map Function
    +-----------------+    +-----------------+
    | This is a text  |    | (This, 1)       |
    | file that has   | -> | (is, 1)         |
    | some words in   |    | (a, 1)          |
    | it.             |    | (text, 1)       |
    +-----------------+    | (file, 1)       |
                           | (that, 1)       |
                           | (has, 1)        |
                           | (some, 1)