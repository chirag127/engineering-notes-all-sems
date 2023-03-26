 Here is the content in markdown format without any feeling or friendliness, being formal and without any emojis or external links:

## Unit 4 - Apache Spark as a Stream-Processing Engine

1. Spark Streaming - Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams.
2. DStream - The basic abstraction in Spark Streaming is a Discretized Stream or DStream, which represents a continuous stream of data divided into batches.
3. Transformations on DStreams - DStreams support many of the transformations available on normal Spark RDDs, such as map, reduce, filter, flatMap, etc.  
4. Output Operations on DStreams - DStreams also support output operations like printing, saving to files, or writing to databases to get data out of the system or to perform further analysis.
5. Architecture - Spark Streaming receives live input data streams and divides the data into batches, which are then processed by the Spark engine to generate the final results in batches.
6. Fault-tolerance Semantics - Spark Streaming provides exactly-once semantics by performing an idempotent operation to update the state during the processing of each record (like updating a counter or an accumulator).
7. Performance - Spark Streaming leverages Spark's fast scheduling capability to perform streaming analytics with high throughput and low latency.

The content outlines the key points regarding Apache Spark as a Stream-Processing Engine in a formal manner without any feeling or friendliness and in markdown format as requested. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.