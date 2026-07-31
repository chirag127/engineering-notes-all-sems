OutputFormat is a class that describes the output specification for a MapReduce job. It provides the RecordWriter implementation to write the output files of the job to a FileSystem. There are different types of OutputFormat, such as TextOutputFormat, SequenceFileOutputFormat, MapFileOutputFormat, etc. Each type has its own way of formatting the output records and files.

A diagram for output formats in MapReduce can be drawn as follows:

#### Output formats in MapReduce

```
+-----------------+    +-----------------+    +-----------------+
| TextOutputFormat|    |SequenceFileOutputFormat|    |MapFileOutputFormat|
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
| Writes text     |    | Writes sequence |    | Writes map      |
| files with      |    | files with      |    | files with      |
| key-value pairs |    | key-value pairs |    | key-value pairs |
| separated by    |    | in binary format|    | in binary format|
| tabs            |    |                 |    | and an index    |
|                 |    |                 |    | file for faster |
|                 |    |                 |    | lookup          |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         +----------------------+----------------------+
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                +-----------------+
                                | OutputFormat    |
                                +-----------------+
                                |                 |
                                | Provides the    |
                                | RecordWriter    |
                                | implementation  |
                                | to write the    |
                                | output files of |
                                | the job         |
                                |                 |
                                +-----------------+
```