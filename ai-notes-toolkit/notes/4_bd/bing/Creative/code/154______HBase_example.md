#### HBase example

HBase is a column-oriented non-relational database management system that runs on top of Hadoop Distributed File System (HDFS). HBase provides a fault-tolerant way of storing sparse data sets, which are common in many big data use cases. It is well suited for real-time data processing or random read/write access to large volumes of data.

Some examples of HBase applications are:

- In the healthcare sector, HBase is used for storing genome sequences and disease history of people or a particular area .
- In the field of e-commerce, HBase is used for storing logs about customer search history and it also performs analytics and target advertisement for better business insights .
- In sports, HBase is used to store match details and the history of each match.
- In social media, HBase is used to store user profiles, messages, comments, likes, and other interactions.

To create a table in HBase, you can use the HBase shell command `create` with the table name and the column family name as arguments. For example, to create a table named `education` with a column family named `guru99`, you can use the following command:

```
hbase (main):001:0> create 'education','guru99'
0 rows (s) in 0.312 seconds
=>Hbase::Table – education
```

To access the HBase Master UI, you can sign into the Ambari Web UI at https://CLUSTERNAME.azurehdinsight.net where CLUSTERNAME is the name of your HBase cluster. Select HBase from the left menu. The HBase Master UI allows you to monitor the cluster status, request statistics, or view information about regions.