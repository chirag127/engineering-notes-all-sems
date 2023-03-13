#### Hadoop archives in HDFS

- Hadoop archives or HAR files are a file archiving facility that packs files into HDFS blocks more efficiently, thereby reducing Name Node memory usage while still allowing transparent access to files  .
- Hadoop archives can be used as input to MapReduce jobs   by specifying a different input filesystem than the default file system. For example, if you have a hadoop archive stored in HDFS in /user/zoo/foo.har then for using this archive for MapReduce input, all you need to specify the input directory as har:///user/zoo/foo.har .
- Hadoop archives are created from a collection of files and the archiving tool (a simple command) will run a MapReduce job to process the input files in parallel and create an archive file. The command syntax is:

```bash
hadoop archive -archiveName name -p <parent path> <src>* <dest>
```

- Hadoop archives have a hierarchical structure that consists of an index file, a master index file and data files . The index file contains the metadata of the files in the archive, such as name, size, modification time, etc. The master index file contains the offsets of the index files in the data files. The data files contain the actual data of the files in the archive.
- Hadoop archives can be accessed using the har:// scheme or using the hadoop fs -lsr command . The har:// scheme allows the user to access the files in the archive as if they were normal files in HDFS. The hadoop fs -lsr command lists the files in the archive recursively.