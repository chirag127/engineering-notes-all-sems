### Hive shell

Hive shell is a command-line interface that allows users to interact with Hive and run Hive queries. It can be used in either interactive or batch mode. Some of the features and benefits of Hive shell are:

- It supports HiveQL, which is a SQL-like language for querying and analyzing data stored in Hadoop.
- It allows users to create, drop, alter, and query tables and partitions in Hive.
- It supports variables, comments, and scripts that can be used to customize and automate Hive queries.
- It provides access to Hive configuration parameters and functions.
- It can connect to HiveServer2, which is a service that enables remote clients to execute queries against Hive.

To launch Hive shell, users need to run the following command:

```bash
$HIVE_HOME/bin/hive
```

where `$HIVE_HOME` is the environment variable that points to the Hive installation directory.

Once the Hive shell is launched, users can enter HiveQL statements and commands, such as:

```sql
hive> show databases;
hive> use default;
hive> create table emp (id int, name string, salary double);
hive> load data local inpath '/home/user/emp.txt' into table emp;
hive> select * from emp where salary > 50000;
hive> set hivevar:tablename=emp;
hive> select * from ${hivevar:tablename};
```

To exit the Hive shell, users can enter `quit` or `exit` commands, or press `Ctrl+D`.

Hive shell also supports some built-in commands that are not part of HiveQL, such as:

- `!` to execute a shell command, such as `!ls` or `!pwd`.
- `source` to execute a script file that contains HiveQL statements, such as `source /path/to/script.hql`.
- `dfs` to execute a Hadoop file system command, such as `dfs -ls /user/hive/warehouse`.
- `add` to add a file, jar, or archive to the distributed cache, such as `add file /path/to/file.txt`.
- `list` to list the files, jars, and archives in the distributed cache, such as `list files`.
- `delete` to delete a file, jar, or archive from the distributed cache, such as `delete file file.txt`.

For more information on Hive shell, users can refer to the official documentation  or the online tutorials.