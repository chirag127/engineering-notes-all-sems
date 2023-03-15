#### Hive shell

- Hive shell is a command-line interface that allows users to interact with Hive and run Hive queries .
- Hive shell can be launched by typing `$HIVE_HOME/bin/hive` in the terminal, where `$HIVE_HOME` is the environment variable that points to the Hive installation directory.
- Hive shell supports both interactive and batch modes. In interactive mode, users can type Hive queries and get the results on the screen. In batch mode, users can execute a script file that contains Hive queries by using the `-f` option.
- Hive shell also supports variables that can be used to pass parameters to Hive queries. Variables can be set by using the `set` command with the `hivevar` prefix, such as `set hivevar:tablename=mytable;`. Variables can be referenced by using the `${}` syntax, such as `select * from ${tablename};`.
- Hive shell provides some useful commands to manage the Hive session, such as `show databases;`, `use database;`, `show tables;`, `describe table;`, `quit;`, etc.
- Hive shell can also be used to access Hiveon OS workers remotely using the Hiveon OS network infrastructure. Hiveon OS is a Linux-based operating system for mining cryptocurrencies. Hive shell offers some unique features, such as access via an SSH client and console sharing.