#### HBase example

HBase is a column-oriented non-relational database management system that runs on top of Hadoop Distributed File System (HDFS). HBase provides a fault-tolerant way of storing sparse data sets, which are common in many big data use cases. It is well suited for real-time data processing or random read/write access to large volumes of data.

An example of HBase is as follows:

- An HBase table consists of rows and columns. Each row has a unique identifier called a row key. Each column belongs to a column family, which is a logical grouping of columns that share some common properties. A column is identified by its column family name and a qualifier. A cell is the intersection of a row and a column, which stores a value and a timestamp.
- An HBase table can be created using the HBase shell, which is a command-line interface for interacting with HBase. For example, to create a table named 'education' with a column family named 'guru99', the following command can be used:

```
hbase (main):001:0> create 'education','guru99'
0 rows (s) in 0.312 seconds
=>Hbase::Table – education
```

- An HBase table can be populated with data using the put command, which takes the table name, the row key, the column name, and the value as arguments. For example, to insert a record with the row key '1', the column 'guru99:name', and the value 'John' into the 'education' table, the following command can be used:

```
hbase (main):002:0> put 'education','1','guru99:name','John'
0 rows (s) in 0.031 seconds
```

- An HBase table can be queried using the get command, which takes the table name and the row key as arguments. For example, to retrieve the record with the row key '1' from the 'education' table, the following command can be used:

```
hbase (main):003:0> get 'education','1'
COLUMN                             CELL
 guru99:name                       timestamp=1639580896918, value=John
1 row (s) in 0.015 seconds
```

- An HBase table can be scanned using the scan command, which takes the table name and some optional parameters as arguments. For example, to scan the entire 'education' table, the following command can be used:

```
hbase (main):004:0> scan 'education'
ROW                                COLUMN+CELL
 1                                 column=guru99:name, timestamp=1639580896918, value=John
1 row (s) in 0.015 seconds
```

- An HBase table can be modified using the delete command, which takes the table name, the row key, and the column name as arguments. For example, to delete the column 'guru99:name' from the record with the row key '1' in the 'education' table, the following command can be used:

```
hbase (main):005:0> delete 'education','1','guru99:name'
0 rows (s) in 0.015 seconds
```

- An HBase table can be dropped using the disable and drop commands, which take the table name as an argument. For example, to drop the 'education' table, the following commands can be used:

```
hbase (main):006:0> disable 'education'
0 rows (s) in 0.015 seconds
hbase (main):007:0> drop 'education'
0 rows (s) in 0.015 seconds
```

These are some basic examples of how to use HBase. HBase can also be used for various applications in different domains, such as healthcare, e-commerce, sports, etc. For instance:

- In the healthcare sector, HBase is used for storing genome sequences and disease history of people or a particular area.
- In the field of e-commerce, HBase is used for storing logs about customer search history and it also performs analytics and target advertisement for better business insights.
- In sports, HBase is used to store match details and the history of each match.