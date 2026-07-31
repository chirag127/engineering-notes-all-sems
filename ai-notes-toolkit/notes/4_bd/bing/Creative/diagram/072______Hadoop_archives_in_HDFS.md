Hadoop archives (HAR) are a way of compressing and storing multiple small files in HDFS more efficiently, without using too much memory on the NameNode. HAR files are created by running a MapReduce job that takes a collection of files as input and produces an archive file as output. The archive file consists of two parts: an index file that contains the metadata of the original files, and a data file that contains the actual content of the original files. The index file and the data file are stored as regular HDFS files, but they are accessed through a special har:// URI scheme. The HAR files can be used as input to other MapReduce jobs, or accessed by other applications that support the har:// scheme.

A possible ASCII diagram for Hadoop archives in HDFS is:

```
+-----------------+      +-----------------+
|  Input files    |      |  Output files   |
|  in HDFS        |      |  in HDFS        |
+-----------------+      +-----------------+
| file1.txt       |      | foo.har         |
| file2.txt       |      | foo.har.index   |
| file3.txt       |      | foo.har.data    |
| ...             |      |                 |
+-----------------+      +-----------------+
         |                        ^
         |                        |
         v                        |
+-----------------+               |
|  MapReduce job  |               |
|  to create HAR  |               |
+-----------------+               |
         |                        |
         |                        |
         v                        |
+-----------------+               |
|  HAR file       |---------------+
|  in memory      |
+-----------------+
| foo.har         |
| foo.har.index   |
| foo.har.data    |
+-----------------+
```