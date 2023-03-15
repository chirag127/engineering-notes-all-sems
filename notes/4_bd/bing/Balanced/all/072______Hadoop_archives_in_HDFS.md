#### Hadoop archives in HDFS

- Hadoop archives or HAR files are a file archiving facility that packs files into HDFS blocks more efficiently, thereby reducing NameNode memory usage while still allowing transparent access to files  .
- Hadoop archives can be used as input to MapReduce jobs  . Using Hadoop archives in MapReduce is as easy as specifying a different input filesystem than the default file system. For example, if you have a Hadoop archive stored in HDFS in /user/zoo/foo.har, then for using this archive for MapReduce input, all you need to specify the input directory as har:///user/zoo/foo.har .
- Hadoop archives are created from a collection of files and the archiving tool (a simple command) will run a MapReduce job to process the input files in parallel and create an archive file. The command to create a Hadoop archive is:

```bash
hadoop archive -archiveName name -p parent source destination
```

where name is the name of the archive file, parent is the parent directory of the source files, source is the name of the source directory, and destination is the name of the destination directory .

- Hadoop archives have a hierarchical structure that consists of an index file, a master index file, and data files. The index file contains the metadata of the files in the archive, such as name, size, and offset. The master index file contains the metadata of the index file, such as name, size, and offset. The data files contain the actual data of the files in the archive .
- Hadoop archives have some advantages and disadvantages. Some of the advantages are:

  - They reduce the NameNode memory usage by reducing the number of files in HDFS  .
  - They improve the performance of MapReduce jobs by reducing the number of mappers and the input splits .
  - They preserve the original permissions and ownership of the files in the archive .
  - They support compression and decompression of the files in the archive .

Some of the disadvantages are:

  - They do not support random access to the files in the archive. The entire archive file has to be read to access a single file .
  - They do not support append or overwrite operations on the files in the archive. The entire archive file has to be recreated to modify a single file .
  - They do not support replication or erasure coding of the files in the archive. The replication or erasure coding factor of the archive file is determined by the HDFS configuration .

- A possible mnemonic to remember the structure of a Hadoop archive is:

```text
HAR = Hierarchy of Index and Data
```

where H stands for Hadoop, A stands for Archive, R stands for file, Hierarchy stands for the nested structure of the archive, Index stands for the index and master index files, and Data stands for the data files.