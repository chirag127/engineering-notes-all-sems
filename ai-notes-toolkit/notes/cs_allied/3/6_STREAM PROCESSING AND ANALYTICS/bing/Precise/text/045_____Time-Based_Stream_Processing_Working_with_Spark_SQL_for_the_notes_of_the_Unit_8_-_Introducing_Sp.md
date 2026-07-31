### Time-Based Stream Processing Working with Spark SQL

- Spark Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine.
- It allows ingesting real-time data from various data sources, including storage files, Azure Event Hubs, and Azure IoT Hubs.
- Azure Synapse Analytics has introduced Spark support for data engineering needs, opening the possibility of processing real-time streaming data using popular languages like Python, Scala, and SQL.
- Apache Spark Structured Streaming processes data incrementally, and controlling the trigger interval for batch processing allows you to use Structured Streaming for workloads including near-real-time processing, refreshing databases every 5 minutes or once per hour, or batch processing all new data for a day or week.
- The Spark SQL engine will take care of running it incrementally and continuously and updating the final result as streaming data continues to arrive.
- You can use the Dataset/DataFrame API in Scala, Java, Python, or R to express streaming aggregations, event-time windows, stream-to-batch joins, etc.
- Structured Streaming was introduced in Apache Spark™ 2.0 to meet the stream processing needs.
- The user can express the logic using SQL or Dataset/DataFrame API.
- When a query is executed, Spark SQL will automatically keep track of the maximum observed value of the eventTime column, update the watermark, and clear old state.