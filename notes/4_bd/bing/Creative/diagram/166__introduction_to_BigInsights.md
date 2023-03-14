BigInsights is an IBM product that helps firms analyze the increasing volume, velocity and veracity of data of their interest. It is based on the open source Apache Hadoop framework, which is a distributed system for processing large-scale data sets using a cluster of commodity hardware. BigInsights does not replace a relational database management system (DBMS) or a traditional data warehouse, but rather complements them by enabling the analysis of unstructured or semi-structured data, such as text, images, audio, video, social media, sensor data, etc. BigInsights also provides various tools and features to enhance the Hadoop ecosystem, such as Big SQL, BigSheets, Big R, Text Analytics, BigInsights Enterprise Management, etc.

#### Introduction to BigInsights

The following diagram illustrates the basic architecture of BigInsights:

```
+-----------------------------------------------------------------+
| BigInsights Enterprise Management                              |
| +-------------------------------------------------------------+ |
| | BigInsights Console                                         | |
| | +-----------------+ +-----------------+ +-----------------+ | |
| | | Cluster Manager | | Service Monitor | | Application     | | |
| | |                 | |                 | | Accelerator     | | |
| | +-----------------+ +-----------------+ +-----------------+ | |
| +-------------------------------------------------------------+ |
+-----------------------------------------------------------------+
| BigInsights Tools and Applications                              |
| +-------------------------------------------------------------+ |
| | Big SQL           | BigSheets        | Big R              | |
| | +---------------+ | +---------------+ | +---------------+ | |
| | | SQL interface | | | Spreadsheet   | | | R interface   | | |
| | | to Hadoop     | | | for Hadoop    | | | to Hadoop     | | |
| | +---------------+ | +---------------+ | +---------------+ | |
| | Text Analytics    | Machine Learning | Geospatial Toolkit | |
| | +---------------+ | +---------------+ | +---------------+ | |
| | | Natural       | | | Algorithms    | | | Spatial       | | |
| | | language      | | | for Hadoop    | | | analysis      | | |
| | | processing    | | |                | | | for Hadoop    | | |
| | +---------------+ | +---------------+ | +---------------+ | |
| +-------------------------------------------------------------+ |
+-----------------------------------------------------------------+
| Hadoop Ecosystem                                                |
| +-------------------------------------------------------------+ |
| | Hadoop Distributed File System (HDFS)                       | |
| | +---------------------------------------------------------+ | |
| | | NameNode | DataNode | DataNode | DataNode | DataNode   | | |
| | +---------------------------------------------------------+ | |
| | MapReduce                                                   | |
| | +---------------------------------------------------------+ | |
| | | JobTracker | TaskTracker | TaskTracker | TaskTracker  | | |
| | +---------------------------------------------------------+ | |
| | YARN                                                       | |
| | +---------------------------------------------------------+ | |
| | | ResourceManager | NodeManager | NodeManager | NodeManager| | |
| | +---------------------------------------------------------+ | |
| | Pig | Hive | HBase | ZooKeeper | Oozie | Flume | Sqoop | ... | |
| +-------------------------------------------------------------+ |
+-----------------------------------------------------------------+
| Hardware Cluster                                                |
| +-------------------------------------------------------------+ |
| | Node 1 | Node 2 | Node 3 | Node 4 | Node 5 | Node 6 | ...   | |
| +-------------------------------------------------------------+ |
+-----------------------------------------------------------------+
```