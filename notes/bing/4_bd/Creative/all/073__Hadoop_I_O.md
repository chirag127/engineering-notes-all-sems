#### Hadoop I/O

- Hadoop I/O is a set of primitives for data input and output in Hadoop. It includes techniques such as data integrity, compression, serialization, and file formats that are suitable for large-scale data processing.
- Data integrity is the ability to detect and correct errors in data. Hadoop uses checksums to ensure data integrity at different levels, such as in HDFS blocks, MapReduce shuffle transfers, and SequenceFiles. Checksums are stored separately from data, and are verified by Hadoop before reading or writing data.
- Compression is the technique of reducing the size of data by removing redundancy. Compression can save disk space, network bandwidth, and I/O time. Hadoop supports various compression codecs, such as Gzip, Bzip2, Snappy, and LZO. Compression can be applied at different levels, such as in HDFS files, MapReduce intermediate outputs, and SequenceFiles. Compression can be either splittable or non-splittable, depending on whether the compressed data can be split into independent chunks for parallel processing.
- Serialization is the process of converting data structures into a binary format that can be stored or transmitted. Serialization is used by Hadoop to transfer data between nodes, and to store data in files. Hadoop has its own serialization framework, called Writable, that provides a compact and fast way of serializing data for MapReduce. Writable classes implement the Writable interface, which defines two methods: readFields() and write(). Hadoop provides a number of built-in Writable classes, such as IntWritable, Text, and NullWritable, and also allows users to define their own custom Writable classes.
- File formats are the ways of organizing data in files. Hadoop supports various file formats, such as plain text, binary, and structured. Some of the common file formats used by Hadoop are:

  - SequenceFile: A binary file format that stores key-value pairs in a sequence. SequenceFiles can be compressed, split, and indexed. They are suitable for storing intermediate outputs of MapReduce, or small files that are otherwise inefficient to store in HDFS.
  - MapFile: A directory of files that stores key-value pairs in a sorted order. MapFiles are built on top of SequenceFiles, and provide random access to the values by using an index file. They are suitable for storing lookup tables or inverted indexes that are used by MapReduce or other applications.
  - Avro: A binary file format that stores data in a schema-based way. Avro files have a self-describing schema that is stored with the data, and can be read by any program that supports Avro. Avro files can be compressed, split, and processed in parallel. They are suitable for storing complex or evolving data structures that are used by MapReduce or other applications.

- Some of the advantages of using Hadoop I/O are:

  - It provides a consistent and reliable way of handling data in Hadoop.
  - It optimizes the performance and efficiency of data processing in Hadoop.
  - It supports various types and formats of data that are common in big data scenarios.
  - It allows users to customize and extend the data I/O functionality according to their needs.

- Some of the disadvantages of using Hadoop I/O are:

  - It requires users to learn and use the specific APIs and conventions of Hadoop I/O.
  - It may not be compatible or interoperable with other data I/O frameworks or tools that are outside of Hadoop.
  - It may not support some of the advanced or specialized features or requirements of data I/O that are specific to certain domains or applications.