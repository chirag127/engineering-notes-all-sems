#### Hadoop archives in HDFS

- Hadoop archives (HAR) are a special format of archives that can pack files into HDFS blocks more efficiently, thereby reducing the NameNode memory usage and the namespace pressure    .
- HAR files can be created from a collection of files using a simple command that runs a MapReduce job to process the input files in parallel and create an archive file  .
- HAR files can be used as input to MapReduce jobs and can be accessed transparently using a file system layer with a different URI   .
- HAR files are immutable, so operations like rename, delete and create are not supported  .
- HAR files can be unarchived by copying them to a regular HDFS directory using either sequential or parallel methods  .