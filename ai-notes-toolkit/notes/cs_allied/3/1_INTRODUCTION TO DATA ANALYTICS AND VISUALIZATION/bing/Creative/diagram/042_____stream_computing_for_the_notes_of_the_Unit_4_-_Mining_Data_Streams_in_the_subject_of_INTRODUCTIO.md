### Stream Computing

Stream computing is a programming paradigm that deals with data streams, or sequences of events in time, as the central input and output objects of computation. Stream computing enables organizations to process data streams which are always on and never ceasing, and to analyze the data in real time as it streams in to increase speed and accuracy when dealing with data handling and analysis .

Some of the key concepts and features of stream computing are:

- **Stream sources and sinks**: Stream sources are the software or hardware sensors that generate data streams, such as web logs, social media posts, sensor readings, etc. Stream sinks are the destinations where the processed data streams are sent, such as databases, dashboards, alerts, etc.
- **Stream operators**: Stream operators are the functions that perform computations on the data streams, such as filtering, aggregation, transformation, joining, etc. Stream operators can be stateless or stateful, depending on whether they need to store information from previous events or not.
- **Stream queries**: Stream queries are the expressions that specify what stream operators to apply on what data streams, and how to combine the results. Stream queries can be continuous or windowed, depending on whether they run indefinitely or over a fixed time interval or number of events.
- **Stream applications**: Stream applications are the programs that implement stream queries and run on stream computing platforms. Stream applications can be written in various languages, such as SQL, Java, Python, etc.
- **Stream computing platforms**: Stream computing platforms are the systems that provide the infrastructure and the runtime environment for stream applications. Stream computing platforms can be distributed or centralized, depending on whether they run on multiple nodes or a single node. Stream computing platforms can also provide features such as fault tolerance, scalability, load balancing, security, etc.

Some of the examples of stream computing platforms are:

- **IBM Streams**: IBM Streams is a distributed stream processing platform that supports stream applications written in SPL (Streams Processing Language), Java, Python, and Scala. IBM Streams provides features such as parallelism, elasticity, high availability, analytics libraries, etc.
- **Apache Flink**: Apache Flink is an open source distributed stream processing platform that supports stream applications written in Java, Scala, and Python. Apache Flink provides features such as low latency, high throughput, state management, event time processing, etc.
- **Apache Spark Streaming**: Apache Spark Streaming is an extension of Apache Spark that supports stream applications written in Java, Scala, Python, and R. Apache Spark Streaming provides features such as micro-batching, fault tolerance, integration with Spark SQL and MLlib, etc.
- **Apache Kafka Streams**: Apache Kafka Streams is a library that enables stream applications written in Java or Scala to process data streams from Apache Kafka. Apache Kafka Streams provides features such as stateful processing, exactly-once semantics, interactive queries, etc.