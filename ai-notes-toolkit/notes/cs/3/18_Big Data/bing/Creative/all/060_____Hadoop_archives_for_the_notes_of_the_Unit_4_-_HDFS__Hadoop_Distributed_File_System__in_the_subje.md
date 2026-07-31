# Hadoop Archives

- Hadoop archives are special format archives that can reduce the number of files in HDFS and improve the performance of MapReduce jobs.
- A Hadoop archive maps to a file system directory and always has a *.har extension.
- A Hadoop archive directory contains metadata (in the form of _index and _masterindex) and data (part-*) files.
- The _index file contains the name of the files that are part of the archive and the location within the part files.
- The _masterindex file contains the offset of each part file within the archive.
- Hadoop archives can be created using the `hadoop archive` command with the following syntax:

```
hadoop archive -archiveName name -p <parent> [-r <replication factor>] <src>* <dest>
```

- Hadoop archives can be accessed using the `har://` scheme or the `fs -lsr` command.
- Hadoop archives can be used as input or output of MapReduce jobs, but they cannot be modified or deleted.