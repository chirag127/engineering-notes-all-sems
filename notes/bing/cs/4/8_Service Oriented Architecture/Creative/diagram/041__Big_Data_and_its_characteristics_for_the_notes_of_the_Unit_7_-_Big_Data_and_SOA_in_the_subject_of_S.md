The following is a detailed ASCII diagram for Big Data and its characteristics for the notes of the Unit 7 - Big Data and SOA in the subject of Service Oriented Architecture.

Big Data is a term used to describe the massive volumes of data that organizations generate daily. But big data is more than just a large volume of data. The five characteristics of big data are- volume, value, variety, velocity, and veracity  .

Volume is the most important characteristic of big data. It refers to the size of the dataset processed and stored in the big data system. The volume of big data can range from terabytes to petabytes and beyond   .

Value is another important characteristic of big data. It refers to the usefulness and relevance of the information extracted from the data. The value of big data depends on the quality of the data, the analysis methods, and the business objectives   .

Variety is the third characteristic of big data. It refers to the diversity of the data sources, types, and formats. Big data can include structured, semi-structured, and unstructured data from various sources such as text, images, audio, video, social media, sensors, etc   .

Velocity is the fourth characteristic of big data. It refers to the speed of data generation, collection, processing, and analysis. Big data requires fast and real-time processing to handle the continuous flow of data and to provide timely insights   .

Veracity is the fifth characteristic of big data. It refers to the trustworthiness and reliability of the data. Big data can have issues such as incompleteness, inconsistency, ambiguity, noise, and bias that affect the accuracy and quality of the data and the analysis results   .

The following diagram illustrates the basic architecture of a big data system that can handle the five characteristics of big data:

```
+----------------+     +----------------+     +----------------+
| Data Sources   |     | Data Storage   |     | Data Analysis  |
|                |     |                |     |                |
| - Text         |     | - HDFS         |     | - MapReduce    |
| - Images       |     | - NoSQL        |     | - Spark        |
| - Audio        |     | - Cloud        |     | - Hive         |
| - Video        |     |                |     | - Pig          |
| - Social Media |     |                |     | - MLlib        |
| - Sensors      |     |                |     | - Mahout       |
| - etc.         |     |                |     | - etc.         |
+----------------+     +----------------+     +----------------+
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
        +--------------------->+--------------------->+
        | Data Ingestion      | Data Processing      |
        |                     |                      |
        | - Flume             | - Batch              |
        | - Kafka             | - Streaming          |
        | - Sqoop             | - Interactive        |
        | - etc.              | - etc.               |
        |                     |                      |
        +---------------------+----------------------+
```