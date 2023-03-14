Hadoop streaming is a utility that allows you to create and run MapReduce jobs with any executable or script as the mapper and/or the reducer. It works by launching the executable or script as a separate process for each mapper or reducer task, and feeding the input and output data through standard input and output streams. The utility will also monitor the progress and status of the job until it completes.

#### Hadoop streaming diagram

The following diagram illustrates the basic architecture of a Hadoop streaming job:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Input files   |     |  Output files  |     |  Output files  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      ^                      ^
       |                      |                      |
       v                      |                      |
+----------------+            |                      |
|                |            |                      |
|  InputFormat   |            |                      |
|                |            |                      |
+----------------+            |                      |
       |                      |                      |
       |                      |                      |
       v                      |                      |
+----------------+            |                      |
|                |            |                      |
|  RecordReader  |            |                      |
|                |            |                      |
+----------------+            |                      |
       |                      |                      |
       |                      |                      |
       v                      |                      |
+----------------+            |                      |
|                |            |                      |
|  Mapper        |            |                      |
|                |            |                      |
+----------------+            |                      |
       |                      |                      |
       |                      |                      |
       v                      |                      |
+----------------+            |                      |
|                |            |                      |
|  Partitioner   |            |                      |
|                |            |                      |
+----------------+            |                      |
       |                      |                      |
       |                      |                      |
       v                      |                      |
+----------------+            |                      |
|                |            |                      |
|  Sort/Shuffle  |            |                      |
|                |            |                      |
+----------------+            |                      |
       |                      |                      |
       |                      |                      |
       v                      |                      |
+----------------+            |                      |
|                |            |                      |
|  Reducer       |            |                      |
|                |            |                      |
+----------------+            |                      |
       |                      |                      |
       |                      |                      |
       v                      |                      |
+----------------+            |                      |
|                |            |                      |
|  RecordWriter  |            |                      |
|                |            |                      |
+----------------+            |                      |
       |                      |                      |
       |                      |                      |
       v                      |                      |
+----------------+            |                      |
|                |            |                      |
|  OutputFormat  |            |                      |
|                |            |                      |
+----------------+            |                      |
       |                      |                      |
       |                      |                      |
       v                      |                      |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Output files  |     |  Output files  |     |  Output files  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```

In this diagram, the boxes represent the components of the MapReduce framework, and the arrows represent the data flow between them. The input and output files are stored in HDFS, and the input format and output format determine how the files are split and written. The record reader and record writer are responsible for converting the input and output data into key-value pairs. The mapper and reducer are the user-defined functions that process the key-value pairs. The partitioner and sort/shuffle are the internal mechanisms that distribute and sort the intermediate data among the reducers. The output files of the reducers are the final result of the MapReduce job.