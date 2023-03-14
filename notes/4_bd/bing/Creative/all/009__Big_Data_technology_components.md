### Big Data technology components

Big data technology refers to the tools and techniques that are used to handle, process, and analyze large and complex data sets that are beyond the capabilities of traditional database systems. Big data technology enables organizations to extract value from their data sources and gain insights for various purposes, such as business intelligence, customer analytics, machine learning, and data science.

There are many components that make up a big data technology stack, and they can vary depending on the specific use case and requirements of each organization. However, some of the common components that are found in most big data architectures are:

- **Data sources**: These are the origins of the data that are collected and processed by the big data system. Data sources can include various types of data, such as structured, semi-structured, or unstructured data, and they can come from different domains, such as application data stores, web server logs, IoT devices, social media, sensors, etc.
- **Data storage**: This is the component that stores the data for batch or stream processing operations. Data storage can be implemented using different technologies, such as distributed file systems, cloud storage, data lakes, data warehouses, or NoSQL databases. Data storage should be scalable, reliable, and cost-effective, and it should support various data formats and schemas.
- **Data processing**: This is the component that performs the transformation, aggregation, filtering, and enrichment of the data for analysis and reporting. Data processing can be done in batch mode, where large volumes of data are processed periodically, or in stream mode, where data are processed in real time or near real time. Data processing can be implemented using different frameworks, such as MapReduce, Spark, Flink, Storm, Kafka, etc.
- **Data analysis**: This is the component that applies various analytical techniques and algorithms to the data to generate insights, predictions, recommendations, or decisions. Data analysis can be done using different tools and languages, such as SQL, Python, R, SAS, Tableau, Power BI, etc. Data analysis can also involve machine learning and data science methods, such as classification, clustering, regression, anomaly detection, natural language processing, computer vision, etc.
- **Data visualization**: This is the component that presents the results of the data analysis in a graphical or interactive form to the end users or stakeholders. Data visualization can help to communicate the insights, trends, patterns, or outliers in the data, and to support decision making and action taking. Data visualization can be done using different tools and libraries, such as Matplotlib, Seaborn, Plotly, D3.js, etc.

The following diagram shows an example of a big data technology stack, based on the Azure Architecture Center:

```
+-----------------+   +-----------------+   +-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |   |                 |   |                 |
|   Data sources  |   |   Data storage  |   |  Data processing |   |   Data analysis |   | Data visualization
|                 |   |                 |   |                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |   |                 |   |                 |
| - Relational    |   | - Data Lake     |   | - Batch         |   | - SQL           |   | - Dashboards    |
|   databases     |   | - Data Warehouse|   | - Stream        |   | - Python        |   | - Charts        |
| - Web logs      |   | - NoSQL         |   |                 |   | - R             |   | - Maps          |
| - IoT devices   |   |                 |   |                 |   | - SAS           |   | - Graphs        |
| - Social media  |   |                 |   |                 |   | - Tableau       |   |                 |
| - Sensors       |   |                 |   |                 |   | - Power BI      |   |                 |
|                 |   |                 |   |                 |   | - Machine       |   |                 |
|                 |   |                 |   |                 |   |   learning      |   |                 |
|                 |   |                 |   |                 |   | - Data science  |   |                 |
+-----------------+   +-----------------+   +-----------------+   +-----------------+   +-----------------+
        |