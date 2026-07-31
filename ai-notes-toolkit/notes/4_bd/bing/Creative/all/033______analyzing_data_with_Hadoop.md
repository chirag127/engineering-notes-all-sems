#### Analyzing Data with Hadoop

- Hadoop is an open source software framework and platform for storing, analyzing and processing large volumes of data in a distributed manner on clusters of commodity hardware .
- Hadoop consists of two main components: Hadoop Distributed File System (HDFS) and Hadoop MapReduce. HDFS is a distributed file system that provides high-throughput access to data across the cluster. MapReduce is a programming model and an execution engine that enables parallel processing of data using key-value pairs.
- Hadoop can run various analytical algorithms on the data stored in HDFS, such as machine learning, data mining, text analysis, sentiment analysis, etc. Hadoop can also integrate with other tools and frameworks that provide additional functionality and features for data analysis, such as Hive, Pig, Spark, HBase, etc .
- Hadoop can help in the analysis of big data by providing the following benefits :
  - Scalability: Hadoop can scale up from a single node to thousands of nodes, and handle petabytes of data without any loss of performance or reliability.
  - Cost-effectiveness: Hadoop can run on commodity hardware, which reduces the cost of storage and processing. Hadoop also uses data compression and replication techniques to optimize the use of disk space and network bandwidth.
  - Flexibility: Hadoop can handle any type of data, whether structured, semi-structured or unstructured, and in any format, such as text, images, audio, video, etc. Hadoop can also process data in batch or real-time mode, depending on the application requirements.
  - Fault-tolerance: Hadoop can automatically recover from failures and errors, by replicating the data across multiple nodes and re-executing the failed tasks on other nodes.
  - Security: Hadoop can provide authentication, authorization, encryption and auditing mechanisms to protect the data and the cluster from unauthorized access and malicious attacks.

- To analyze data with Hadoop, the following steps are typically involved:
  - Launch a Hadoop cluster using a service provider such as Amazon EMR, or set up your own cluster using Hadoop installation and configuration guides.
  - Define the schema and create a table for the data stored in HDFS or another data source such as Amazon S3, using a tool such as Hive or Pig, or writing your own MapReduce code.
  - Analyze the data using a query language such as HiveQL or Pig Latin, or writing your own MapReduce code, and write the results back to HDFS or another data source.
  - Download and view the results on your computer, or use a visualization tool such as Tableau or Power BI to create charts and graphs.

- A simple example of analyzing data with Hadoop is shown below:

  - The data is a sample of web server logs stored in Amazon S3, in the following format:

    ```
    127.0.0.1 - - [15/Mar/2023:14:00:34 +0000] "GET /index.html HTTP/1.1" 200 1234
    127.0.0.2 - - [15/Mar/2023:14:00:35 +0000] "GET /about.html HTTP/1.1" 200 5678
    127.0.0.3 - - [15/Mar/2023:14:00:36 +0000] "GET /contact.html HTTP/1.1" 404 9012
    ```

  - The goal is to count the number of hits for each page and the total bytes transferred for each page.

  - The schema and table for the data are defined using Hive as follows:

    ```
    CREATE EXTERNAL TABLE weblogs (
      ip STRING,
      time STRING,
      request STRING,
      status INT,
      size INT
    )
    ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe'
    WITH SERDEPROPERTIES (
      "input.regex" = "([^ ]*) - - \\[([^\\]]*)\\] \"([^\"]*)\" ([0-9]*) ([0-9]*)"
    )
    LOCATION 's3://mybucket/weblogs/';
    ```

  - The data is analyzed using a HiveQL script as follows:

    ```
    SELECT page, COUNT(*) AS hits, SUM(size) AS bytes
    FROM (
      SELECT split(request, ' ')[1] AS page

```
