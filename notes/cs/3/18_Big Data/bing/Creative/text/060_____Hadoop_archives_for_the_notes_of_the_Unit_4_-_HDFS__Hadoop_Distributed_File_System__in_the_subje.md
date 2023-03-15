### Hadoop archives

- Hadoop archives are special format archives that can be used to store large number of small files in HDFS  .
- A Hadoop archive maps to a file system directory and always has a *.har extension  .
- A Hadoop archive directory contains metadata (in the form of _index and _masterindex) and data (part-*) files  .
- The _index file contains the name of the files that are part of the archive and the location within the part files .
- The _masterindex file contains the offset of each part file within the archive.
- The part files contain the actual data of the archived files.
- Hadoop archives can be created using the `hadoop archive` command .
- The syntax of the command is: `hadoop archive -archiveName name -p <parent> [-r <replication factor>] <src>* <dest>` .
- The `-archiveName` option specifies the name of the archive file with the *.har extension .
- The `-p` option specifies the parent path of the source files .
- The `-r` option specifies the replication factor of the archive file, which defaults to the cluster replication factor .
- The `<src>` option specifies one or more source files or directories to be archived .
- The `<dest>` option specifies the destination directory where the archive file will be created .
- Hadoop archives can be accessed using the `har://` scheme in the HDFS URI .
- For example, `har:///user/hadoop/test.har/file1.txt` refers to the file1.txt inside the test.har archive .
- Hadoop archives can be used to improve the performance and efficiency of HDFS by reducing the number of blocks and namenode memory usage  .
- Hadoop archives can also be used as input or output of MapReduce jobs .