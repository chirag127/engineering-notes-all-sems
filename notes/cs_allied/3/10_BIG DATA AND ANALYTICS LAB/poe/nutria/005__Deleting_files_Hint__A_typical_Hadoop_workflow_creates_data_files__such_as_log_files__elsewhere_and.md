
## Deleting Files 

A typical Hadoop workflow creates data files (such as log files) elsewhere and copies them into HDFS using one of the following command line utilities: 

- `hadoop fs -rm`: This command is used to delete files from HDFS. 
- `hadoop fs -rmdir`: This command is used to delete directories from HDFS. 
- `hadoop fs -expunge`: This command is used to delete files from HDFS and clear out the Trash directory. 

When deleting files from HDFS, it is important to remember that the files are not permanently deleted until the Trash directory is cleared out. Therefore, it is important to use the `hadoop fs -expunge` command to permanently delete files from HDFS.