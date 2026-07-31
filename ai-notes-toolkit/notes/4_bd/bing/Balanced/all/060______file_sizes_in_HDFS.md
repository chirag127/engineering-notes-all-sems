#### File sizes in HDFS

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant storage system for large-scale data processing.
- HDFS is designed to store and handle files that are **gigabytes to terabytes** in size . It splits files into fixed-size blocks, which are distributed across multiple nodes in a cluster.
- The default block size in HDFS is **128 MB**, which can be configured by changing the parameter `dfs.blocksize` in `hdfs-site.xml` file. The block size should be chosen based on the network bandwidth, disk space, and application requirements.
- To check the size of a file or a directory in HDFS, one can use the command `hadoop fs -du`  , which shows the disk usage in bytes before replication. For example, `hadoop fs -du /user/hduser/input` will show the size of the directory `/user/hduser/input` and its contents.
- To check the size of a file or a directory in HDFS in a human-readable format, one can use the option `-h` with the command `hadoop fs -du`. For example, `hadoop fs -du -h /user/hduser/input` will show the size in KB, MB, GB, etc.
- To check the total size of a file or a directory in HDFS, one can use the option `-s` with the command `hadoop fs -du`. For example, `hadoop fs -du -s /user/hduser/input` will show the sum of the sizes of all the files and subdirectories under `/user/hduser/input`.
- To check the size of a file or a directory in HDFS that matches a certain pattern, one can use the wildcard `*` with the command `hadoop fs -du`. For example, `hadoop fs -du /user/hduser/input/*.txt` will show the size of all the text files under `/user/hduser/input`.
- A possible mnemonic to remember the command `hadoop fs -du` is: **D**isk **U**sage of **F**ile **S**ystem in **H**adoop.