Big data analytics is the process of uncovering trends, patterns, and correlations in large amounts of raw data to help make data-informed decisions. Big data analytics uses various tools and technologies, such as data mining, AI, predictive analytics, machine learning, and statistical analysis, to analyze data from different sources and in different formats.

### Analytic processes and tools for Big Data

The following diagram illustrates the basic architecture of a big data analytics system, using some of the popular open source tools and technologies.

```
+----------------+    +----------------+    +----------------+    +----------------+
|                |    |                |    |                |    |                |
| Data sources   |    | Data storage   |    | Data processing|    | Data analysis  |
|                |    |                |    |                |    |                |
+----------------+    +----------------+    +----------------+    +----------------+
|                |    |                |    |                |    |                |
| Sensors        |    | Hadoop         |    | Airflow        |    | Tableau        |
| Devices        |    | MongoDB        |    | Spark          |    | PowerBI        |
| Web            |    | Cassandra      |    | Kafka          |    | QlikView       |
| Social media   |    | MySQL          |    | Flink          |    | Excel          |
| Logs           |    |                |    | Storm          |    |                |
|                |    |                |    |                |    |                |
+----------------+    +----------------+    +----------------+    +----------------+
```

The data sources are the origin of the raw data, such as sensors, devices, web, social media, and logs. The data storage is the layer where the data is collected and stored, using tools such as Hadoop, MongoDB, Cassandra, and MySQL. The data processing is the layer where the data is transformed, cleaned, and prepared for analysis, using tools such as Airflow, Spark, Kafka, Flink, and Storm. The data analysis is the layer where the data is explored, visualized, and modeled, using tools such as Tableau, PowerBI, QlikView, and Excel.