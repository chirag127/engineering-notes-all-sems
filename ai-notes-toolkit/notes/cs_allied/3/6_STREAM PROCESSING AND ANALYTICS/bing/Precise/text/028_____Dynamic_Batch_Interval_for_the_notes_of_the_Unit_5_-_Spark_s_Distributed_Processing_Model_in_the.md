### Dynamic Batch Interval

- Spark Streaming receives live input data streams and divides the data into batches, which are then processed by the Spark engine to generate the final stream of results in batches.
- Spark Streaming provides a high-level abstraction called discretized stream or DStream, which represents a continuous stream of data.
- Each batch of streaming data is represented by an RDD, which is Spark’s concept for a distributed dataset. Therefore a DStream is just a series of RDDs.
- Unlike a solely event-driven process, a Spark Stream batches input data into time windows, such as a 2-second slice, and then transforms each batch of data using map, reduce, join, and extract operations.
- The Spark Stream then writes the transformed data out to filesystems, databases, dashboards, and the console.
- Controlling the trigger interval for batch processing allows you to use Structured Streaming for workloads including near-real time processing, refreshing databases every 5 minutes or once per hour, or batch processing all new data for a day or week.
- Batch interval is the time in seconds how long data will be collected before dispatching processing on it. For example, if you set the batch interval to 5 seconds, Spark Streaming will collect data for 5 seconds and then kick out calculation on RDD with that data.
- Spark Streaming is developed to process real-time stream data analytics by using a micro-batch approach.
- The unified programming model of Spark Steaming leads to some unique benefits over other traditional streaming systems, such as fast recovery from failures, better load balancing, and resource usage.