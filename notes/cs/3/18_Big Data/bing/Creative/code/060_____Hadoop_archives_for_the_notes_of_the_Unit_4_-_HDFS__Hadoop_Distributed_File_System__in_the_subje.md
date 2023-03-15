### Hadoop archives

- Hadoop archives are special format archives that reduce the number of files in HDFS and improve the performance of MapReduce jobs  .
- A Hadoop archive maps to a file system directory and always has a *.har extension  .
- A Hadoop archive directory contains metadata (in the form of _index and _masterindex) and data (part-*) files  .
- The _index file contains the name of the files that are part of the archive and the location within the part files .
- The _masterindex file contains the offset of each part file within the archive.
- To create a Hadoop archive, the command is: `hadoop archive -archiveName name -p <parent> [-r <replication factor>] <src>* <dest>` .
- To access a file inside a Hadoop archive, the URI is: `har://<archive_path>/<file_path>` .
- Hadoop archives support most of the HDFS commands, such as `ls`, `cat`, `cp`, `mv`, `rm`, `chmod`, `chown`, etc .
- Hadoop archives can be used as input or output of MapReduce jobs, as long as the input format and output format support them .
- Hadoop archives can improve the performance of MapReduce jobs by reducing the number of mappers, the disk I/O, and the network traffic .