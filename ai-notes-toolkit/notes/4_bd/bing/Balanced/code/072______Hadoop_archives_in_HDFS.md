#### Hadoop archives in HDFS

Hadoop archives or HAR files are a way of archiving files in HDFS more efficiently, reducing the memory usage of the Name Node and allowing transparent access to the files. HAR files can also be used as input to MapReduce jobs.

To create a HAR file from a collection of files, you can use the `hadoop archive` command, which will run a MapReduce job to process the input files in parallel and create an archive file. For example, to create a HAR file named `foo.har` from the files in the directory `/user/zoo/input` and store it in the directory `/user/zoo/output`, you can use the following command:

```bash
hadoop archive -archiveName foo.har -p /user/zoo/input /user/zoo/output
```

To access the files inside the HAR file, you can use the `har://` scheme to specify the path. For example, to list the files in the HAR file, you can use the following command:

```bash
hadoop fs -ls har:///user/zoo/output/foo.har
```

To use the HAR file as input to a MapReduce job, you can specify the `har://` scheme as the input directory. For example, to run a word count job on the HAR file, you can use the following command:

```bash
hadoop jar hadoop-examples.jar wordcount har:///user/zoo/output/foo.har /user/zoo/wordcount
```

HAR files are useful for storing large numbers of small files in HDFS, as they reduce the overhead of the Name Node and improve the performance of MapReduce jobs. However, HAR files have some limitations, such as:

- They are read-only and cannot be modified or appended.
- They do not support compression or encryption.
- They do not support random access to the files inside the archive.
- They may introduce some overhead in accessing the files, as they require an extra lookup in the index file.