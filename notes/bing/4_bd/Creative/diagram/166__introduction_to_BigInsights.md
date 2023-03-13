BigInsights is an IBM product that helps firms analyze the increasing volume, velocity and veracity of data of their interest. BigInsights does not replace a relational database management system (DBMS) or a traditional data warehouse, but rather complements them by providing a scalable and flexible platform for processing and analyzing large and complex data sets using Apache Hadoop and its ecosystem of tools.

#### Introduction to BigInsights

The following diagram illustrates the basic architecture of BigInsights using ASCII art:

```
+----------------------------------------------------+
|                                                    |
| IBM BigInsights                                    |
|                                                    |
| +--------------------------------+                 |
| |                                |                 |
| | IBM Open Platform with Apache  |                 |
| | Hadoop                        |                 |
| |                                |                 |
| | +----------------+ +--------+ |                 |
| | |                | |        | |                 |
| | | Apache Hadoop  | | Apache | |                 |
| | | Core           | | Spark  | |                 |
| | |                | |        | |                 |
| | +----------------+ +--------+ |                 |
| |                                |                 |
| +--------------------------------+                 |
|                                                    |
| +--------------------------------+                 |
| |                                |                 |
| | IBM BigInsights for Apache     |                 |
| | Hadoop                         |                 |
| |                                |                 |
| | +--------+ +---------+ +-----+ |                 |
| | |        | |         | |     | |                 |
| | | Big SQL| | BigSheets| | Big| |                 |
| | |        | |         | | R   | |                 |
| | +--------+ +---------+ +-----+ |                 |
| |                                |                 |
| +--------------------------------+                 |
|                                                    |
+----------------------------------------------------+
```

BigInsights consists of two main modules:

- IBM Open Platform with Apache Hadoop: This module provides the core components of Apache Hadoop, such as HDFS, MapReduce, YARN, ZooKeeper, etc. It also includes Apache Spark, a fast and general engine for large-scale data processing that supports SQL, streaming, machine learning, and graph analytics.
- IBM BigInsights for Apache Hadoop: This module provides additional value-added components that enhance the capabilities of Apache Hadoop, such as Big SQL, a SQL engine that allows users to query data stored in Hadoop using standard SQL syntax and JDBC/ODBC drivers; BigSheets, a spreadsheet-like interface that allows users to explore, visualize, and analyze data in Hadoop using a web browser; Big R, a framework that allows users to run R scripts on Hadoop data using a familiar R syntax and environment; and other services such as Text Analytics, Spectrum Scale (GPFS), and Platform Symphony.