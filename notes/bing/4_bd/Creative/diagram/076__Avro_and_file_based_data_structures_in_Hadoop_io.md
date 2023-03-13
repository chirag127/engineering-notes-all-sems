Avro is a data serialization framework that is widely used in Hadoop and its ecosystem. It stores data along with its schema in a binary format that is compact and efficient. Avro data files are line-oriented, meaning that each row in the file is stored consecutively. Avro data files support compression and are splittable, which makes them suitable for MapReduce data input format.

File-based data structures in Hadoop are data structures that are stored as files in HDFS. They are used to store and process large amounts of data in a distributed manner. Some examples of file-based data structures are sequential files, map files, and Avro data files.

The following diagram illustrates the basic architecture of a file-based data structure in Hadoop:

```
+-----------------+    +-----------------+    +-----------------+
|  File System    |    |  File System    |    |  File System    |
|  (HDFS)         |    |  (HDFS)         |    |  (HDFS)         |
+-----------------+    +-----------------+    +-----------------+
|  Data Node      |    |  Data Node      |    |  Data Node      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|  File Block     |    |  File Block     |    |  File Block     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|  File Record    |    |  File Record    |    |  File Record    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|  File Format    |    |  File Format    |    |  File Format    |
|  (Avro, etc.)   |    |  (Avro, etc.)   |    |  (Avro, etc.)   |
+-----------------+    +-----------------+    +-----------------+
|  Schema         |    |  Schema         |    |  Schema         |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|  Data           |    |  Data           |    |  Data           |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The following diagram illustrates the basic architecture of an Avro data file:

```
+-----------------+
|  Avro Data File |
+-----------------+
|  Metadata       |
|  (Schema, etc.) |
+-----------------+
|  Data Block 1   |
|  (Sync Marker,  |
|  Length, Data)  |
+-----------------+
|  Data Block 2   |
|  (Sync Marker,  |
|  Length, Data)  |
+-----------------+
|  ...            |
+-----------------+
|  Data Block N   |
|  (Sync Marker,  |
|  Length, Data)  |
+-----------------+
```
