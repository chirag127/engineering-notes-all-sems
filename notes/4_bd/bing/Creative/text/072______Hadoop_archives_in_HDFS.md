#### Hadoop archives in HDFS

- Hadoop archives (HAR) are a way of compressing large numbers of small files in HDFS to reduce the metadata overhead and improve the performance of the file system.
- HAR files are similar to ZIP or TAR files, but they are not compressed. They are created by using the `hadoop archive` command, which takes a list of files or directories as input and produces a single HAR file as output.
- HAR files can be accessed transparently by using the `har://` scheme in the file path. For example, `har:///user/hadoop/test.har/file1.txt` refers to the file `file1.txt` inside the HAR file `test.har` in the HDFS directory `/user/hadoop`.
- HAR files can be used to store rarely accessed files or historical data that do not need to be modified. They can also be used as input or output for MapReduce jobs, as long as the job does not require splitting the input files.
- HAR files have some limitations and trade-offs. They cannot be modified or appended once created. They also introduce some overhead in reading and writing, as the HAR file has to be scanned to locate the desired file. They also do not support compression or encryption.