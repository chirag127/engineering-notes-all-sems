
#### Input Formats in Map Reduce

1. Text Input Format: This is the default input format used in MapReduce. It reads data line by line, and each line is divided into key-value pairs. The key is the offset of the line, and the value is the content of the line.

2. Key-Value Input Format: This input format is used to read data in the form of key-value pairs. It is used to process data from NoSQL databases like HBase, Cassandra, etc.

3. Sequence File Input Format: This input format is used to read data from sequence files. It is used to process data from Hadoop Distributed File System (HDFS).

4. NLine Input Format: This input format is used to read data from multiple lines. It is used to process multiple lines of data at once.

5. DBInputFormat: This input format is used to read data from databases. It is used to process data from relational databases like Oracle, MySQL, etc.

6. XML Input Format: This input format is used to read data from XML files. It is used to process data from XML documents.

7. Multiple Input Format: This input format is used to read data from multiple sources. It is used to process data from multiple sources like HDFS, HBase, Cassandra, etc.

Mnemonics:

- Text Input Format: TIF
- Key-Value Input Format: KVIF
- Sequence File Input Format: SFIF
- NLine Input Format: NLIF
- DBInputFormat: DBIF
- XML Input Format: XIF
- Multiple Input Format: MIF