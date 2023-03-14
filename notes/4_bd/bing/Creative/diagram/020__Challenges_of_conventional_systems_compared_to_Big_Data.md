One of the challenges of conventional systems compared to big data is the difficulty of handling the volume, variety, velocity and veracity of data. Conventional systems are designed to process structured, relational data that can fit into predefined schemas and tables. Big data, on the other hand, can include structured, semi-structured and unstructured data that can come from various sources and formats, such as text, images, audio, video, social media, sensors, etc. Big data also requires faster processing and analysis to extract meaningful insights and value from the data.

The following diagram illustrates the basic architecture of a conventional system and a big data system using ASCII art:

```
Conventional System:

+-----------------+       +-----------------+       +-----------------+
| Data Sources    |       | Database Server |       | Application     |
| (Structured)    |  ---> | (SQL)           |  ---> | (Reporting,     |
|                 |       |                 |       |  Analytics,     |
|                 |       |                 |       |  Visualization) |
+-----------------+       +-----------------+       +-----------------+

Big Data System:

+-----------------+       +-----------------+       +-----------------+
| Data Sources    |       | Distributed File|       | Application     |
| (Structured,    |  ---> | System (HDFS)   |  ---> | (MapReduce,     |
|  Semi-structured,|      |                 |       |  Spark, Hive,   |
|  Unstructured)  |       |                 |       |  Pig, etc.)     |
+-----------------+       +-----------------+       +-----------------+
```

As you can see, the conventional system relies on a single database server that can store and query structured data using SQL. The application layer can then access the data and perform reporting, analytics and visualization tasks. The big data system, however, uses a distributed file system (such as HDFS) that can store and process large and diverse data sets across multiple nodes. The application layer can then use various frameworks and tools (such as MapReduce, Spark, Hive, Pig, etc.) to perform parallel and scalable data processing and analysis tasks.