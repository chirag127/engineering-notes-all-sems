#### Hadoop archives in HDFS

- Hadoop archives or HAR files are a file archiving facility that packs files into HDFS blocks more efficiently, thereby reducing NameNode memory usage while still allowing transparent access to files  .
- Hadoop archives can be used as input to MapReduce jobs   by specifying a different input filesystem than the default file system. For example, if you have a hadoop archive stored in HDFS in /user/zoo/foo.har then for using this archive for MapReduce input, all you need to specify the input directory as har:///user/zoo/foo.har .
- Hadoop archives are created from a collection of files and the archiving tool (a simple command) will run a MapReduce job to process the input files in parallel and create an archive file. The command syntax is:

```bash
hadoop archive -archiveName name -p <parent path> <src>* <dest>
```

- where name is the name of the archive file, -p is the parent path of the source files, src is the list of source files or directories, and dest is the destination directory in HDFS.
- Hadoop archives have a hierarchical structure that consists of an index file, a master index file, and data files . The index file contains the metadata of the files in the archive, such as name, size, and offset. The master index file contains the metadata of the index file, such as name, size, and offset. The data files contain the actual data of the files in the archive, packed into HDFS blocks.
- Hadoop archives have some advantages and disadvantages. Some of the advantages are:

  - They reduce the NameNode memory usage by storing many small files as one large file.
  - They improve the performance of MapReduce jobs by reducing the number of mappers and the input splits.
  - They preserve the original file permissions and ownership of the files in the archive.
  - They allow transparent access to the files in the archive using the har:// scheme.

- Some of the disadvantages are:

  - They increase the disk space usage by creating duplicate copies of the files in the archive.
  - They do not support compression or encryption of the files in the archive.
  - They do not support appending or modifying the files in the archive.
  - They do not support random access to the files in the archive.

- A possible mnemonic to remember the concept of Hadoop archives is:

  - HAR = Hadoop Archive = HDFS Block Archive
  - HAR files pack files into HDFS blocks more efficiently
  - HAR files can be used as input to MapReduce jobs
  - HAR files have a hierarchical structure of index, master index, and data files
  - HAR files have advantages and disadvantages