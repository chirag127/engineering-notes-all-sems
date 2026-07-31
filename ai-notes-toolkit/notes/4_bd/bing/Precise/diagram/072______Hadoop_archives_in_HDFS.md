#### Hadoop archives in HDFS

Hadoop archives (HAR) are a way to reduce the number of files in HDFS by combining small files into larger ones. Here is an ASCII diagram that shows how Hadoop archives work in HDFS:

```
+-----------------+
| HDFS            |
| +-------------+ |
| | HAR File    | |
| | +---------+ | |
| | | File 1  | | |
| | | File 2  | | |
| | | ...     | | |
| | | File N  | | |
| | +---------+ | |
| +-------------+ |
+-----------------+
```
