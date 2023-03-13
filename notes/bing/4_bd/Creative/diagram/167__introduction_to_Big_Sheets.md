Big Sheets is a spreadsheet-style tool for business analysts provided with IBM InfoSphere BigInsights, a platform based on the open source Apache Hadoop project. Big Sheets enables non-programmers to iteratively explore, manipulate, and visualize data stored in your distributed file system.

#### Introduction to Big Sheets

The following diagram illustrates the basic architecture of Big Sheets:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Web Browser    |       |  BigInsights    |       |  Hadoop Cluster |
|                 |       |  Console        |       |                 |
|  +-----------+  |       |                 |       |  +-----------+  |
|  | BigSheets |  |       |  +-----------+  |       |  | HDFS      |  |
|  | UI        |  |       |  | BigSheets |  |       |  |           |  |
|  +-----------+  |       |  | Engine    |  |       |  +-----------+  |
|                 |       |  +-----------+  |       |  +-----------+  |
+-----------------+       |                 |       |  | MapReduce |  |
                          |  +-----------+  |       |  |           |  |
                          |  | Big SQL   |  |       |  +-----------+  |
                          |  |           |  |       |                 |
                          |  +-----------+  |       +-----------------+
                          |                 |
                          +-----------------+
```

The diagram shows the following components:

- Web Browser: The user interface for Big Sheets. It allows the user to create, edit, and view worksheets that contain data from the Hadoop cluster.
- BigInsights Console: The web-based management console for IBM InfoSphere BigInsights. It provides access to various tools and services, including Big Sheets.
- Big Sheets Engine: The core component of Big Sheets. It handles the communication between the web browser and the Hadoop cluster. It also performs data processing and transformation using Big SQL and MapReduce.
- Big SQL: A SQL engine that runs on top of Hadoop. It allows Big Sheets to query and manipulate data using SQL syntax and functions.
- Hadoop Cluster: The distributed system that stores and processes large amounts of data. It consists of two main components: HDFS and MapReduce.
- HDFS: The Hadoop Distributed File System. It is a scalable and fault-tolerant file system that stores data across multiple nodes in the cluster.
- MapReduce: The programming model and framework for parallel processing of data in Hadoop. It divides the data into smaller chunks and assigns them to different nodes for processing.