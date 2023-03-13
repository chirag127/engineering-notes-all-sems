#### Hadoop archives in HDFS

- Hadoop archives or HAR files are a file archiving facility that packs files into HDFS blocks more efficiently, thereby reducing Name Node memory usage while still allowing transparent access to files  .
- Hadoop archives can be used as input to MapReduce jobs   by specifying a different input filesystem than the default file system, such as `har:///user/zoo/foo.har` .
- Hadoop archives are created from a collection of files and the archiving tool (a simple command) will run a MapReduce job to process the input files in parallel and create an archive file.
- Hadoop archives have a hierarchical structure that consists of an index file, a master index file, and data files . The index file contains the metadata of the files in the archive, such as name, size, and offset. The master index file contains the metadata of the index files, such as name, size, and offset. The data files contain the actual data of the files in the archive.
- Hadoop archives can be accessed using the `har://` scheme or the `hadoop archive` command . The `har://` scheme allows users to browse, read, and write files in the archive as if they were normal files in HDFS. The `hadoop archive` command allows users to create, list, and get files from the archive.
- Hadoop archives can be used to tackle the small files problem in Hadoop, which occurs when there are too many small files in HDFS that consume a lot of Name Node memory and degrade the performance of MapReduce jobs . By packing small files into larger blocks, Hadoop archives reduce the number of files and blocks in HDFS and improve the efficiency of MapReduce jobs.
- Hadoop archives have some limitations, such as not supporting append or overwrite operations, not preserving the permissions and ownership of the original files, and not being compatible with some HDFS features, such as snapshots, encryption zones, and erasure coding .

A possible mnemonic to remember the main features of Hadoop archives is:

**H**ierarchical structure
**A**ccessible by `har://` scheme or `hadoop archive` command
**R**educes Name Node memory usage and small files problem
**F**ormed by a MapReduce job
**I**nput to MapReduce jobs
**L**imitations on append, overwrite, permissions, and compatibility
**E**fficient packing of files into blocks