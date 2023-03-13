Hadoop archives (HAR) are a way of compressing and storing multiple small files in HDFS more efficiently, reducing the memory usage of the NameNode and allowing transparent access to the files. HAR files are created by running a MapReduce job that takes a collection of files as input and produces an archive file as output. The archive file consists of an index file, a master index file, and one or more part files that contain the compressed data. The index file maps the original file names and sizes to the part files and offsets. The master index file maps the part files to their HDFS block locations. The part files are stored as regular HDFS files and can be accessed using a special har:// URI scheme.

#### Hadoop archives in HDFS

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Input files    |    |  HAR file       |    |  Part files     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
| file1.txt       |    | index           |    | part-0          |
| file2.txt       |    | masterindex     |    | part-1          |
| file3.txt       |    |                 |    | part-2          |
| ...             |    |                 |    | ...             |
+-----------------+    +-----------------+    +-----------------+
        |                     |                      |
        |                     |                      |
        +---------------------+----------------------+
                              |
                              |
                              v
                      +-----------------+
                      |                 |
                      |  MapReduce job  |
                      |                 |
                      +-----------------+
                              |
                              |
                              v
                      +-----------------+
                      |                 |
                      |  HDFS blocks    |
                      |                 |
                      +-----------------+
                      | block1          |
                      | block2          |
                      | block3          |
                      | ...             |
                      +-----------------+
```