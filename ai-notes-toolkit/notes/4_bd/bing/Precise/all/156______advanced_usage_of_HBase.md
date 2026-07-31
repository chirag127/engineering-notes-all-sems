#### Advanced Usage of HBase

HBase is a column-oriented non-relational database management system that runs on top of Hadoop Distributed File System (HDFS). It provides a fault-tolerant way of storing sparse data sets, which are common in many big data use cases. It is well suited for real-time data processing or random read/write access to large volumes of data.

Some advanced usage of HBase includes:
1. In the healthcare sector, HBase is used for storing genome sequences and disease history of people or a particular area.
2. In the field of e-commerce, HBase is used for storing logs about customer search history and it also performs analytics and target advertisement for better business insights.
3. In sports, HBase is used to store match details and the history of each match.
4. HBase has two fundamental key structures: the row key and the column key. Both can be used to convey meaning, by either the data they store, or by exploiting their sorting order. These keys can be used to solve commonly found problems when designing storage solutions.

HBase can be used when we want to store huge volumes of data and want high scalability. However, it should be noted that it can only be used if we can live without all the extra features of traditional database systems like typed columns, transactions, advanced query languages, secondary indexes, etc.