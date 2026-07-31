OutputFormat is a class that describes the output-specification for a MapReduce job. It provides the RecordWriter implementation to be used to write the output files of the job to a FileSystem. There are different types of OutputFormat in MapReduce, such as TextOutputFormat, SequenceFileOutputFormat, MapFileOutputFormat, DBOutputFormat, etc. Each type of OutputFormat has its own way of formatting and storing the output data.

A diagram for the output formats in MapReduce can be drawn as follows:

#### Output formats in MapReduce

```
+-----------------+     +-----------------+     +-----------------+
| TextOutputFormat|     |SequenceFileOutputFormat|     |MapFileOutputFormat|
+-----------------+     +-----------------+     +-----------------+
| Writes text files|     |Writes sequence files|     |Writes map files|
| with key-value pairs|  |with binary key-value pairs|  |with sorted key-value pairs|
| separated by tabs|     |compressed by codecs|     |indexed by keys|
| Example:         |     |Example:           |     |Example:          |
| key1\tvalue1     |     |<binary data>      |     |<key1><value1>    |
| key2\tvalue2     |     |<binary data>      |     |<key2><value2>    |
+-----------------+     +-----------------+     +-----------------+
         |                       |                       |
         |                       |                       |
         +-----------------------+-----------------------+
                                 |
                                 v
                         +-----------------+
                         |  DBOutputFormat |
                         +-----------------+
                         | Writes records  |
                         | to a relational |
                         | database table  |
                         | Example:        |
                         | INSERT INTO     |
                         | table (key,value)|
                         | VALUES (key1,value1)|
                         | VALUES (key2,value2)|
                         +-----------------+
```