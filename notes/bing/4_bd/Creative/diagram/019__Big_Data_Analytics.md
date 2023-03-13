Big data analytics is the use of advanced analytic techniques against large data sets, including structured/unstructured data and streaming/batch data. Big data analytics requires a big data architecture that can handle the ingestion, processing, and analysis of data that is too large or complex for traditional database systems .

### Big Data Analytics

The following diagram illustrates the basic architecture of a big data analytics system using ASCII art:

```
+-----------------+    +-----------------+    +-----------------+
| Data Sources    |    | Data Storage    |    | Data Analysis   |
|                 |    |                 |    |                 |
| - Web logs      |    | - Data lake     |    | - Machine       |
| - Social media  |    | - Data warehouse|    |   learning      |
| - IoT devices   |    | - NoSQL database|    | - BI tools      |
| - Sensors       |    | - HDFS          |    | - SQL queries   |
| - ...           |    | - ...           |    | - ...           |
+-----------------+    +-----------------+    +-----------------+
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
+-----------------+    +-----------------+    +-----------------+
| Data Ingestion  |    | Data Processing |    | Data Consumption|
|                 |    |                 |    |                 |
| - Kafka         |    | - Spark         |    | - Dashboards    |
| - Flume         |    | - MapReduce     |    | - Reports       |
| - Sqoop         |    | - Hive          |    | - Visualizations|
| - NiFi          |    | - Pig           |    | - ...           |
| - ...           |    | - ...           |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The diagram shows the three main layers of a big data analytics system: data sources, data storage, and data analysis. Each layer has different components that perform specific functions.

- Data sources are the origin of the data, such as web logs, social media, IoT devices, sensors, etc. They generate data in various formats and velocities.
- Data storage is the layer that stores the data in different formats and structures, such as data lake, data warehouse, NoSQL database, HDFS, etc. They provide scalability, reliability, and accessibility for the data.
- Data analysis is the layer that applies advanced analytic techniques to the data, such as machine learning, BI tools, SQL queries, etc. They provide insights, predictions, and recommendations for the data.

The diagram also shows the three supporting layers of a big data analytics system: data ingestion, data processing, and data consumption. Each layer has different components that enable the flow and transformation of the data.

- Data ingestion is the layer that collects and transfers the data from the data sources to the data storage, such as Kafka, Flume, Sqoop, NiFi, etc. They handle the challenges of data volume, variety, and velocity.
- Data processing is the layer that processes and transforms the data in the data storage, such as Spark, MapReduce, Hive, Pig, etc. They handle the challenges of data quality, consistency, and complexity.
- Data consumption is the layer that consumes and presents the data from the data analysis, such as dashboards, reports, visualizations, etc. They handle the challenges of data interpretation, communication, and action.