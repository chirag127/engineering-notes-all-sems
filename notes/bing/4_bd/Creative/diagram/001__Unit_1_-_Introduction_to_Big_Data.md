## Unit 1 - Introduction to Big Data

Big data is the term used to describe the large and complex datasets that are generated from various sources and require special techniques and technologies to store, process, and analyze. Big data can be characterized by the 5 Vs: volume, velocity, variety, veracity, and value.

A big data architecture is the design of a system that can handle the ingestion, processing, and analysis of big data. A big data architecture typically consists of the following components:

- Data sources: These are the originators of the data, such as sensors, applications, web servers, social media, etc.
- Data ingestion: This is the process of capturing, validating, and transferring the data from the sources to a data store or a processing engine. Data ingestion can be done in batch mode (periodically) or in real-time (streaming).
- Data storage: This is the component that stores the raw or processed data in a scalable and reliable way. Data storage can be done using various technologies, such as relational databases, NoSQL databases, data warehouses, data lakes, etc.
- Data processing: This is the component that transforms, enriches, and analyzes the data using various techniques, such as ETL (extract, transform, load), ELT (extract, load, transform), MapReduce, Spark, etc.
- Data analysis: This is the component that provides insights and answers from the data using various tools, such as BI (business intelligence), ML (machine learning), AI (artificial intelligence), etc.
- Data consumption: This is the component that delivers the data or the insights to the end users or applications, such as dashboards, reports, APIs, etc.

The following diagram illustrates the basic architecture of a big data system using ASCII art:

```
+-------------+     +-------------+     +-------------+
| Data sources|---->| Data ingestion|---->| Data storage |
+-------------+     +-------------+     +-------------+
                                   |           |
                                   |           |
                                   v           v
                             +-------------+     +-------------+
                             | Data processing|---->| Data analysis |
                             +-------------+     +-------------+
                                                   |
                                                   |
                                                   v
                                             +-------------+
                                             | Data consumption|
                                             +-------------+
```