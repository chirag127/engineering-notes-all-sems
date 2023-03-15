#### Advanced Usage of HBase

HBase is a column-oriented non-relational database management system that runs on top of Hadoop Distributed File System (HDFS). It provides a fault-tolerant way of storing sparse data sets, which are common in many big data use cases. It is well suited for real-time data processing or random read/write access to large volumes of data.

HBase has two fundamental key structures: the row key and the column key. Both can be used to convey meaning, by either the data they store, or by exploiting their sorting order. These keys can be used to solve commonly found problems when designing storage solutions.

Some advanced use cases of HBase include:
1. In the healthcare sector, HBase is used for storing genome sequences and disease history of people or a particular area.
2. In the field of e-commerce, HBase is used for storing logs about customer search history and it also performs analytics and target advertisement for better business insights.
3. In sports, HBase is used to store match details and the history of each match.

HBase is mainly used for random, real-time read/write access to Big Data. It can be used when there is a need to store huge volumes of data and high scalability is required. However, it can only be used if the user can live without all the extra features of traditional database systems like typed columns, transactions, advanced query languages, secondary indexes, etc.