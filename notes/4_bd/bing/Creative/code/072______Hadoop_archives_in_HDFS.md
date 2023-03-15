#### Hadoop archives in HDFS

Hadoop archives or HAR files are a way of archiving files in HDFS more efficiently, reducing the memory usage of the Name Node and allowing transparent access to the archived files . HAR files can also be used as input to MapReduce jobs.

To create a HAR file from a collection of files, you can use the `hadoop archive` command, which will run a MapReduce job to process the input files in parallel and create an archive file. For example, to create a HAR file named `foo.har` from the files in the directory `/user/zoo`, you can use the following command:

```bash
hadoop archive -archiveName foo.har -p /user/zoo /user/zoo/foo.har
```

To access the files inside the HAR file, you can use the `har://` scheme to specify the path to the archive file and the relative path to the file inside the archive . For example, to access the file `bar.txt` inside the `foo.har` archive, you can use the following path:

```bash
har:///user/zoo/foo.har/bar.txt
```

You can also use the `hadoop fs` command to list, copy, or delete the files inside the HAR file, using the same `har://` scheme . For example, to list the files inside the `foo.har` archive, you can use the following command:

```bash
hadoop fs -ls har:///user/zoo/foo.har
```