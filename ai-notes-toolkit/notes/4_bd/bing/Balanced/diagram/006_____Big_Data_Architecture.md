Big Data Architecture is the framework that defines the components, processes, and technologies needed to capture, store, process, and analyze Big Data. Big Data is the term used to describe large and complex data sets that are beyond the capabilities of traditional data processing systems. Big Data Architecture typically contains multiple data sources, data storage, batch processing, stream processing, data analysis, and data visualization components. There are different types of Big Data Architecture, such as Lambda Architecture, Kappa Architecture, and Microservices Architecture, depending on the use case and requirements.

### Big Data Architecture

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|   Data Sources |       |   Data Storage |       | Data Analysis  |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  - Web logs    |       |  - HDFS        |       |  - Spark       |
|  - Social media|       |  - NoSQL       |       |  - Hive        |
|  - IoT devices |       |  - Data Lake   |       |  - HBase       |
|  - Sensors     |       |  - Data Warehouse|     |  - MongoDB     |
|                |       |                |       |                |
+-------+--------+       +-------+--------+       +--------+-------+
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
+-------+--------+       +-------+--------+       +--------+-------+
|                |       |                |       |                |
| Batch Processing|      | Stream Processing|     | Data Visualization|
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  - MapReduce   |       |  - Kafka       |       |  - Power BI    |
|  - Spark       |       |  - Storm       |       |  - Tableau     |
|  - Pig         |       |  - Spark Streaming|    |  - D3.js       |
|  - Hive        |       |  - Flink       |       |  - Kibana      |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
```