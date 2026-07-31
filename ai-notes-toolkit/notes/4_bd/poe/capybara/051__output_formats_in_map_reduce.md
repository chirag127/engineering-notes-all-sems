#### Output Formats in Map Reduce

MapReduce is a programming model that is used to process large datasets in a distributed manner. It divides the input data into smaller chunks, processes them in parallel, and then combines the results to produce the final output. The output of a MapReduce job can be written in various formats. In this section, we will discuss some of the popular output formats in MapReduce.

1. Text Output Format
- The Text output format is the default format in MapReduce.
- It writes the key-value pairs in plain text format, where keys and values are separated by a tab character.
- The output is stored as a sequence of text files in the Hadoop Distributed File System(HDFS).

2. Sequence File Output Format
- The Sequence File output format is a binary file format that stores key-value pairs.
- It is an efficient format for MapReduce jobs that produce a large number of small files.
- The output is stored as a sequence of binary files in the Hadoop Distributed File System(HDFS).

3. Avro Output Format
- The Avro output format is a binary file format that stores data in a compact binary format.
- It supports schema evolution, which means that the schema of the data can change over time without breaking the existing applications.
- The output is stored as Avro files in the Hadoop Distributed File System(HDFS).

4. Parquet Output Format
- The Parquet output format is a columnar storage file format that is optimized for analytics workloads.
- It stores data in a compressed format, which makes it efficient for processing large datasets.
- The output is stored as Parquet files in the Hadoop Distributed File System(HDFS).

5. ORC Output Format
- The ORC output format is a columnar storage file format that is optimized for Hive-based data warehouses.
- It supports advanced compression algorithms and predicate pushdown, which makes it efficient for processing large datasets.
- The output is stored as ORC files in the Hadoop Distributed File System(HDFS).

In conclusion, MapReduce provides various output formats to store the results of a job. The choice of output format depends on the nature of the data and the requirements of the application. The above-discussed output formats are some of the popular formats in MapReduce.