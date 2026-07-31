#### Hadoop I/O

Hadoop Input/Output (I/O) module enables data ingestion and data export from Hadoop Distributed File System (HDFS) and other file systems. The module provides a set of APIs to read and write data from and to HDFS.

Here are the key points to understand about Hadoop I/O:

- Hadoop I/O supports different file formats, including text, sequence, and Avro.
- Hadoop I/O supports different compression codecs, including gzip, bzip2, and Snappy.
- Hadoop I/O APIs include FileInputFormat, which defines how to read data from a file system, and FileOutputFormat, which defines how to write data to a file system.
- Hadoop I/O also includes RecordReader and RecordWriter, which enable reading and writing of data in a specific format, such as text or sequence.
- Hadoop I/O supports splitting large input files into smaller chunks, which can be processed in parallel by different nodes in a Hadoop cluster.
- Hadoop I/O provides a set of utility classes, such as LineRecordReader and TextInputFormat, which simplify reading and writing of data in specific formats.
- Hadoop I/O also supports custom input and output formats, which enable users to define their own data formats and processing logic.

In summary, Hadoop I/O provides a flexible and scalable way to read and write data from and to Hadoop file systems. By leveraging Hadoop I/O APIs and utility classes, users can efficiently process large data sets and customize data processing logic to meet their specific needs.