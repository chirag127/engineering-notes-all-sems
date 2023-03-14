Intelligent data analysis (IDA) is the application of advanced analytical techniques, such as data mining, statistical analysis, predictive modeling, and machine learning, on big data sets to discover useful patterns, trends, and insights that can support decision making  . IDA can also leverage artificial intelligence (AI) to automate and enhance data preparation, data visualization, and other complex analytical tasks that would otherwise be labor-intensive and time-consuming  . IDA can help users work with, manipulate, and surface actionable insights faster from large, complex datasets  .

The following diagram illustrates the basic architecture of a typical IDA system:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Data Sources  |----->|   Data Storage  |----->|   Data Analysis |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
     |  |  |  |               |  |  |  |               |  |  |  |
     |  |  |  |               |  |  |  |               |  |  |  |
     v  v  v  v               v  v  v  v               v  v  v  v
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
| Data Extraction |      | Data Processing |      | Data Mining     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
     |  |  |  |               |  |  |  |               |  |  |  |
     |  |  |  |               |  |  |  |               |  |  |  |
     v  v  v  v               v  v  v  v               v  v  v  v
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
| Data Cleansing  |      | Data Integration|      | Statistical     |
|                 |      |                 |      | Analysis        |
+-----------------+      +-----------------+      +-----------------+
     |  |  |  |               |  |  |  |               |  |  |  |
     |  |  |  |               |  |  |  |               |  |  |  |
     v  v  v  v               v  v  v  v               v  v  v  v
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
| Data Validation |      | Data Selection  |      | Predictive      |
|                 |      |                 |      | Modeling        |
+-----------------+      +-----------------+      +-----------------+
     |  |  |  |               |  |  |  |               |  |  |  |
     |  |  |  |               |  |  |  |               |  |  |  |
     v  v  v  v               v  v  v  v               v  v  v  v
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
| Data Enrichment |      | Data Reduction  |      | Machine Learning|
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
     |  |  |  |               |  |  |  |               |  |  |  |
     |  |  |  |               |  |  |  |               |  |  |  |
     v  v  v  v               v  v  v  v               v  v  v  v
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
| Data Annotation |      | Data Sampling   |      | Artificial      |
|                 |      |                 |      | Intelligence    |
+-----------------+      +-----------------+      +-----------------+
     |  |  |  |               |  |  |  |               |  |  |  |
     |  |  |