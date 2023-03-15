#### File sizes in HDFS

HDFS is a distributed file system that can store large files across multiple nodes in a cluster. A typical file in HDFS is gigabytes to terabytes in size. HDFS breaks down each file into fixed-size blocks, called data blocks, and stores them as independent units. The default size of these data blocks is 128 MB, but it can be configured by the user.

To find the size of a file or a directory in HDFS, you can use the `hadoop fs -du` command. This command shows the amount of space in bytes that have been used by the files that match the specified file pattern. For example, to find the size of a file named `input.txt` in the current directory, you can run:

```bash
hadoop fs -du input.txt
```

This will output something like:

```bash
1024 /user/hduser/input.txt
```

The first column is the file size in bytes, and the second column is the file path. You can also use the `-s` option to summarize the total size of a directory or multiple files. For example, to find the total size of all files containing `count` in the current directory, you can run:

```bash
hadoop fs -du -s count*
```

This will output something like:

```bash
2048 /user/hduser/count1.txt
2048 /user/hduser/count2.txt
```

The first column is the total size in bytes, and the second column is the file pattern. You can also use the `-h` option to display the sizes in human-readable format, such as KB, MB, GB, etc. For example, to find the size of a directory named `some_dir` in human-readable format, you can run:

```bash
hadoop fs -du -h some_dir
```

This will output something like:

```bash
4.0 K some_dir
```

The first column is the size in human-readable format, and the second column is the directory path.