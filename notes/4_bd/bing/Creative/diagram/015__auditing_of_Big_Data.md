Auditing of big data is the process of evaluating the quality, reliability, security and governance of data that is collected, stored, processed and analyzed by big data systems. Auditing of big data can help organizations to identify and mitigate risks, ensure compliance with regulations and standards, and improve the performance and value of their data-driven initiatives.

One possible way to draw a diagram for auditing of big data is to use the following symbols:

- A rectangle with rounded corners represents a data source or a data sink
- A rectangle with straight corners represents a data processing component or a tool
- A circle represents a data flow or a data stream
- A dashed line represents a control or a governance mechanism
- A solid line represents a dependency or a relationship

Using these symbols, a simplified diagram for auditing of big data could look like this:

```
    +-----------------+       +-----------------+       +-----------------+
    | Data Source 1   |       | Data Source 2   |       | Data Source 3   |
    | (e.g., web logs)|       | (e.g., CRM data)|       | (e.g., sensors) |
    +-----------------+       +-----------------+       +-----------------+
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             v                       v                       v
    +-----------------+       +-----------------+       +-----------------+
    | Data Ingestion  |       | Data Ingestion  |       | Data Ingestion  |
    | (e.g., Flume)   |       | (e.g., Kafka)   |       | (e.g., Sqoop)   |
    +-----------------+       +-----------------+       +-----------------+
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             v                       v                       v
    +-----------------+       +-----------------+       +-----------------+
    | Data Storage    |       | Data Storage    |       | Data Storage    |
    | (e.g., HDFS)    |       | (e.g., HBase)   |       | (e.g., Hive)    |
    +-----------------+       +-----------------+       +-----------------+
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             v                       v                       v
    +-----------------+       +-----------------+       +-----------------+
    | Data Processing |       | Data Processing |       | Data Processing |
    | (e.g., MapReduce)|      | (e.g., Spark)   |       | (e.g., Pig)     |
    +-----------------+       +-----------------+       +-----------------+
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             v                       v                       v
    +-----------------+       +-----------------+       +-----------------+
    | Data Analysis   |       | Data Analysis   |       | Data Analysis   |
    | (e.g., R)       |