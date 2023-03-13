
## Hadoop Eco System Frameworks , Pig , Hive and HBase

Hadoop is an open source software platform for distributed storage and distributed processing of large datasets on computer clusters built from commodity hardware. It provides a distributed file system (HDFS) and a framework for the analysis and transformation of large datasets using the MapReduce programming model. Pig, Hive, and HBase are three popular frameworks that are part of the Hadoop ecosystem.

**Pig**

Pig is a high-level data-flow language and execution framework for parallel computation. Pig programs are written in a language called Pig Latin, which is a data flow language similar to SQL. Pig Latin has a set of relational and procedural operators that can be used to perform data analysis. Pig programs are compiled into MapReduce jobs and are executed on the Hadoop cluster.

**Hive**

Hive is a data warehouse infrastructure built on top of Hadoop. It provides a SQL-like language called HiveQL, which is used to query the data stored in the Hadoop cluster. HiveQL is a declarative language, and it is used to specify the transformation and analysis that needs to be done on the data. Hive also provides a data model for working with data stored in the Hadoop cluster.

**HBase**

HBase is a distributed, column-oriented database built on top of the Hadoop Distributed File System (HDFS). It provides a data model that is similar to a traditional database, but it is optimized for working with large datasets that are stored in the Hadoop cluster. HBase provides a low-latency, random-access interface to data stored in the Hadoop cluster, and it also provides an API for programmatic access to the data.