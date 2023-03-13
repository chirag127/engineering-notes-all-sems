#### HBase example

- HBase is a column-oriented non-relational database management system that runs on top of Hadoop Distributed File System (HDFS) .
- HBase provides a fault-tolerant way of storing sparse data sets, which are common in many big data use cases .
- HBase is well suited for real-time data processing or random read/write access to large volumes of data .
- HBase can be installed in two modes: standalone mode and distributed mode .
- Standalone mode is for development and testing purposes, where HBase runs on a single machine without HDFS .
- Distributed mode is for production purposes, where HBase runs on a cluster of machines with HDFS .
- An HBase table consists of rows and columns, where each row has a unique identifier called row key .
- An HBase column represents an attribute of an object; for example, if the table is storing diagnostic logs from servers, each row might be a log record, and a typical column could be the timestamp of when the log record was written, or the server name where the record originated .
- An HBase column is organized into column families, which are groups of columns that share a common prefix and are stored together on disk .
- An HBase column can have multiple versions, which are stored as timestamps .
- An HBase table can have one or more regions, which are horizontal partitions of the table based on the row key range .
- An HBase region is assigned to a region server, which is a node in the cluster that handles read and write requests for that region .
- An HBase region server can serve multiple regions, and a region can be moved from one region server to another for load balancing or fault tolerance .
- An HBase master is a node in the cluster that coordinates the region servers and handles metadata operations, such as creating and deleting tables, splitting and merging regions, and assigning regions to region servers .
- An HBase client is a node in the cluster or outside the cluster that interacts with the HBase master and region servers to perform data operations, such as inserting, updating, deleting, and querying data .
- An HBase client can use different APIs, such as Java API, REST API, Thrift API, or HBase shell, to communicate with the HBase cluster  .
- An HBase shell is a command-line interface that allows the user to execute HBase commands using Ruby syntax .
- An HBase command can be used to create, alter, drop, list, scan, put, get, delete, count, truncate, or describe tables, columns, or rows .
- An example of creating a table in HBase using the shell is:

```
hbase (main):001:0> create 'education','guru99'
0 rows (s) in 0.312 seconds
=>Hbase::Table – education
```

- The above example explains how to create a table in HBase with the name 'education' and the column family 'guru99' .
- An example of inserting data into the table using the shell is:

```
hbase (main):002:0> put 'education','row1','guru99:course','HBase'
0 rows (s) in 0.031 seconds
```

- The above example explains how to insert a row with the row key 'row1' and the column 'guru99:course' with the value 'HBase' into the table 'education' .
- An example of querying data from the table using the shell is:

```
hbase (main):003:0> get 'education','row1'
COLUMN                             CELL
 guru99:course                     timestamp=1639492614, value=HBase
1 row (s) in 0.015 seconds
```

- The above example explains how to retrieve the row with the row key 'row1' from the table 'education' .
- An example of deleting data from the table using the shell is:

```
hbase (main):004:0> delete 'education','row1','guru99:course'
0 rows (s) in 0.015 seconds
```

- The above example