## Deleting files

- To delete files from HDFS, we can use the `hadoop fs -rm` command, which takes one or more paths as arguments and deletes them recursively.
- For example, to delete a file named `log.txt` from the `/user/sydney` directory, we can run:

```
hadoop fs -rm /user/sydney/log.txt
```

- To delete a directory and all its contents, we can use the `-r` option, which stands for recursive. For example, to delete the `/user/sydney/logs` directory, we can run:

```
hadoop fs -rm -r /user/sydney/logs
```

- To delete files or directories without confirmation, we can use the `-f` option, which stands for force. For example, to delete the `/user/sydney/temp` directory without asking for confirmation, we can run:

```
hadoop fs -rm -f -r /user/sydney/temp
```

- To delete files or directories and move them to the trash, we can use the `-skipTrash` option, which will skip the trash mechanism and delete the files or directories permanently. For example, to delete the `/user/sydney/data` directory and move it to the trash, we can run:

```
hadoop fs -rm -skipTrash /user/sydney/data
```

- To delete files or directories from the trash, we can use the `hadoop fs -expunge` command, which will empty the trash and free up space. For example, to delete all the files or directories from the trash, we can run:

```
hadoop fs -expunge
```

- To view the contents of the trash, we can use the `hadoop fs -ls` command with the `.Trash` directory as the argument. For example, to view the contents of the trash for the current user, we can run:

```
hadoop fs -ls .Trash
```

- To restore files or directories from the trash, we can use the `hadoop fs -mv` command with the `.Trash` directory as the source and the desired destination as the target. For example, to restore the `/user/sydney/data` directory from the trash, we can run:

```
hadoop fs -mv .Trash/Current/user/sydney/data /user/sydney/data
```

- Note: The trash mechanism is enabled by default and has a retention period of 6 hours. This means that the files or directories deleted from HDFS will be moved to the trash and will be deleted permanently after 6 hours. To disable the trash mechanism, we can set the `fs.trash.interval` property to 0 in the `core-site.xml` file. To change the retention period, we can set the `fs.trash.interval` property to a different value in minutes. For example, to set the retention period to 24 hours, we can set the `fs.trash.interval` property to 1440.