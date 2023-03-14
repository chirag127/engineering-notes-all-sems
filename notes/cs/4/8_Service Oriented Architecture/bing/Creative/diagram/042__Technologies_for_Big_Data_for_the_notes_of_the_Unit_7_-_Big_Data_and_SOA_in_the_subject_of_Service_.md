According to the search results, there are four types of big data technologies: data storage, data mining, data analytics, and data visualization. Data storage technologies deal with fetching, storing, and managing big data. Data mining technologies extract useful patterns and trends from the raw data. Data analytics technologies transform data into information that can be used to drive business decisions. Data visualization technologies present data in graphical or interactive forms to communicate insights.

The following diagram illustrates the basic architecture of a big data system using some of the popular tools for each type of technology:

```
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|  Data Storage  |     |  Data Mining   |     | Data Analytics |     | Data Visualization
|                |     |                |     |                |     |                |
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|  Apache Hadoop |     |  Rapidminer    |     |  Apache Spark  |     |  Tableau       |
|  MongoDB       |     |  Presto        |     |  R             |     |  Power BI      |
|                |     |                |     |                |     |                |
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|  Fetch         |---->|  Extract       |---->|  Transform     |---->|  Present       |
|  Store         |     |  Analyze       |     |  Analyze       |     |  Explore       |
|  Manage        |     |                |     |                |     |                |
+----------------+     +----------------+     +----------------+     +----------------+
```