 Here is the formal content in markdown format without any feeling or friendliness:

## Deleting files Hint: A typical Hadoop workflow creates data files (such as log files) elsewhere and copies them into HDFS using one of the above command line utilities

- Data files can be deleted from HDFS using the `hadoop fs -rm` command.
- The `-r` flag can be used to delete directories and their contents recursively.
- Wildcards can be used to delete multiple files at once. For example, `hadoop fs -rm log*` would delete all files starting with "log".
- Deleted files are moved to the trash directory ($HDFS_HOME/trash) and are eventually deleted after the trash retention period expires (by default 168 hours or 7 days). The trash retention period can be configured by changing the `fs.trash.interval` property.
- The trash can be emptied manually using `hadoop fs -expunge`. This permanently deletes all files in the trash, even before the retention period expires.
- Hadoop 2.x clusters introduced an additional `fs.hdfs.umask.enableTrash` configuration to disable the trash completely if set to `false`. In this case, deletes go straight to permanent removal and bypass the trash.

The above points cover how to delete files in HDFS for the notes of the BIG DATA AND ANALYTICS LAB in the subject of BIG DATA AND ANALYTICS LAB. The content is written in formal language without any feeling or friendliness and in markdown format as requested.