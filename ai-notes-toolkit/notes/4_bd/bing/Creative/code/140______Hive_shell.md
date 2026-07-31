#### Hive shell

- Hive shell is a command-line interface that allows users to interact with Hive and run Hive queries .
- Hive shell can be launched by typing `$HIVE_HOME/bin/hive` in the terminal, where `$HIVE_HOME` is the environment variable that points to the Hive installation directory.
- Hive shell supports both interactive and batch modes. In interactive mode, users can type Hive queries and see the results on the screen. In batch mode, users can execute a script file that contains Hive queries by using the `-f` option.
- Hive shell also supports variables that can be used to pass parameters to Hive queries. Variables can be set using the `set` command with the syntax `set hivevar:name=value` or `set name=value`. Variables can be referenced using the syntax `${name}` or `${hivevar:name}`.
- Hive shell provides some useful commands to manage the Hive environment, such as `show databases`, `show tables`, `describe table`, `create table`, `drop table`, etc. These commands are documented in the [Hive Language Manual](https://cwiki.apache.org/confluence/display/Hive/LanguageManual).
- Hive shell is different from Beeline, which is another command-line interface for Hive that uses JDBC to connect to HiveServer2. Beeline has some advantages over Hive shell, such as support for multiple sessions, authentication, and encryption.