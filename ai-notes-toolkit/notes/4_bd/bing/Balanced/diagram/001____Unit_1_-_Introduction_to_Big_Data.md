## Unit 1 - Introduction to Big Data

Big data is the term used to describe the large and complex data sets that are generated from various sources and applications. Big data can be structured, semi-structured, or unstructured, and can have different formats, velocities, and varieties. Big data challenges the traditional methods of data storage, processing, and analysis, and requires new technologies and architectures to handle it efficiently and effectively.

A big data architecture is the design of how the data is managed throughout its life cycle, from ingestion to analysis to disposal. A big data architecture typically consists of the following components:

- Data sources: These are the origins of the data, such as sensors, web logs, social media, databases, etc. Data sources can produce data in different formats, such as text, images, audio, video, etc.
- Data ingestion: This is the process of capturing, extracting, and loading the data from the data sources into a data store or a data processing system. Data ingestion can be done in batch mode, where the data is collected periodically and processed in bulk, or in real-time mode, where the data is streamed and processed as it arrives.
- Data storage: This is the component that stores the data for further processing or analysis. Data storage can be done in different ways, such as using a distributed file system, a relational database, a NoSQL database, a data warehouse, a data lake, etc. Data storage can also be done in different locations, such as on-premises, in the cloud, or in a hybrid mode.
- Data processing: This is the component that transforms, cleans, enriches, and aggregates the data for analysis or consumption. Data processing can be done using different frameworks and tools, such as MapReduce, Spark, Flink, Storm, etc. Data processing can also be done in different modes, such as batch processing, stream processing, or interactive processing.
- Data analysis: This is the component that performs various types of analysis on the data, such as descriptive, diagnostic, predictive, or prescriptive. Data analysis can be done using different techniques and methods, such as machine learning, data mining, statistics, natural language processing, etc. Data analysis can also be done using different tools and platforms, such as R, Python, SAS, Tableau, Power BI, etc.
- Data consumption: This is the component that delivers the results of the data analysis to the end users or applications. Data consumption can be done in different ways, such as using dashboards, reports, visualizations, alerts, recommendations, etc. Data consumption can also be done in different formats, such as text, charts, graphs, maps, etc.

The following diagram shows a possible big data architecture using ASCII art:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Data Sources  +---->+  Data Ingestion+---->+  Data Storage  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
                                                 |
                                                 |
                                                 v
                                        +----------------+
                                        |                |
                                        | Data Processing|
                                        |                |
                                        +----------------+
                                                 |
                                                 |
                                                 v
                                        +----------------+
                                        |                |
                                        |  Data Analysis |
                                        |                |
                                        +----------------+
                                                 |
                                                 |
                                                 v
                                        +----------------+
                                        |                |
                                        | Data Consumption|
                                        |                |
                                        +----------------+
```