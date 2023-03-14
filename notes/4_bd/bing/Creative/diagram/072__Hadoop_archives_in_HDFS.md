#### Hadoop archives in HDFS

Hadoop archives (HAR) are a special format of archives that pack files into HDFS blocks more efficiently, thereby reducing the NameNode memory usage while still allowing transparent access to files. HAR files can be used as input to MapReduce jobs and have a *.har extension. A HAR file directory contains metadata (_index and _masterindex) and data (part-*) files. The _index file contains the name of the files that are part of the archive and the location within the part files  .

The following diagram illustrates the basic architecture of a HAR file:

```
+-----------------+  +-----------------+  +-----------------+
| HDFS Block 1    |  | HDFS Block 2    |  | HDFS Block 3    |
| +-------------+ |  | +-------------+ |  | +-------------+ |
| | part-0      | |  | | part-1      | |  | | part-2      | |
| | +---------+ | |  | | +---------+ | |  | | +---------+ | |
| | | file1   | | |  | | | file4   | | |  | | | file7   | | |
| | +---------+ | |  | | +---------+ | |  | | +---------+ | |
| | +---------+ | |  | | +---------+ | |  | | +---------+ | |
| | | file2   | | |  | | | file5   | | |  | | | file8   | | |
| | +---------+ | |  | | +---------+ | |  | | +---------+ | |
| | +---------+ | |  | | +---------+ | |  | | +---------+ | |
| | | file3   | | |  | | | file6   | | |  | | | file9   | | |
| | +---------+ | |  | | +---------+ | |  | | +---------+ | |
| +-------------+ |  | +-------------+ |  | +-------------+ |
+-----------------+  +-----------------+  +-----------------+
         |                   |                   |
         +-------------------+-------------------+
                             |
                             v
+---------------------------------------------------------------+
| HAR file directory                                           |
| +-----------------+  +-----------------+  +-----------------+ |
| | _masterindex    |  | _index          |  | part-*          | |
| | +-------------+ |  | +-------------+ |  | +-------------+ | |
| | | HDFS Block  | |  | | File Name   | |  | | File Data   | | |
| | | Locations   | |  | | and Offset  | |  | | and Length  | | |
| | +-------------+ |  | +-------------+ |  | +-------------+ | |
| +-----------------+  +-----------------+  +-----------------+ |
+---------------------------------------------------------------+
```

To create a HAR file, the hadoop archive command is used with the following syntax:

```
hadoop archive -archiveName name -p <parent> [-r <replication factor>] <src>* <dest>
```

To look up files in a HAR file, the har:// URI scheme is used with the following syntax:

```
har://scheme-hostname:port/archivepath/fileinarchive
```

To unarchive a HAR file, the hdfs dfs -cp or hadoop distcp command is used with the following syntax:

```
hdfs dfs -cp har:///archivepath/fileinarchive hdfs:/destpath
hadoop distcp har:///archivepath/fileinarchive hdfs:/destpath
```