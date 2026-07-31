#### HBase example

HBase is a column-oriented non-relational database management system that runs on top of Hadoop Distributed File System (HDFS). It provides a fault-tolerant way of storing sparse data sets, which are common in many big data use cases. It is well suited for real-time data processing or random read/write access to large volumes of data.

Here are some examples of how HBase is used in different industries:

1. In the healthcare sector, HBase is used for storing genome sequences and disease history of people or a particular area.
2. In the field of e-commerce, HBase is used for storing logs about customer search history and it also performs analytics and target advertisement for better business insights.
3. In sports, HBase is used to store match details and the history of each match.

An example of HBase in action is when storing diagnostic logs from servers in an environment. Each row might be a log record, and a typical column could be the timestamp of when the log record was written, or the server name where the record originated.

Another example is creating a table in HBase with the specified name and column family. For instance, to create a table named 'education' with a column family 'guru99', the HBase shell command would be: `create 'education','guru99'`.