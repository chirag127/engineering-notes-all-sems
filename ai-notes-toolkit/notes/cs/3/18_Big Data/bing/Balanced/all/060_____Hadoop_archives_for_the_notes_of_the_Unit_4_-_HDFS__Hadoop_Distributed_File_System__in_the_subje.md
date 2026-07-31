# Hadoop Archives

- Hadoop archives are special format archives that can be used to store large number of small files in HDFS.
- A Hadoop archive maps to a file system directory and has a *.har extension.
- A Hadoop archive directory contains metadata (in the form of _index and _masterindex) and data (part-*) files.
- The _index file contains the name of the files that are part of the archive and the location within the part files.
- The _masterindex file contains the offset of each part file within the archive.
- Hadoop archives can reduce the number of blocks and the namenode memory usage in HDFS.
- Hadoop archives can be created using the `hadoop archive` command with the following syntax:

```
hadoop archive -archiveName name -p <parent> [-r <replication factor>] <src>* <dest>
```

- Hadoop archives can be accessed using the `har://` scheme or the `hdfs://` scheme with the archive name as part of the path.
- Hadoop archives support most of the HDFS operations such as `ls`, `cat`, `cp`, `mv`, `rm`, etc.
- Hadoop archives do not support appending or modifying the files within the archive.