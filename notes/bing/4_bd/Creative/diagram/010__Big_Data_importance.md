Big data is the term used to describe the large and complex datasets that are generated from various sources and in various formats. Big data is important because it can help businesses and organizations to gain valuable insights, improve decision making, enhance customer experience, reduce costs, and drive innovation. 

The following diagram illustrates the basic architecture of a big data system using ASCII art:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Data Sources  |    |   Data Storage  |    |   Data Analysis |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
| - Web logs      |    | - Hadoop HDFS   |    | - Spark         |
| - Social media  |    | - NoSQL DBs     |    | - Hive          |
| - Sensors       |    | - Cloud storage |    | - R             |
| - etc.          |    | - etc.          |    | - etc.          |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         +---------------------+---------------------+
                               |
                               |
                               v
                       +-----------------+
                       |                 |
                       |   Data Users    |
                       |                 |
                       +-----------------+
                       |                 |
                       | - Business      |
                       | - Researchers   |
                       | - Government    |
                       | - etc.          |
                       |                 |
                       +-----------------+
```

The diagram shows that data sources generate big data that is stored in various data storage systems. The data storage systems can be distributed, scalable, and fault-tolerant. The data analysis layer performs various tasks such as querying, processing, mining, and visualizing the data using different tools and frameworks. The data analysis layer can also leverage parallel and distributed computing to handle large and complex data. The data users are the end-users who consume the data and use it for various purposes such as business intelligence, research, policy making, and so on.