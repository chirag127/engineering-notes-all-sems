#### Hadoop archives in HDFS

Hadoop archives (HAR files) are a way to reduce the number of files in HDFS, by combining smaller files into larger archives. This can improve the performance of HDFS by reducing the load on the NameNode.

Here is an example of how to create a Hadoop archive using the `hadoop archive` command:

```sh
hadoop archive -archiveName myArchive.har -p /input /output
```

This command will create a Hadoop archive named `myArchive.har` from the files in the `/input` directory and store the archive in the `/output` directory.

You can then access the files in the archive using the `har://` URI scheme. For example, to access a file named `file.txt` in the archive, you would use the following URI: `har:///output/myArchive.har/file.txt`.