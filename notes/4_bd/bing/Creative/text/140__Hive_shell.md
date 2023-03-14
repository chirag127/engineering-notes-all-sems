#### Hive shell

- Hive shell is a command-line interface that allows users to interact with Hive and run Hive queries.
- Hive shell can be launched by typing `hive` in the terminal, or by specifying a script file with the `-f` option.
- Hive shell supports Hive Query Language (HQL), which is a SQL-like language for querying and managing data stored in Hadoop.
- Hive shell can also execute commands that are not part of HQL, such as `set`, `dfs`, `add`, `list`, etc. These commands are used to configure Hive settings, access Hadoop file system, add files or jars to the classpath, and list the available functions or tables.
- Hive shell can run in two modes: interactive and batch. In interactive mode, users can type HQL statements and see the results on the screen. In batch mode, users can run a script file that contains multiple HQL statements and see the output in a log file.
- Hive shell can connect to different Hive servers, such as HiveServer1 or HiveServer2. HiveServer2 is the preferred option, as it supports multiple clients, security, and a JDBC/ODBC driver. To connect to HiveServer2, users need to use a separate CLI called Beeline, which is based on SQLLine. Beeline can be launched by typing `beeline` in the terminal, or by specifying a connection string with the `-u` option.