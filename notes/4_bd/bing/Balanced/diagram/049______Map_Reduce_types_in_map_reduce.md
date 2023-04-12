MapReduce is a programming model for processing large-scale data sets in parallel and distributed manner. It consists of two types of functions: map and reduce. The map function takes a key-value pair as input and produces a list of intermediate key-value pairs as output. The reduce function takes an intermediate key and a list of values associated with that key as input and produces a list of final key-value pairs as output. The MapReduce framework handles the partitioning, shuffling, sorting and aggregation of the intermediate and final results.

There are different types of input and output formats for MapReduce jobs, depending on the data source and the desired output format. Some of the common input formats are:

- TextInputFormat: reads lines of text files and splits them by newline characters. The key is the byte offset of the line and the value is the line itself.
- KeyValueInputFormat: reads lines of text files and splits them by a separator character (default is tab). The key is the first part of the line and the value is the rest of the line.
- SequenceFileInputFormat: reads binary files that store sequences of key-value pairs in a compressed and serialized format. The key and value are the same as the ones stored in the file.

Some of the common output formats are:

- TextOutputFormat: writes key-value pairs as lines of text files. The key and value are separated by a separator character (default is tab).
- SequenceFileOutputFormat: writes key-value pairs as binary files in a compressed and serialized format. The key and value are the same as the ones written to the file.
- NullOutputFormat: does not write any output to the file system. This can be useful for testing or benchmarking purposes.

A diagram of the MapReduce types and formats is shown below:

#### MapReduce types and formats

```
+----------------+       +----------------+       +----------------+
|  Input Format  |       |  Output Format |       |  Output Format |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  Key1  Value1  |       |  Key3  Value3  |       |  Key3  Value3  |
|  Key1  Value1  |       |  Key3  Value3  |       |  Key3  Value3  |
|  Key1  Value1  |       |  Key3  Value3  |       |  Key3  Value3  |
|  Key1  Value1  |       |  Key3  Value3  |       |  Key3  Value3  |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       v                        v                        v
+----------------+       +----------------+       +----------------+
|     Mapper     |       |    Reducer     |       |    Reducer     |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  map(Key1,Value1)      |  reduce(Key2,list(Value2))               |
|  -> list(Key2,Value2)  |  -> list(Key3,Value3)    |  -> list(Key3,Value3)    |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       v                        v                        v
+----------------+       +----------------+       +----------------+
|  Intermediate  |       |  Intermediate  |       |  Intermediate  |
|  Key-Value     |       |  Key-Value     |       |  Key-Value     |
|  Pairs         |       |  Pairs         |       |  Pairs         |
+----------------+       +----------------

```
