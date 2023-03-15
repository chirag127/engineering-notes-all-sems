#### Hive shell

- Hive shell is a command-line interface that allows users to interact with Hive and execute HiveQL commands.
- Hive shell can be launched by typing `hive` in the terminal or by specifying a script file to run with `hive -f script.hql`.
- Hive shell supports various options and commands to configure and control the Hive session, such as `-hiveconf`, `-hivevar`, `-e`, `-i`, `-S`, `-v`, `-h`, etc.
- Hive shell also supports some built-in commands that are not part of HiveQL, such as `set`, `dfs`, `add`, `list`, `delete`, `reload`, etc.
- Hive shell can be used to create, alter, drop, and query tables, views, partitions, functions, and indexes in Hive.
- Hive shell can also be used to load data from local or HDFS files into Hive tables, or export data from Hive tables to local or HDFS files.
- Hive shell can display the results of queries in various formats, such as table, csv, tsv, etc. by using the `set hive.cli.print.header` and `set hive.cli.output.format` properties.
- Hive shell can also store the results of queries into local or HDFS files by using the `INSERT OVERWRITE LOCAL DIRECTORY` or `INSERT OVERWRITE DIRECTORY` commands.