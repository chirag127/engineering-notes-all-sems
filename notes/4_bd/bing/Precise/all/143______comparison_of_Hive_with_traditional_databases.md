#### Comparison of Hive with traditional databases

Hive is a data warehouse software system that provides data query and analysis. It gives an interface like SQL to query data stored in various databases and file systems that integrate with Hadoop. Hive helps with querying and managing large datasets real fast .

- **Interface:** Hive is similar to traditional databases by supporting the SQL interface but it is not a full database. Instead of calling Hive a database, it can also be called a data warehouse .
- **Schema:** Hive applies schema on read time but traditional databases apply schema on write time .
- **Data Analysis:** Hive is better for analyzing complex data sets while traditional databases are better for analyzing less complicated data sets very quickly .
- **Online Transactional Processing (OLTP):** SQL supports OLTP while Hive doesn't support OLTP .
- **Latency:** Hive queries can have high latency because Hive runs batch processing via Hadoop. This means an hour's wait (or more) for some queries .
- **Data Processing:** Hive is majorly used to do analysis on a huge amount of data which traditional databases cannot process using MapReduce. Although for a small number of records, all other databases are faster than Hive. The real power of Hive is unleashed when you have about 100 million or so records .