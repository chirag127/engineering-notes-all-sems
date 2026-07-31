#### Hive Shell

- Hive Shell provides Hiveon OS remote access to your workers using the Hiveon OS network infrastructure .
- It offers unique features, such as access via an SSH client and console sharing .
- Hive Shell is a shell utility that can be used to run Hive queries in either interactive or batch mode .
- HiveServer2 (introduced in Hive 0.11) has its own CLI called Beeline, which is a JDBC client based on SQLLine .
- Variables can be set in Hive scripts using the `set hivevar:tablename=mytable;` command .
- The `source` command can be used to bring a script into Hive, for example: `hive> source /path/to/setup.hql;` .
- Variables can be used in queries, for example: `hive> select * from $ {tablename}` or `hive> select * from $ {hivevar:tablename}` .