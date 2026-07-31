### Hadoop Archives

- Hadoop archives are special format archives that can reduce the number of files in HDFS and improve the performance of MapReduce jobs.
- A Hadoop archive maps to a file system directory and has a *.har extension.
- A Hadoop archive directory contains metadata files (_index and _masterindex) and data files (part-*).
- The _index file contains the name and location of the files that are part of the archive.
- The _masterindex file contains the offset of each part file in the archive.
- To create a Hadoop archive, use the command: `hadoop archive -archiveName name -p <parent> [-r <replication factor>] <src>* <dest>`
- To access a file inside a Hadoop archive, use the har:// scheme, for example: `har:///user/hadoop/archive.har/file.txt`
- To list the contents of a Hadoop archive, use the command: `hadoop fs -lsr har:///user/hadoop/archive.har`
- To delete a Hadoop archive, use the command: `hadoop fs -rmr /user/hadoop/archive.har`
- Hadoop archives can be used as input or output of MapReduce jobs, but not as intermediate data.