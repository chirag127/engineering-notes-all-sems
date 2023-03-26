 Here is the content in Markdown format without any external links or emojis:

## Installation of HBase

1. Download HBase from http://hbase.apache.org/downloads.html. Choose a stable version. For this lab, we will use HBase 1.2.6.
2. Unzip the downloaded file. This will create a directory called hbase-1.2.6.
3. Set HBASE_HOME environment variable to point to the hbase-1.2.6 directory.
4. Add $HBASE_HOME/bin to PATH. This is required to run HBase commands without providing the full path.
5. Create HBase data directories:
```
mkdir -p ~/hbase/data
mkdir -p ~/hbase/logs
```
6. Start HBase:
```
start-hbase.sh
```
7. Check if HBase is running by visiting HBase Web UI - http://localhost:16010/.

## Installing thrift

1. Download thrift from http://thrift.apache.org/download.
2. Unzip the downloaded file. This will create a directory called thrift-0.9.3.
3. Set THRIFT_HOME environment variable to point to the thrift-0.9.3 directory.
4. Add $THRIFT_HOME/bin and $THRIFT_HOME/lib/java to PATH.

## Practice examples

1. Create a table:
```
create 'student', 'name', 'age'
```
2. Put some data in the table:
```
put 'student', '1', 'name', 'John'
put 'student', '1', 'age', '20'
```
3. Scan the table:
```
scan 'student'
```

...

[More practice examples to be added]