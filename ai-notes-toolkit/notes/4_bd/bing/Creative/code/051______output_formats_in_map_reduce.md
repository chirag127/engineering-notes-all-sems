#### Output formats in map reduce

Output formats in map reduce are the classes that define how the output files of a map reduce job are written and stored in a file system. The output format also provides the record writer implementation that is used to write the output records of the map and reduce tasks. The output format can be specified by the user using the `setOutputFormatClass` method of the `Job` class.

There are different types of output formats in map reduce, such as:

- `TextOutputFormat`: This is the default output format that writes plain text files as output. Each record is a line of text that consists of the key and the value separated by a tab character. The keys and values are converted to strings using their `toString` methods.
- `SequenceFileOutputFormat`: This output format writes sequence files as output. Sequence files are binary files that store key-value pairs in a compressed and serialized format. They are suitable for storing large amounts of data that can be processed efficiently by map reduce.
- `SequenceFileAsBinaryOutputFormat`: This output format is similar to `SequenceFileOutputFormat`, but it writes the keys and values as raw bytes instead of using their `Writable` implementations. This can save space and time when the keys and values are already in a binary format.
- `MapFileOutputFormat`: This output format writes map files as output. Map files are a special type of sequence files that support random access to the records by using an index file. They are useful for storing data that needs to be looked up frequently by map reduce or other applications.
- `MultipleOutputs`: This output format allows writing to multiple output files from a single map reduce job. The output files can have different formats and names based on the keys or values of the output records. This is useful for partitioning the output data into different categories or formats.
- `LazyOutputFormat`: This output format prevents creating empty output files for map reduce tasks that do not produce any output records. This can save space and time when the output data is sparse or unevenly distributed.
- `DBOutputFormat`: This output format writes the output records to a relational database table using JDBC. The output table schema and the connection parameters can be specified by the user. This is useful for exporting data from map reduce to a database.